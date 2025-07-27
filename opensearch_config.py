"""
OpenSearch 설정 및 유틸리티 함수들
"""

import boto3
import json
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 설정 파일에서 import
from config import (
    OPENSEARCH_ENDPOINT,
    OPENSEARCH_INDEX_NAME, 
    OPENSEARCH_REGION,
    KOREAN_MODEL_NAME,
    DEFAULT_DUPLICATION_THRESHOLD
)
korean_model = None

# 인덱스 생성 여부 추적
index_created = False

def load_korean_model():
    """한국어 임베딩 모델 로딩"""
    global korean_model
    if korean_model is None:
        print("[임베딩] 한국어 모델 로딩 중: jhgan/ko-sroberta-multitask")
        korean_model = SentenceTransformer(KOREAN_MODEL_NAME)
        print("[임베딩] 한국어 모델 로딩 완료!")
    return korean_model

def generate_korean_embedding(text):
    """한국어 텍스트의 임베딩 생성"""
    model = load_korean_model()
    embedding = model.encode(text)
    return embedding.tolist()

def get_opensearch_client():
    """OpenSearch 클라이언트 생성"""
    try:
        # AWS 자격 증명 설정
        credentials = boto3.Session().get_credentials()
        awsauth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            OPENSEARCH_REGION,
            'aoss',
            session_token=credentials.token
        )
        
        # OpenSearch 클라이언트 생성
        client = OpenSearch(
            hosts=[{'host': OPENSEARCH_ENDPOINT, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            pool_maxsize=20
        )
        
        return client
        
    except Exception as e:
        print(f"[OpenSearch] 클라이언트 생성 실패: {e}")
        return None

def check_duplicate_in_opensearch(question_text, threshold=DEFAULT_DUPLICATION_THRESHOLD):
    """
    OpenSearch에서 중복 퀴즈 검사
    
    Args:
        question_text: 검사할 질문 텍스트
        threshold: 코사인 유사도 임계값 (기본값: 0.65)
    
    Returns:
        tuple: (중복여부, 중복퀴즈목록, 오류메시지)
    """
    try:
        client = get_opensearch_client()
        if not client:
            return False, [], "OpenSearch 클라이언트 생성 실패"
        
        # 새 질문의 임베딩 생성
        new_embedding = generate_korean_embedding(question_text)
        
        # KNN 검색 쿼리
        knn_query = {
            "size": 10,
            "query": {
                "knn": {
                    "embedding": {
                        "vector": new_embedding,
                        "k": 10
                    }
                }
            }
        }
        
        # 검색 실행
        result = client.search(index=OPENSEARCH_INDEX_NAME, body=knn_query)
        
        # 코사인 유사도로 중복 판단
        duplicates = []
        for hit in result['hits']['hits']:
            if 'embedding' not in hit['_source']:
                continue
                
            stored_embedding = hit['_source']['embedding']
            
            # 코사인 유사도 직접 계산
            cosine_sim = cosine_similarity([new_embedding], [stored_embedding])[0][0]
            
            if cosine_sim > threshold:
                duplicates.append({
                    'question': hit['_source'].get('question', ''),
                    'quiz_id': hit['_source'].get('quiz_id', ''),
                    'category': hit['_source'].get('category', ''),
                    'cosine_similarity': cosine_sim,
                    'document_id': hit['_id']
                })
        
        # 유사도 순으로 정렬
        duplicates.sort(key=lambda x: x['cosine_similarity'], reverse=True)
        
        return len(duplicates) > 0, duplicates, None
        
    except Exception as e:
        error_msg = f"OpenSearch 중복 검사 실패: {e}"
        print(f"[OpenSearch] {error_msg}")
        return False, [], error_msg

def save_quiz_to_opensearch(quiz_data):
    """
    퀴즈 데이터를 OpenSearch에 저장
    
    Args:
        quiz_data: 퀴즈 데이터 딕셔너리
    
    Returns:
        tuple: (성공여부, 문서ID, 오류메시지)
    """
    global index_created
    
    try:
        client = get_opensearch_client()
        if not client:
            return False, None, "OpenSearch 클라이언트 생성 실패"
        
        # 인덱스가 존재하지 않으면 생성 (최초 1회만)
        if not index_created:
            try:
                if not client.indices.exists(index=OPENSEARCH_INDEX_NAME):
                    print(f"[OpenSearch] 인덱스 생성 중: {OPENSEARCH_INDEX_NAME}")
                    index_mapping = {
                        "mappings": {
                            "properties": {
                                "quiz_id": {"type": "keyword"},
                                "category": {"type": "text"},
                                "question_id": {"type": "integer"},  # 실제: integer
                                "quiz_type": {"type": "keyword"},  # 실제 필드명
                                "type": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                },
                                "question": {"type": "text"},
                                "options": {"type": "text"},
                                "correct_answer": {"type": "text"},
                                "embedding": {
                                    "type": "knn_vector",
                                    "dimension": 768,
                                    "method": {
                                        "engine": "nmslib",
                                        "space_type": "l2",  # 실제 인덱스와 일치
                                        "name": "hnsw",
                                        "parameters": {
                                            "ef_construction": 128,
                                            "m": 24
                                        }
                                    }
                                },
                                "created_at": {"type": "date"},
                                "model_used": {"type": "keyword"},  # 실제 필드 추가
                                "topic": {"type": "text"}  # 실제 필드 추가
                            }
                        }
                    }
                    client.indices.create(index=OPENSEARCH_INDEX_NAME, body=index_mapping)
                    print(f"[OpenSearch] 인덱스 생성 완료: {OPENSEARCH_INDEX_NAME}")
                
                index_created = True
                
            except Exception as index_error:
                print(f"[OpenSearch] 인덱스 생성 실패: {index_error}")
                # 인덱스 생성 실패해도 저장은 시도해봄
        
        # 질문 텍스트로 임베딩 생성
        question_text = quiz_data.get("Question", "")
        if not question_text:
            return False, None, "질문 텍스트가 없습니다"
        
        embedding = generate_korean_embedding(question_text)
        
        # 저장할 문서 구성 (기존 인덱스 스키마에 맞춤)
        document = {
            "quiz_id": quiz_data.get("QuizID", 1),  # 기존: keyword 타입이지만 숫자 사용
            "category": quiz_data.get("Category", ""),
            "question_id": quiz_data.get("QuestionID", 101),  # 기존: integer 타입
            "quiz_type": quiz_data.get("Type", ""),  # 기존 필드명: quiz_type
            "type": quiz_data.get("Type", ""),  # 기존 필드: type도 있음
            "question": question_text,
            "options": quiz_data.get("Options", []),
            "correct_answer": quiz_data.get("IsCorrect", ""),
            "embedding": embedding,
            "created_at": "2025-07-27T23:26:11.846799",  # 기존 형식에 맞춤
            "model_used": "jhgan/ko-sroberta-multitask",  # 기존 필드 추가
            "topic": "Generated Quiz"  # 기존 필드 추가
        }
        
        # OpenSearch에 저장
        response = client.index(
            index=OPENSEARCH_INDEX_NAME,
            body=document
        )
        
        return True, response['_id'], None
        
    except Exception as e:
        error_msg = f"OpenSearch 저장 실패: {e}"
        print(f"[OpenSearch] {error_msg}")
        return False, None, error_msg

def get_opensearch_stats():
    """OpenSearch 인덱스 통계 정보 조회"""
    try:
        client = get_opensearch_client()
        if not client:
            return None
        
        # 간단한 count 쿼리 사용
        count_response = client.count(index=OPENSEARCH_INDEX_NAME)
        doc_count = count_response['count']
        
        return {
            'document_count': doc_count,
            'index_name': OPENSEARCH_INDEX_NAME,
            'endpoint': OPENSEARCH_ENDPOINT
        }
        
    except Exception as e:
        print(f"[OpenSearch] 통계 조회 실패: {e}")
        return None

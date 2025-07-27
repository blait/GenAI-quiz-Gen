#!/usr/bin/env python3
"""
다양한 한국어 임베딩 모델 비교 테스트
K-pop 퀴즈 중복 검사에 가장 적합한 모델 선택
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logging
import time
import numpy as np

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 테스트할 한국어 모델들
KOREAN_MODELS = [
    "jhgan/ko-sroberta-multitask",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", 
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    "sentence-transformers/distiluse-base-multilingual-cased-v2",
    "BM-K/KoSimCSE-roberta-multitask",
    "snunlp/KR-SBERT-V40K-klueNLI-augSTS"
]

# 다양한 테스트 데이터셋
TEST_DATASETS = {
    "데뷔_관련": [
        "BTS의 데뷔 연도는 언제인가요?",
        "BTS가 데뷔한 해는?", 
        "방탄소년단이 언제 시작했나요?",
        "방탄소년단의 첫 활동은?",
        "BTS는 언제부터 활동을 시작했나요?",
        "방탄소년단이 처음 나온 연도는?"
    ],
    
    "멤버_관련": [
        "BTS 멤버는 몇 명인가요?",
        "방탄소년단은 총 몇 명으로 구성되어 있나요?",
        "BTS의 구성원 수는?",
        "방탄소년단 멤버 수는 얼마나 되나요?",
        "BTS는 몇 명의 멤버로 이루어져 있나요?"
    ],
    
    "리더_관련": [
        "BTS의 리더는 누구인가요?",
        "방탄소년단의 리더는?",
        "BTS 팀장은 누구인가요?",
        "방탄소년단을 이끄는 사람은?"
    ],
    
    "음악_관련": [
        "BTS의 대표곡은 무엇인가요?",
        "방탄소년단의 히트곡은?",
        "BTS의 유명한 노래는?",
        "방탄소년단 인기곡을 알려주세요"
    ],
    
    "완전_다른_주제": [
        "오늘 날씨가 어때요?",
        "사과는 빨간색입니다",
        "파이썬 프로그래밍을 배우고 싶어요",
        "서울의 인구는 얼마나 되나요?",
        "축구 경기는 언제 시작하나요?"
    ]
}

def load_model_safely(model_name):
    """모델을 안전하게 로드"""
    try:
        logger.info(f"모델 로딩 중: {model_name}")
        start_time = time.time()
        model = SentenceTransformer(model_name)
        load_time = time.time() - start_time
        logger.info(f"로딩 완료: {load_time:.2f}초")
        return model, load_time
    except Exception as e:
        logger.error(f"모델 로딩 실패 {model_name}: {e}")
        return None, None

def calculate_intra_group_similarity(embeddings):
    """그룹 내 평균 유사도 계산"""
    if len(embeddings) < 2:
        return 0.0
    
    similarities = []
    for i in range(len(embeddings)):
        for j in range(i+1, len(embeddings)):
            sim = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
            similarities.append(sim)
    
    return np.mean(similarities)

def calculate_inter_group_similarity(group1_embeddings, group2_embeddings):
    """그룹 간 평균 유사도 계산"""
    similarities = []
    for emb1 in group1_embeddings:
        for emb2 in group2_embeddings:
            sim = cosine_similarity([emb1], [emb2])[0][0]
            similarities.append(sim)
    
    return np.mean(similarities)

def evaluate_model_performance(model, model_name):
    """모델 성능 평가"""
    logger.info(f"\n=== {model_name} 성능 평가 ===")
    
    results = {
        "model_name": model_name,
        "intra_group_similarities": {},
        "inter_group_similarities": {},
        "encoding_time": 0,
        "dimension": 0
    }
    
    # 모든 문장 임베딩 생성
    all_embeddings = {}
    start_time = time.time()
    
    for group_name, sentences in TEST_DATASETS.items():
        embeddings = []
        for sentence in sentences:
            embedding = model.encode(sentence)
            embeddings.append(embedding)
        all_embeddings[group_name] = embeddings
    
    encoding_time = time.time() - start_time
    results["encoding_time"] = encoding_time
    results["dimension"] = len(all_embeddings[list(TEST_DATASETS.keys())[0]][0])
    
    logger.info(f"임베딩 차원: {results['dimension']}")
    logger.info(f"인코딩 시간: {encoding_time:.2f}초")
    
    # 그룹 내 유사도 계산
    logger.info("\n--- 그룹 내 유사도 (높을수록 좋음) ---")
    for group_name, embeddings in all_embeddings.items():
        if group_name != "완전_다른_주제":  # 완전 다른 주제는 제외
            intra_sim = calculate_intra_group_similarity(embeddings)
            results["intra_group_similarities"][group_name] = intra_sim
            logger.info(f"{group_name}: {intra_sim:.4f}")
    
    # 그룹 간 유사도 계산 (관련 없는 그룹들)
    logger.info("\n--- 그룹 간 유사도 (낮을수록 좋음) ---")
    group_names = [name for name in TEST_DATASETS.keys() if name != "완전_다른_주제"]
    
    for i, group1 in enumerate(group_names):
        for j, group2 in enumerate(group_names):
            if i < j:
                inter_sim = calculate_inter_group_similarity(
                    all_embeddings[group1], 
                    all_embeddings[group2]
                )
                pair_name = f"{group1}_vs_{group2}"
                results["inter_group_similarities"][pair_name] = inter_sim
                logger.info(f"{group1} vs {group2}: {inter_sim:.4f}")
    
    # 완전 다른 주제와의 유사도 (매우 낮아야 함)
    logger.info("\n--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---")
    for group_name in group_names:
        different_sim = calculate_inter_group_similarity(
            all_embeddings[group_name],
            all_embeddings["완전_다른_주제"]
        )
        results["inter_group_similarities"][f"{group_name}_vs_완전다른주제"] = different_sim
        logger.info(f"{group_name} vs 완전다른주제: {different_sim:.4f}")
    
    return results

def calculate_model_score(results):
    """모델 종합 점수 계산"""
    score = 0
    
    # 1. 그룹 내 유사도 (높을수록 좋음) - 가중치 40%
    intra_avg = np.mean(list(results["intra_group_similarities"].values()))
    score += intra_avg * 0.4
    
    # 2. 서로 다른 주제 간 유사도 (낮을수록 좋음) - 가중치 30%
    different_topic_sims = [
        sim for key, sim in results["inter_group_similarities"].items() 
        if "완전다른주제" in key
    ]
    different_avg = np.mean(different_topic_sims)
    score += (1 - different_avg) * 0.3  # 낮을수록 좋으므로 1에서 빼기
    
    # 3. 관련 주제 간 적절한 구분 (너무 높지도 낮지도 않게) - 가중치 20%
    related_sims = [
        sim for key, sim in results["inter_group_similarities"].items() 
        if "완전다른주제" not in key
    ]
    related_avg = np.mean(related_sims)
    # 0.6~0.8 범위가 이상적 (관련있지만 구분되는 수준)
    if 0.6 <= related_avg <= 0.8:
        related_score = 1.0
    else:
        related_score = 1.0 - abs(related_avg - 0.7) / 0.3
    score += related_score * 0.2
    
    # 4. 속도 보너스 (5초 이하면 보너스) - 가중치 10%
    if results["encoding_time"] <= 5.0:
        speed_bonus = 0.1
    else:
        speed_bonus = max(0, 0.1 - (results["encoding_time"] - 5.0) * 0.01)
    score += speed_bonus
    
    return min(score, 1.0)  # 최대 1.0으로 제한

def compare_specific_cases(model, model_name):
    """특정 중복 검사 케이스 테스트"""
    logger.info(f"\n=== {model_name} 중복 검사 케이스 테스트 ===")
    
    # 실제 중복 검사에서 중요한 케이스들
    test_cases = [
        {
            "original": "BTS의 데뷔 연도는 언제인가요?",
            "candidates": [
                "BTS가 데뷔한 해는?",  # 높은 유사도 예상
                "방탄소년단이 언제 시작했나요?",  # 중간 유사도 예상
                "BTS 멤버는 몇 명인가요?",  # 낮은 유사도 예상
                "오늘 날씨가 어때요?"  # 매우 낮은 유사도 예상
            ]
        },
        {
            "original": "방탄소년단의 리더는 누구인가요?",
            "candidates": [
                "BTS의 리더는?",  # 높은 유사도 예상
                "방탄소년단 팀장은 누구인가요?",  # 높은 유사도 예상
                "BTS의 대표곡은 무엇인가요?",  # 낮은 유사도 예상
                "파이썬을 배우고 싶어요"  # 매우 낮은 유사도 예상
            ]
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        logger.info(f"\n--- 케이스 {i}: {case['original']} ---")
        
        original_embedding = model.encode(case['original'])
        
        for candidate in case['candidates']:
            candidate_embedding = model.encode(candidate)
            similarity = cosine_similarity([original_embedding], [candidate_embedding])[0][0]
            
            # 유사도 수준 판단
            if similarity > 0.9:
                level = "매우 높음 🔥"
            elif similarity > 0.8:
                level = "높음 ✅"
            elif similarity > 0.6:
                level = "중간 ⚠️"
            elif similarity > 0.4:
                level = "낮음 ❌"
            else:
                level = "매우 낮음 ⛔"
            
            logger.info(f"  vs '{candidate}': {similarity:.4f} ({level})")

def main():
    """메인 비교 테스트 함수"""
    logger.info("=== 한국어 임베딩 모델 종합 비교 테스트 ===")
    
    all_results = []
    successful_models = []
    
    # 각 모델 테스트
    for model_name in KOREAN_MODELS:
        try:
            model, load_time = load_model_safely(model_name)
            if model is None:
                continue
                
            # 성능 평가
            results = evaluate_model_performance(model, model_name)
            results["load_time"] = load_time
            
            # 종합 점수 계산
            score = calculate_model_score(results)
            results["total_score"] = score
            
            # 특정 케이스 테스트
            compare_specific_cases(model, model_name)
            
            all_results.append(results)
            successful_models.append((model_name, model))
            
            logger.info(f"\n{model_name} 종합 점수: {score:.4f}")
            
        except Exception as e:
            logger.error(f"{model_name} 테스트 실패: {e}")
            continue
    
    # 최종 결과 정리
    logger.info("\n" + "="*80)
    logger.info("🏆 최종 모델 순위")
    logger.info("="*80)
    
    # 점수순으로 정렬
    all_results.sort(key=lambda x: x["total_score"], reverse=True)
    
    for i, result in enumerate(all_results, 1):
        logger.info(f"\n{i}위: {result['model_name']}")
        logger.info(f"   종합 점수: {result['total_score']:.4f}")
        logger.info(f"   로딩 시간: {result['load_time']:.2f}초")
        logger.info(f"   인코딩 시간: {result['encoding_time']:.2f}초")
        logger.info(f"   임베딩 차원: {result['dimension']}")
        
        # 그룹 내 평균 유사도
        intra_avg = np.mean(list(result["intra_group_similarities"].values()))
        logger.info(f"   그룹 내 평균 유사도: {intra_avg:.4f}")
        
        # 완전 다른 주제와의 평균 유사도
        different_sims = [
            sim for key, sim in result["inter_group_similarities"].items() 
            if "완전다른주제" in key
        ]
        different_avg = np.mean(different_sims)
        logger.info(f"   다른 주제와 평균 유사도: {different_avg:.4f}")
    
    # 추천 모델
    if all_results:
        best_model = all_results[0]
        logger.info(f"\n🎯 추천 모델: {best_model['model_name']}")
        logger.info(f"   이유: 종합 점수 {best_model['total_score']:.4f}로 1위")
        
        # 실용성 고려 추천
        practical_models = [r for r in all_results if r['load_time'] < 10 and r['encoding_time'] < 10]
        if practical_models:
            practical_best = practical_models[0]
            logger.info(f"\n⚡ 실용성 고려 추천: {practical_best['model_name']}")
            logger.info(f"   이유: 성능과 속도의 균형이 좋음")
    
    logger.info("\n=== 모델 비교 테스트 완료 ===")
    
    return all_results

if __name__ == "__main__":
    results = main()

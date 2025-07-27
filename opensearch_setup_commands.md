# AWS OpenSearch Serverless 설정 - 실제 실행 명령어

## 🚀 시작하기 전 준비사항 (백지 상태에서)

### 1. AWS 계정 및 IAM 사용자 준비
```bash
# AWS 계정이 없다면 먼저 생성: https://aws.amazon.com/
# IAM 사용자 생성 및 필요한 권한 부여 필요
```

### 2. AWS CLI 설치 및 설정
```bash
# macOS
brew install awscli

# Ubuntu/Debian
sudo apt-get install awscli

# Windows
# https://aws.amazon.com/cli/ 에서 다운로드

# AWS CLI 설정
aws configure
# AWS Access Key ID: [your-access-key]
# AWS Secret Access Key: [your-secret-key]  
# Default region name: us-east-1
# Default output format: json
```

### 3. 필요한 IAM 권한 확인
사용자에게 다음 권한이 필요합니다:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aoss:*",
                "iam:ListUsers",
                "iam:GetUser"
            ],
            "Resource": "*"
        }
    ]
}
```

### 4. 계정 정보 확인
```bash
# 현재 사용자 정보 확인
aws sts get-caller-identity

```

### 5. OpenSearch Serverless 서비스 활성화 확인
```bash
# OpenSearch Serverless가 해당 리전에서 사용 가능한지 확인
aws opensearchserverless list-collections --region us-east-1
```


## 1단계: Network Policy 생성 ✅
```bash
aws opensearchserverless create-security-policy \
  --name "kpop-quiz-network-policy" \
  --type network \
  --policy '[{"Rules":[{"Resource":["collection/kpop-quiz-collection"],"ResourceType":"collection"}],"AllowFromPublic":true}]'
```

**결과:**
- Policy Version: MTc1MzYxOTUxNzAyNF8x
- 생성 시간: 1753619517024

## 2단계: Encryption Policy 생성 ✅
```bash
aws opensearchserverless create-security-policy \
  --name "kpop-quiz-encryption-policy" \
  --type encryption \
  --policy '{"Rules":[{"Resource":["collection/kpop-quiz-collection"],"ResourceType":"collection"}],"AWSOwnedKey":true}'
```

**결과:**
- Policy Version: MTc1MzYxOTUzODA2NV8x
- 생성 시간: 1753619538065

## 3단계: Data Access Policy 생성 ✅
```bash
# ⚠️ 주의: 아래 명령어에서 계정 ID와 사용자명을 본인 것으로 변경하세요!
# 123456789 → 본인 계정 ID
# myuser → 본인 IAM 사용자명

aws opensearchserverless create-access-policy \
  --name "kpop-quiz-access-policy" \
  --type data \
  --policy '[{"Rules":[{"Resource":["collection/kpop-quiz-collection"],"Permission":["aoss:CreateCollectionItems","aoss:DeleteCollectionItems","aoss:UpdateCollectionItems","aoss:DescribeCollectionItems"],"ResourceType":"collection"},{"Resource":["index/kpop-quiz-collection/*"],"Permission":["aoss:CreateIndex","aoss:DeleteIndex","aoss:UpdateIndex","aoss:DescribeIndex","aoss:ReadDocument","aoss:WriteDocument"],"ResourceType":"index"}],"Principal":["arn:aws:iam::123456789:user/myuser"]}]'
```

**⚠️ 본인 환경에 맞게 수정된 명령어 예시:**
```bash
# 예시: 계정 ID가 123456789012이고 사용자명이 myuser인 경우
aws opensearchserverless create-access-policy \
  --name "kpop-quiz-access-policy" \
  --type data \
  --policy '[{"Rules":[{"Resource":["collection/kpop-quiz-collection"],"Permission":["aoss:CreateCollectionItems","aoss:DeleteCollectionItems","aoss:UpdateCollectionItems","aoss:DescribeCollectionItems"],"ResourceType":"collection"},{"Resource":["index/kpop-quiz-collection/*"],"Permission":["aoss:CreateIndex","aoss:DeleteIndex","aoss:UpdateIndex","aoss:DescribeIndex","aoss:ReadDocument","aoss:WriteDocument"],"ResourceType":"index"}],"Principal":["arn:aws:iam::123456789012:user/myuser"]}]'
```


## 4단계: Collection 생성 ✅
```bash
aws opensearchserverless create-collection \
  --name "kpop-quiz-collection" \
  --type SEARCH \
  --description "K-pop Quiz Generator - Duplicate Detection System"
```

**결과:**
- Collection ID: xxxxxx
- ARN: arn:aws:aoss:us-east-1:1234566:collection/xxxxx
- Status: ACTIVE ✅

## 5단계: Collection 정보 확인 ✅
```bash
# Collection 세부 정보 확인
aws opensearchserverless batch-get-collection --names kpop-quiz-collection

```

**⚠️ 중요: 본인의 실제 엔드포인트 확인**
- 위 명령어 실행 후 `collectionEndpoint` 값을 복사하세요
- 예: `https://your-collection-id.us-east-1.aoss.amazonaws.com`
- 이 값에서 `https://`를 제거한 호스트명만 Python 코드에서 사용합니다

**최종 결과:**
- **Collection Endpoint**: https://xxxxx.us-east-1.aoss.amazonaws.com
- **Dashboard Endpoint**: https://xxxxx.us-east-1.aoss.amazonaws.com/_dashboards

## 6단계: 설정 확인 및 검증

### Collection 상태 확인
```bash
# Collection 상태 모니터링
aws opensearchserverless list-collections --collection-filters name=kpop-quiz-collection

# 특정 Collection 상세 정보 확인
aws opensearchserverless batch-get-collection --names kpop-quiz-collection
```

### 생성된 Policy들 확인
```bash
# Network Policy 확인
aws opensearchserverless list-security-policies --type network

# Encryption Policy 확인  
aws opensearchserverless list-security-policies --type encryption

# Data Access Policy 확인
aws opensearchserverless list-access-policies --type data

# 특정 Policy 상세 정보 확인
aws opensearchserverless get-security-policy --name kpop-quiz-network-policy --type network
aws opensearchserverless get-security-policy --name kpop-quiz-encryption-policy --type encryption
aws opensearchserverless get-access-policy --name kpop-quiz-access-policy --type data
```

## 7단계: 연결 테스트 및 검증

### 기본 연결 테스트
```bash
# opensearch_config.py 파일이 있는 디렉토리에서 실행
python3 -c "
from opensearch_config import get_opensearch_client
client = get_opensearch_client()
if client:
    print('✅ OpenSearch 연결 성공')
    # 클러스터 상태 확인
    try:
        health = client.cluster.health()
        print(f'클러스터 상태: {health[\"status\"]}')
    except Exception as e:
        print(f'클러스터 상태 확인 실패: {e}')
else:
    print('❌ OpenSearch 연결 실패')
"
```

### 인덱스 생성 테스트
```bash
python3 -c "
from opensearch_config import save_quiz_to_opensearch

# 테스트 퀴즈 데이터
test_quiz = {
    'QuizID': 1,
    'Category': 'Test',
    'QuestionID': 1,
    'Type': 'multiple_choice',
    'Question': '테스트 질문입니다.',
    'Options': ['옵션1', '옵션2', '옵션3', '옵션4'],
    'IsCorrect': '옵션1'
}

success, doc_id, error = save_quiz_to_opensearch(test_quiz)
if success:
    print(f'✅ 테스트 퀴즈 저장 성공: {doc_id}')
else:
    print(f'❌ 테스트 퀴즈 저장 실패: {error}')
"
```

## 8단계: OpenSearch 설정값 정리

```python
# OpenSearch Serverless 설정
OPENSEARCH_ENDPOINT = "xxxxxx.us-east-1.aoss.amazonaws.com"  # https:// 제외
OPENSEARCH_REGION = "us-east-1"
OPENSEARCH_COLLECTION_NAME = "kpop-quiz-collection"
OPENSEARCH_INDEX_NAME = "kpop-quiz-vector-index"  # 실제 사용 중인 인덱스명
```

## 실제 운영 정보 (2025-07-27 기준)
- **실제 Endpoint**: xxxxxxx.us-east-1.aoss.amazonaws.com
- **실제 Index**: kpop-quiz-vector-index
- **저장된 문서 수**: 15개
- **벡터 차원**: 768
- **벡터 엔진**: nmslib (L2 거리로 빠른 검색, 코사인 유사도로 정확한 판단)
1. ✅ Collection 생성 완료
2. ✅ Python 코드에서 OpenSearch 클라이언트 설정 완료
3. ✅ 인덱스 생성 및 매핑 설정 완료
4. ✅ 중복 검사 로직 구현 완료
5. ✅ 퀴즈 저장 시스템 구현 완료

## 인덱스 매핑 정보 (실제 운영 중)
```json
{
  "category": {"type": "text"},
  "correct_answer": {"type": "text"},
  "created_at": {"type": "date"},
  "embedding": {
    "type": "knn_vector",
    "dimension": 768,
    "method": {
      "engine": "nmslib",
      "space_type": "l2",
      "name": "hnsw",
      "parameters": {
        "ef_construction": 128,
        "m": 24
      }
    }
  },
  "model_used": {"type": "keyword"},
  "options": {"type": "text"},
  "question": {"type": "text"},
  "question_id": {"type": "integer"},
  "quiz_id": {"type": "keyword"},
  "quiz_type": {"type": "keyword"},
  "topic": {"type": "text"},
  "type": {
    "type": "text",
    "fields": {
      "keyword": {
        "type": "keyword",
        "ignore_above": 256
      }
    }
  }
}
```

## 정리 명령어 (필요시)
```bash
# Collection 삭제
aws opensearchserverless delete-collection --id xxxxxx

# Access Policy 삭제
aws opensearchserverless delete-access-policy --name kpop-quiz-access-policy --type data

# Security Policy 삭제
aws opensearchserverless delete-security-policy --name kpop-quiz-encryption-policy --type encryption
aws opensearchserverless delete-security-policy --name kpop-quiz-network-policy --type network
```

## 주요 정보 요약
- **Collection Name**: kpop-quiz-collection
- **Collection ID**: xxxxx
- **설정 Endpoint**: https://xxxxx.us-east-1.aoss.amazonaws.com
- **실제 운영 Endpoint**: xxxxxx.us-east-1.aoss.amazonaws.com
- **Region**: us-east-1
- **Status**: ACTIVE ✅
- **실제 Index**: kpop-quiz-vector-index
- **중복 검사 임계값**: 0.65 (코사인 유사도)

## 추가 설정 정보
## 추가 설정 정보

### Python 환경 설정 (백지 상태에서)
```bash
# 1. Python 3.8+ 설치 확인
python3 --version

# 2. 가상환경 생성 (권장)
python3 -m venv myenv
source myenv/bin/activate  # macOS/Linux
# myenv\Scripts\activate   # Windows

# 3. 필요한 패키지 설치
pip install boto3 opensearch-py sentence-transformers requests-aws4auth scikit-learn

# 4. 추가 의존성 (LangGraph 퀴즈 생성기용)
pip install langgraph langchain langchain-aws ddgs
```

### opensearch_config.py 파일 생성
프로젝트 디렉토리에 다음 파일을 생성하세요:

**1. config.py 파일 생성:**
```bash
# config.example.py를 복사하여 config.py 생성
cp config.example.py config.py

# config.py 파일을 열어서 본인의 실제 엔드포인트로 변경
```

**2. config.py 내용 (본인 환경에 맞게 수정):**
```python
# config.py
# OpenSearch 설정 (본인의 실제 값으로 변경하세요)
OPENSEARCH_ENDPOINT = "your-collection-id.us-east-1.aoss.amazonaws.com"
OPENSEARCH_INDEX_NAME = "kpop-quiz-vector-index"
OPENSEARCH_REGION = "us-east-1"

# 한국어 임베딩 모델 설정
KOREAN_MODEL_NAME = "jhgan/ko-sroberta-multitask"

# 중복 검사 설정
DEFAULT_DUPLICATION_THRESHOLD = 0.65
```

**3. opensearch_config.py는 이미 구현되어 있음:**
- config.py에서 설정값들을 import
- OpenSearch 클라이언트 및 중복 검사 함수들 포함

### 필요한 Python 패키지
```bash
pip install boto3 opensearch-py sentence-transformers requests-aws4auth
```

### AWS 자격 증명 설정
```bash
# AWS CLI 설정
aws configure

# 또는 환경 변수 설정
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### 중복 검사 시스템 특징
- **임베딩 모델**: jhgan/ko-sroberta-multitask (한국어 특화)
- **벡터 차원**: 768
- **검색 방식**: KNN (k-nearest neighbors)
- **벡터 엔진**: nmslib (L2 거리 기반 빠른 검색)
- **유사도 계산**: 코사인 유사도 (Python에서 재계산)
- **중복 임계값**: 0.65 (코사인 유사도 기준)

## 트러블슈팅

## 트러블슈팅

### 0. 백지 상태에서 자주 발생하는 문제들

#### AWS CLI 설정 문제
```bash
# 오류: "Unable to locate credentials"
# 해결: AWS CLI 재설정
aws configure

# 오류: "An error occurred (UnauthorizedOperation)"
# 해결: IAM 권한 확인
aws sts get-caller-identity
```

#### Python 패키지 설치 문제
```bash
# 오류: "No module named 'boto3'"
# 해결: 가상환경 활성화 후 패키지 설치
source myenv/bin/activate
pip install boto3 opensearch-py sentence-transformers requests-aws4auth

# 오류: "externally-managed-environment"
# 해결: 가상환경 사용
python3 -m venv myenv
source myenv/bin/activate
```

#### Collection 생성 실패
```bash
# 오류: "User is not authorized to perform: aoss:CreateCollection"
# 해결: IAM 정책에 OpenSearch Serverless 권한 추가

# 오류: "Collection name already exists"
# 해결: 다른 이름 사용하거나 기존 Collection 삭제
aws opensearchserverless list-collections
```

### 1. 연결 오류 해결
```bash
# OpenSearch 클라이언트 연결 테스트
python3 -c "
from opensearch_config import get_opensearch_client
client = get_opensearch_client()
if client:
    print('✅ OpenSearch 연결 성공')
else:
    print('❌ OpenSearch 연결 실패')
"
```

### 2. 인덱스 스키마 불일치 해결
- 기존 인덱스와 새 코드의 스키마가 다를 경우
- `question_id`는 integer 타입으로 저장
- `quiz_id`는 keyword 타입이지만 숫자 값 사용

### 3. 권한 문제 해결
```bash
# IAM 사용자 권한 확인
aws sts get-caller-identity

# OpenSearch Serverless 권한 확인
aws opensearchserverless list-access-policies --type data
```

### 4. 인덱스 상태 확인
```bash
# Python에서 인덱스 정보 확인
python3 -c "
from opensearch_config import get_opensearch_stats
stats = get_opensearch_stats()
if stats:
    print(f'문서 수: {stats[\"document_count\"]}')
    print(f'인덱스: {stats[\"index_name\"]}')
else:
    print('통계 조회 실패')
"
```

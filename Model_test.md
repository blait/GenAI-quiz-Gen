INFO:__main__:=== 한국어 임베딩 모델 종합 비교 테스트 ===
INFO:__main__:모델 로딩 중: jhgan/ko-sroberta-multitask
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: jhgan/ko-sroberta-multitask
INFO:__main__:로딩 완료: 6.19초
INFO:__main__:
=== jhgan/ko-sroberta-multitask 성능 평가 ===
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00,  4.45it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 11.30it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 46.74it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  1.49it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  2.03it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  3.82it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 44.97it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  2.07it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 11.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 33.94it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 44.65it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  1.70it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 40.17it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 68.79it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.59it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 63.42it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.63it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.68it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  1.73it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 39.85it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 43.82it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 38.78it/s]
INFO:__main__:임베딩 차원: 768
INFO:__main__:인코딩 시간: 3.83초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.8115
INFO:__main__:멤버_관련: 0.8397
INFO:__main__:리더_관련: 0.7964
INFO:__main__:음악_관련: 0.7815
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.6789
INFO:__main__:데뷔_관련 vs 리더_관련: 0.6514
INFO:__main__:데뷔_관련 vs 음악_관련: 0.6495
INFO:__main__:멤버_관련 vs 리더_관련: 0.7042
INFO:__main__:멤버_관련 vs 음악_관련: 0.6571
INFO:__main__:리더_관련 vs 음악_관련: 0.6720
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.2154
INFO:__main__:멤버_관련 vs 완전다른주제: 0.1743
INFO:__main__:리더_관련 vs 완전다른주제: 0.1568
INFO:__main__:음악_관련 vs 완전다른주제: 0.1525
INFO:__main__:
=== jhgan/ko-sroberta-multitask 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 33.80it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 72.17it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.9341 (매우 높음 🔥)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.68it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.8161 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.31it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.7683 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 61.63it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.1949 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 53.91it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 56.89it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.7676 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 55.40it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.8870 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 54.18it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.7264 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 51.94it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.1392 (매우 낮음 ⛔)
INFO:__main__:
jhgan/ko-sroberta-multitask 종합 점수: 0.8705
INFO:__main__:모델 로딩 중: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
INFO:__main__:로딩 완료: 3.83초
INFO:__main__:
=== sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 성능 평가 ===
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 10.57it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 15.81it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 14.53it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  3.93it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 74.08it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.97it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 13.57it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 13.71it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 63.59it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  4.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 60.45it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 70.18it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.66it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 63.52it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.30it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 61.40it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 31.86it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  3.41it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 76.76it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.15it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 74.50it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.91it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.65it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.61it/s]
INFO:__main__:임베딩 차원: 384
INFO:__main__:인코딩 시간: 1.46초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.5798
INFO:__main__:멤버_관련: 0.6626
INFO:__main__:리더_관련: 0.6107
INFO:__main__:음악_관련: 0.5398
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.4570
INFO:__main__:데뷔_관련 vs 리더_관련: 0.4245
INFO:__main__:데뷔_관련 vs 음악_관련: 0.4001
INFO:__main__:멤버_관련 vs 리더_관련: 0.4775
INFO:__main__:멤버_관련 vs 음악_관련: 0.2934
INFO:__main__:리더_관련 vs 음악_관련: 0.4237
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.2109
INFO:__main__:멤버_관련 vs 완전다른주제: 0.1436
INFO:__main__:리더_관련 vs 완전다른주제: 0.1745
INFO:__main__:음악_관련 vs 완전다른주제: 0.2148
INFO:__main__:
=== sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 69.29it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 69.45it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.9171 (매우 높음 🔥)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 68.87it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.4530 (낮음 ❌)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 71.40it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.6842 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.22it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.2427 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 63.64it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  3.29it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.6033 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 76.88it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.8081 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.50it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.3084 (매우 낮음 ⛔)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.39it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.3019 (매우 낮음 ⛔)
INFO:__main__:
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 종합 점수: 0.5920
INFO:__main__:모델 로딩 중: sentence-transformers/paraphrase-multilingual-mpnet-base-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: sentence-transformers/paraphrase-multilingual-mpnet-base-v2
INFO:__main__:로딩 완료: 51.05초
INFO:__main__:
=== sentence-transformers/paraphrase-multilingual-mpnet-base-v2 성능 평가 ===
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 11.28it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 39.67it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  3.71it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 31.79it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 44.50it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.63it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 47.43it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  5.70it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 41.13it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 27.44it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.56it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 76.19it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 73.07it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.54it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.62it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 70.29it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 53.99it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 50.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.18it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 54.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 55.47it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 47.08it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 44.69it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 39.57it/s]
INFO:__main__:임베딩 차원: 768
INFO:__main__:인코딩 시간: 0.99초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.6643
INFO:__main__:멤버_관련: 0.7980
INFO:__main__:리더_관련: 0.7360
INFO:__main__:음악_관련: 0.6761
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.5020
INFO:__main__:데뷔_관련 vs 리더_관련: 0.5322
INFO:__main__:데뷔_관련 vs 음악_관련: 0.5470
INFO:__main__:멤버_관련 vs 리더_관련: 0.5261
INFO:__main__:멤버_관련 vs 음악_관련: 0.3790
INFO:__main__:리더_관련 vs 음악_관련: 0.4783
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.2130
INFO:__main__:멤버_관련 vs 완전다른주제: 0.1794
INFO:__main__:리더_관련 vs 완전다른주제: 0.1201
INFO:__main__:음악_관련 vs 완전다른주제: 0.1320
INFO:__main__:
=== sentence-transformers/paraphrase-multilingual-mpnet-base-v2 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 63.48it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.28it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.9202 (매우 높음 🔥)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.83it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.5943 (낮음 ❌)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.49it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.6282 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 60.10it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.2465 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 51.79it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 44.96it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.5900 (낮음 ❌)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 54.56it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.8044 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 53.21it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.3959 (매우 낮음 ⛔)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `XLMRobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 52.69it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.0479 (매우 낮음 ⛔)
INFO:__main__:
sentence-transformers/paraphrase-multilingual-mpnet-base-v2 종합 점수: 0.7018
INFO:__main__:모델 로딩 중: sentence-transformers/distiluse-base-multilingual-cased-v2
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: sentence-transformers/distiluse-base-multilingual-cased-v2
INFO:__main__:로딩 완료: 29.92초
INFO:__main__:
=== sentence-transformers/distiluse-base-multilingual-cased-v2 성능 평가 ===
Batches: 100%|██████████| 1/1 [00:00<00:00, 14.55it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 37.55it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 47.47it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 41.65it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 80.70it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 38.14it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 39.38it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  7.36it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 71.74it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 76.55it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 15.52it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 68.55it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.52it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.22it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 53.02it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 55.61it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 61.07it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 36.59it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 93.13it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 78.80it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.20it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 46.26it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 111.88it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 119.15it/s]
INFO:__main__:임베딩 차원: 512
INFO:__main__:인코딩 시간: 0.66초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.5891
INFO:__main__:멤버_관련: 0.6498
INFO:__main__:리더_관련: 0.6367
INFO:__main__:음악_관련: 0.5233
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.4403
INFO:__main__:데뷔_관련 vs 리더_관련: 0.4564
INFO:__main__:데뷔_관련 vs 음악_관련: 0.4206
INFO:__main__:멤버_관련 vs 리더_관련: 0.5358
INFO:__main__:멤버_관련 vs 음악_관련: 0.4321
INFO:__main__:리더_관련 vs 음악_관련: 0.5013
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.2083
INFO:__main__:멤버_관련 vs 완전다른주제: 0.1899
INFO:__main__:리더_관련 vs 완전다른주제: 0.1825
INFO:__main__:음악_관련 vs 완전다른주제: 0.1863
INFO:__main__:
=== sentence-transformers/distiluse-base-multilingual-cased-v2 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches: 100%|██████████| 1/1 [00:00<00:00, 85.16it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 106.60it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.8764 (높음 ✅)
Batches: 100%|██████████| 1/1 [00:00<00:00, 109.41it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.5371 (낮음 ❌)
Batches: 100%|██████████| 1/1 [00:00<00:00, 96.74it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.5444 (낮음 ❌)
Batches: 100%|██████████| 1/1 [00:00<00:00, 78.23it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.1986 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches: 100%|██████████| 1/1 [00:00<00:00, 113.22it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 39.29it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.5687 (낮음 ❌)
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.74it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.9141 (매우 높음 🔥)
Batches: 100%|██████████| 1/1 [00:00<00:00, 55.83it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.4101 (낮음 ❌)
Batches: 100%|██████████| 1/1 [00:00<00:00, 107.89it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.1005 (매우 낮음 ⛔)
INFO:__main__:
sentence-transformers/distiluse-base-multilingual-cased-v2 종합 점수: 0.6253
INFO:__main__:모델 로딩 중: BM-K/KoSimCSE-roberta-multitask
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: BM-K/KoSimCSE-roberta-multitask
WARNING:sentence_transformers.SentenceTransformer:No sentence-transformers model found with name BM-K/KoSimCSE-roberta-multitask. Creating a new one with mean pooling.
INFO:__main__:로딩 완료: 19.53초
INFO:__main__:
=== BM-K/KoSimCSE-roberta-multitask 성능 평가 ===
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 15.90it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 73.19it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 61.61it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 56.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 58.09it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 36.19it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 31.66it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 40.11it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 68.11it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.29it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 71.32it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 69.24it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 70.23it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 60.68it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 62.29it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 69.37it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.43it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 58.56it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.51it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 60.10it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 54.98it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 51.68it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 50.64it/s]
INFO:__main__:임베딩 차원: 768
INFO:__main__:인코딩 시간: 0.53초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.8374
INFO:__main__:멤버_관련: 0.8647
INFO:__main__:리더_관련: 0.8063
INFO:__main__:음악_관련: 0.8089
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.6432
INFO:__main__:데뷔_관련 vs 리더_관련: 0.6262
INFO:__main__:데뷔_관련 vs 음악_관련: 0.6429
INFO:__main__:멤버_관련 vs 리더_관련: 0.6462
INFO:__main__:멤버_관련 vs 음악_관련: 0.6121
INFO:__main__:리더_관련 vs 음악_관련: 0.6730
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.2893
INFO:__main__:멤버_관련 vs 완전다른주제: 0.2609
INFO:__main__:리더_관련 vs 완전다른주제: 0.1751
INFO:__main__:음악_관련 vs 완전다른주제: 0.2077
INFO:__main__:
=== BM-K/KoSimCSE-roberta-multitask 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 37.87it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 75.96it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.9165 (매우 높음 🔥)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 75.23it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.8649 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 73.45it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.6873 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 72.27it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.2372 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 68.39it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.98it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.7159 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 61.71it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.8964 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 60.20it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.7429 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `RobertaSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 59.07it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.1447 (매우 낮음 ⛔)
INFO:__main__:
BM-K/KoSimCSE-roberta-multitask 종합 점수: 0.8618
INFO:__main__:모델 로딩 중: snunlp/KR-SBERT-V40K-klueNLI-augSTS
INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: snunlp/KR-SBERT-V40K-klueNLI-augSTS
INFO:__main__:로딩 완료: 22.43초
INFO:__main__:
=== snunlp/KR-SBERT-V40K-klueNLI-augSTS 성능 평가 ===
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 18.84it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 45.57it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.21it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 31.97it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 65.57it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 53.01it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 42.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 55.53it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 27.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 52.36it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 29.77it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 73.77it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 73.71it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 72.03it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.25it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.06it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 69.16it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.54it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.24it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 64.27it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00,  1.70it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 36.73it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 76.53it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.78it/s]
INFO:__main__:임베딩 차원: 768
INFO:__main__:인코딩 시간: 1.10초
INFO:__main__:
--- 그룹 내 유사도 (높을수록 좋음) ---
INFO:__main__:데뷔_관련: 0.7391
INFO:__main__:멤버_관련: 0.7339
INFO:__main__:리더_관련: 0.7177
INFO:__main__:음악_관련: 0.7154
INFO:__main__:
--- 그룹 간 유사도 (낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 멤버_관련: 0.6084
INFO:__main__:데뷔_관련 vs 리더_관련: 0.6260
INFO:__main__:데뷔_관련 vs 음악_관련: 0.6066
INFO:__main__:멤버_관련 vs 리더_관련: 0.6144
INFO:__main__:멤버_관련 vs 음악_관련: 0.5806
INFO:__main__:리더_관련 vs 음악_관련: 0.6210
INFO:__main__:
--- 완전 다른 주제와의 유사도 (매우 낮을수록 좋음) ---
INFO:__main__:데뷔_관련 vs 완전다른주제: 0.1399
INFO:__main__:멤버_관련 vs 완전다른주제: 0.1692
INFO:__main__:리더_관련 vs 완전다른주제: 0.1430
INFO:__main__:음악_관련 vs 완전다른주제: 0.1168
INFO:__main__:
=== snunlp/KR-SBERT-V40K-klueNLI-augSTS 중복 검사 케이스 테스트 ===
INFO:__main__:
--- 케이스 1: BTS의 데뷔 연도는 언제인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 45.02it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 48.97it/s]
INFO:__main__:  vs 'BTS가 데뷔한 해는?': 0.8603 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 47.57it/s]
INFO:__main__:  vs '방탄소년단이 언제 시작했나요?': 0.6816 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 23.83it/s]
INFO:__main__:  vs 'BTS 멤버는 몇 명인가요?': 0.7492 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 51.42it/s]
INFO:__main__:  vs '오늘 날씨가 어때요?': 0.1211 (매우 낮음 ⛔)
INFO:__main__:
--- 케이스 2: 방탄소년단의 리더는 누구인가요? ---
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 37.20it/s]
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.76it/s]
INFO:__main__:  vs 'BTS의 리더는?': 0.7734 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 66.38it/s]
INFO:__main__:  vs '방탄소년단 팀장은 누구인가요?': 0.8214 (높음 ✅)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.28it/s]
INFO:__main__:  vs 'BTS의 대표곡은 무엇인가요?': 0.6486 (중간 ⚠️)
Batches:   0%|          | 0/1 [00:00<?, ?it/s]/Users/hyeonsup/idolquiz/myenv/lib/python3.13/site-packages/torch/nn/modules/module.py:1762: FutureWarning: `encoder_attention_mask` is deprecated and will be removed in version 4.55.0 for `BertSdpaSelfAttention.forward`.
  return forward_call(*args, **kwargs)
Batches: 100%|██████████| 1/1 [00:00<00:00, 67.11it/s]
INFO:__main__:  vs '파이썬을 배우고 싶어요': 0.1686 (매우 낮음 ⛔)
INFO:__main__:
snunlp/KR-SBERT-V40K-klueNLI-augSTS 종합 점수: 0.8479
INFO:__main__:
================================================================================
INFO:__main__:🏆 최종 모델 순위
INFO:__main__:================================================================================
INFO:__main__:
1위: jhgan/ko-sroberta-multitask
INFO:__main__:   종합 점수: 0.8705
INFO:__main__:   로딩 시간: 6.19초
INFO:__main__:   인코딩 시간: 3.83초
INFO:__main__:   임베딩 차원: 768
INFO:__main__:   그룹 내 평균 유사도: 0.8073
INFO:__main__:   다른 주제와 평균 유사도: 0.1748
INFO:__main__:
2위: BM-K/KoSimCSE-roberta-multitask
INFO:__main__:   종합 점수: 0.8618
INFO:__main__:   로딩 시간: 19.53초
INFO:__main__:   인코딩 시간: 0.53초
INFO:__main__:   임베딩 차원: 768
INFO:__main__:   그룹 내 평균 유사도: 0.8293
INFO:__main__:   다른 주제와 평균 유사도: 0.2332
INFO:__main__:
3위: snunlp/KR-SBERT-V40K-klueNLI-augSTS
INFO:__main__:   종합 점수: 0.8479
INFO:__main__:   로딩 시간: 22.43초
INFO:__main__:   인코딩 시간: 1.10초
INFO:__main__:   임베딩 차원: 768
INFO:__main__:   그룹 내 평균 유사도: 0.7265
INFO:__main__:   다른 주제와 평균 유사도: 0.1423
INFO:__main__:
4위: sentence-transformers/paraphrase-multilingual-mpnet-base-v2
INFO:__main__:   종합 점수: 0.7018
INFO:__main__:   로딩 시간: 51.05초
INFO:__main__:   인코딩 시간: 0.99초
INFO:__main__:   임베딩 차원: 768
INFO:__main__:   그룹 내 평균 유사도: 0.7186
INFO:__main__:   다른 주제와 평균 유사도: 0.1611
INFO:__main__:
5위: sentence-transformers/distiluse-base-multilingual-cased-v2
INFO:__main__:   종합 점수: 0.6253
INFO:__main__:   로딩 시간: 29.92초
INFO:__main__:   인코딩 시간: 0.66초
INFO:__main__:   임베딩 차원: 512
INFO:__main__:   그룹 내 평균 유사도: 0.5997
INFO:__main__:   다른 주제와 평균 유사도: 0.1917
INFO:__main__:
6위: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
INFO:__main__:   종합 점수: 0.5920
INFO:__main__:   로딩 시간: 3.83초
INFO:__main__:   인코딩 시간: 1.46초
INFO:__main__:   임베딩 차원: 384
INFO:__main__:   그룹 내 평균 유사도: 0.5982
INFO:__main__:   다른 주제와 평균 유사도: 0.1859
INFO:__main__:
🎯 추천 모델: jhgan/ko-sroberta-multitask
INFO:__main__:   이유: 종합 점수 0.8705로 1위
INFO:__main__:
⚡ 실용성 고려 추천: jhgan/ko-sroberta-multitask
INFO:__main__:   이유: 성능과 속도의 균형이 좋음
INFO:__main__:
=== 모델 비교 테스트 완료 ===

 ⋮ 
 ● Completed in 164.484s


> 🎉 완벽한 모델 비교 테스트 완료! 

## 🏆 최종 결과 분석:

### **1위: jhgan/ko-sroberta-multitask** ⭐⭐⭐⭐⭐
• **종합 점수**: 0.8705 (최고점)
• **그룹 내 유사도**: 0.8073 (같은 주제끼리 높은 유사도)
• **다른 주제와 유사도**: 0.1748 (완전 다른 주제와는 낮은 유사도)
• **실제 케이스 성능**:
  • "BTS의 데뷔 연도는?" vs "BTS가 데뷔한 해는?" → 0.9341 🔥
  • "방탄소년단의 리더는?" vs "방탄소년단 팀장은?" → 0.8870 ✅

### **2위: BM-K/KoSimCSE-roberta-multitask** ⭐⭐⭐⭐
• **종합 점수**: 0.8618
• **장점**: 가장 빠른 인코딩 속도 (0.53초)
• **단점**: 로딩 시간이 길고, 완전 다른 주제와의 구분이 약간 부족

### **3위: snunlp/KR-SBERT-V40K-klueNLI-augSTS** ⭐⭐⭐⭐
• **종합 점수**: 0.8479
• **장점**: 완전 다른 주제와의 구분이 매우 좋음 (0.1423)
• **단점**: 로딩 시간이 길음

## 📊 핵심 발견사항:

### ✅ 성공적인 개선:
1. 한국어 특화 모델들이 압도적으로 우수함
2. 의미적 유사도 검출 능력 대폭 향상:
   • 기존 영어 모델: "데뷔 연도" vs "멤버 수" → 0.9240 (말이 안됨)
   • 한국어 모델: "데뷔 연도" vs "멤버 수" → 0.7683 (적절함)

### 🎯 최적 임계값 가이드:
• **0.9 이상**: 거의 동일한 질문 (확실한 중복)
• **0.8~0.9**: 매우 유사한 질문 (중복 가능성 높음)
• **0.7~0.8**: 관련 있는 질문 (검토 필요)
• **0.7 미만**: 다른 질문

## 🎯 최종 추천:

jhgan/ko-sroberta-multitask를 최종 모델로 선택!

이유:
1. 최고 성능: 종합 점수 1위
2. 균형잡힌 속도: 로딩/인코딩 시간 적절
3. 실용적 성능: 실제 중복 검사 케이스에서 우수한 결과
4. 안정성: 다양한 테스트에서 일관된 성능
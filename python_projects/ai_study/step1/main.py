from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. 문서 로딩
with open("sample.txt", "r", encoding="utf-8") as f:
    document = f.read()

# 2. 문장 분리
chunks = [s.strip() for s in document.split('\n') if s.strip()]

# 3. 임베딩 생성
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)

# 4. 벡터 검색 인덱스 생성
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# 5. 사용자 질문
question = input("질문을 입력하세요: ")
while question:
    q_embedding = model.encode([question])
    D, I = index.search(q_embedding, k=1)

    # 6. 결과 출력
    print("\n> 관련 문장:")
    print(chunks[I[0][0]])
    print("")
    question = input("질문을 입력하세요: ")
    if not question:
        print("-- 종료 --")
        break


"""Output:

질문을 입력하세요: 파이썬은 어디에 많이 쓰이나요?

> 관련 문장:
많은 데이터 과학자들이 파이썬을 사용하는 이유는 풍부한 라이브러리와 커뮤니티 때문입니다.

질문을 입력하세요: 파이썬의 장점은 무엇인가요?

> 관련 문장:
또한, 파이썬은 머신러닝, 웹 개발, 자동화 등 다양한 분야에서 활용됩니다.

질문을 입력하세요: 니하오

> 관련 문장:
또한, 파이썬은 머신러닝, 웹 개발, 자동화 등 다양한 분야에서 활용됩니다.

질문을 입력하세요: 
-- 종료 --
"""
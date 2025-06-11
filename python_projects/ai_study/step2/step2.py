from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. 문서 내용
with open("sample.txt", "r", encoding="utf-8") as f:
    document = f.read()

chunks = [s.strip() for s in document.split('\n') if s.strip()]

# 2. 문장 임베딩
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# 3. 사용자 질문
# question = input("질문: ")
question = "파이썬이 느려도 사람들이 많이 쓰는 이유는?"
print(f"질문: {question}")
q_vec = model.encode([question])
_, I = index.search(q_vec, k=1)
retrieved = chunks[I[0][0]]

# 4. 로컬 LLM에 질의 (프롬프트 구성)
## 기본 prompt
b_prompt = f"""[문서 내용]
{retrieved}

[질문]
{question}

[답변]
"""

## prompt 개선 실습용
i_prompt = f"""너는 문서 기반 정보를 사용자에게 설명하는 AI야.  
아래 문서를 참고해서 질문에 대해 부드럽고 정확하게 대답해줘.  
답변은 반드시 문서 내용을 기반으로 해야 하고, 없는 정보는 추측하지 마.  
답변은 2~3문장 이내로 간결하게 작성해줘. 
문장과 문장 사이는 다른 줄로 작성해줘.

[문서 내용]
{retrieved}

[질문]
{question}

[답변]
"""

# 5. LLM 호출
llm = Llama(
    model_path="C:\\llama\\models\\mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,          # 시스템에 맞게 조절
    n_gpu_layers=35,       # VRAM 여유 있으면 늘리기
    verbose=False
)

response = llm(b_prompt, max_tokens=256, stop=["</s>"])
print("\n> Basic Prompt LLM 응답:")
print(response["choices"][0]["text"].strip())
response = llm(i_prompt, max_tokens=256, stop=["</s>"])
print("\n> Improve Prompt LLM 응답:")
print(response["choices"][0]["text"].strip())

# 문서 내용 추가.
plus_doc = "그리고 파이썬은 느린 속도에도 불구하고 높은 생산성과 가독성 덕분에 선호됩니다."
print(f"\n ===== 문서 내용 추가 ==== \n'{plus_doc}'\n")
document += f"\n{plus_doc}"

response = llm(b_prompt, max_tokens=256, stop=["</s>"])
print("\n> Basic Prompt 응답:")
print(response["choices"][0]["text"].strip())
response = llm(i_prompt, max_tokens=256, stop=["</s>"])
print("\n> Improve Prompt 응답:")
print(response["choices"][0]["text"].strip())


"""Output
질문: 파이썬이 느려도 사람들이 많이 쓰는 이유는?
llama_context: n_ctx_per_seq (2048) < n_ctx_train (32768) -- the full capacity of the model will not be utilized

> Basic Prompt LLM 응답:
파이썬이 많이 사용되는 이유는 다음과 같습니다.

1. 다양한 라이브러리 제공:
파이썬은 풍부한 라이브러리를 제공합니다. 이러한 라이브러리들은 데이터 처리, 데이터 시각화, 통합 기술 및 높이 학습 등에 대한 힘을 돕습니다.
2. 유연한 문법:
파이썬의 문법은 널리 인 프로그램 문제 해결을 위한 적합하고 유연한 문법입니다.
3. 간결한 코드 작성:
파이썬의 문법은 간결하고 직관적으로 작성할 수 있습니다. 이러한 코드

> Improve Prompt LLM 응답:
파이썬의 강력한 라이브러리와 커뮤니터리로 인해 많은 데이터 과학자들이 사용합니다. 그리고 이러한 협업 및 문제 해결을 위한 강력한 커뮤니티가 있습니다.

 ===== 문서 내용 추가 ==== 
'그리고 파이썬은 느린 속도에도 불구하고 높은 생산성과 가독성 덕분에 선호됩니다.'


> Basic Prompt 응답:
파이썬이 많이 사용되는 이유는 다양한 라이브러리와 튜토리얼이 많이 있고 코드가 간결하고 가독성이 좋고 높은 성능을 낼 수 있습니다. 또한 파이썬은 데이터 과학과 기술 관련 분야에서 넘치는 유용성이 있습니다.

> Improve Prompt 응답:
파이썬은 많은 라이브러리와 커뮤니터리가 있어 데이터 과학자들이 자주 사용합니다.
"""
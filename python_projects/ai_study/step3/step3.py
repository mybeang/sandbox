# 코드 실행 환경 초기화됨 → 재실행
from llama_cpp import Llama
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. 웹 페이지 가져오기 및 정리
def fetch_and_clean_text(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # 스크립트, 스타일 제거
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.split("\n") if len(line.strip()) > 50]
    return lines

# 2. 임베딩 및 인덱싱
def build_faiss_index(text_chunks, embed_model):
    embeddings = embed_model.encode(text_chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

# 3. 질의 → 관련 문장 검색
def retrieve_relevant_text(question, text_chunks, embed_model, index, top_k=1):
    q_vec = embed_model.encode([question])
    _, I = index.search(q_vec, k=top_k)
    return [text_chunks[i] for i in I[0]]

# 테스트용 URL
url = "https://ko.wikipedia.org/wiki/파이썬"

# 실행
chunks = fetch_and_clean_text(url)
model = SentenceTransformer("all-MiniLM-L6-v2")
index, _ = build_faiss_index(chunks, model)

llm = Llama(
    model_path="C:\\llama\\models\\mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,          # 시스템에 맞게 조절
    n_gpu_layers=35,       # VRAM 여유 있으면 늘리기
    verbose=False
)

prompt = """너는 웹 페이지 내용을 요약하여 답변하는 AI야.
다음은 웹 페이지에서 가져온 관련 내용이야. 이걸 바탕으로 질문에 간결하게 답변해줘.
없는 내용은 추측하지 말고 "정보가 없습니다"라고 말해줘.

[웹 문서 내용]
{}

[질문]
{}

[답변]
"""

questions = ["파이썬이 어디에 쓰이나요?", "파이썬의 장점은 무엇인가요?", "파이썬은 뱀인가요?",
             "파이썬과 JAVA의 비슷한점과 다른점을 알려주세요."]

for question in questions:
    relevant_text = "\n".join(retrieve_relevant_text(question, chunks, model, index))
    response = llm(prompt.format(relevant_text, question), max_tokens=256, stop=["</s>"])
    print("?> 질문:", question)
    print("!> LLM 응답:")
    print(response["choices"][0]["text"].strip())
    print()


"""Output
?> 질문: 파이썬이 어디에 쓰이나요?
!> LLM 응답:
파이썬은 웹 개발, 데이터 분석, 머신 학습 등에 사용되며 있습니다.

?> 질문: 파이썬의 장점은 무엇인가요?
!> LLM 응답:
파이썬의 장점에 대한 정보가 없습니다. 이걸 추측하지 말고 파이썬 공식 문서에서 이야기해주시는 내용을 기반으로 답변하십시오.

?> 질문: 파이썬은 뱀인가요?
!> LLM 응답:
정보가 없습니다. 파이썬과 비교하는 내용이 웹 문서에 없습니다. 파이썬은 뱀인가요?라는 질문에 대한 정보가 없습니다.

?> 질문: 파이썬과 JAVA의 비슷한점과 다른점을 알려주세요.
!> LLM 응답:
파이썬과 JAVA는 객체 지향적인 프로그래밍 언어이며, 모듈, 클래스, 객체와 같은 언어의 요소가 내부에서 접근할 수 있고, 리플렉션을 이용한 기술을 쓸 수 있다는 공통점이 있습니다.
다른점으로 파이써는 동적으로 타입 캐스팅을 지원하며, 함수 파라미터, 함수 반환 값 등에 대한 타입 캐스팅을 지원하며, 또한 함수 정의 시 파라미터의 타입을 지정하지 않으면 자동으로 추론할 수 있습니다.
반면 JAVA는 정적으로 타입 캐스
"""
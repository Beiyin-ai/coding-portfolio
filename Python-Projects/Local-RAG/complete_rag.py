### 🥁 跑程式之前先做下一行的環境設定：
### 👉 export SENTENCE_TRANSFORMERS_HOME="$HOME/model/"
### ai_程式設計班， AI是什麼 ， 我喜歡寵物

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8880/v1",
    api_key="none"
)

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2" )

documents = [
    "AI正在大大的影響我們",
    "AI agents are transforming software development.",
    "貓正在睡覺",
    "人工智慧正在改變世界",
    "Machine learning is part of AI",
    "貓是一種動物",
    "人工智慧是一種模擬人類智慧的技術。",
    "Machine learning is a subset of artificial intelligence.",
    "深度學習使用神經網路來學習資料特徵。",
    "Python 是目前最流行的 AI 開發語言。",
    "Vector database 用來儲存 embedding 向量。",
    "貓會很會搗蛋經常弄亂家裡",
    "貓很敏感又愛玩",
    "FAISS 是 Meta 開發的向量搜尋工具。",
    "Large Language Model 可以生成自然語言。",
    "RAG 是 retrieval augmented generation 技術。"
]

vectors = model.encode( documents )
index = faiss.IndexFlatL2( len( vectors[0] ) )

index.add(np.array(vectors))

def search(query, top_k=3):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), top_k )
    results = [documents[i] for i in I[0]]
    return results

def ask_llm(query):
    context = search(query, 3)
    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

while True:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    q = input("💭 Question:✨ ")
    print(ask_llm(q))
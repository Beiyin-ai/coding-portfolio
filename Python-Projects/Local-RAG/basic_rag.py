from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

### 底下指令會自動下載 模型：預設 放在 ~/.cache/torch/sentence_transformers/
##  BAAI/bge-m3  大小：2.3 GB
# model = SentenceTransformer("BAAI/bge-m3", cache_folder="~/model" )
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" )

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
    "FAISS 是 Meta 開發的向量搜尋工具。",
    "Large Language Model 可以生成自然語言。",
    "RAG 是 retrieval augmented generation 技術。"
]

vectors = model.encode( documents )

print( "documents:", len(documents) )
dimension = len( vectors[0] )
print( "vector dimension:", dimension )
print( type( vectors ))
print( vectors.shape )

index = faiss.IndexFlatL2( len( vectors[0] ) )
index.add(np.array(vectors))
print("index size:", index.ntotal)

# query_vector = model.encode(["AI technology"])
query_vector = model.encode(["AI是什麼"])

top_k = 3
D, I = index.search(np.array( query_vector ), k= top_k )

print( I, D )
results = [documents[i] for i in I[0]]
print(results)
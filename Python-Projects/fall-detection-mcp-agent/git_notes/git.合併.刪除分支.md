👉 cd  ~/rag

😀…:~/rag👉 vv

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 git log

(rag) 😀…:~/rag👉 git branch -d faiss_doc

(rag) 😀…:~/rag👉 git config --global alias.co checkout

(rag) 😀…:~/rag👉 git co master

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 git log

(rag) 😀…:~/rag👉 ll faiss_doc.py
ls: 無法存取 'faiss_doc.py': 沒有此一檔案或目錄

(rag) 😀…:~/rag👉 git co faiss_doc

(rag) 😀…:~/rag👉 ll faiss_doc.py

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 git log

(rag) 😀…:~/rag👉 git co master

(rag) 😀…:~/rag👉 git merge faiss_doc

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 ll faiss_doc.py

### 假設只有這個造成衝突
(rag) 😀…:~/rag👉 cp ~/Downloads/ai/a4/myRag.faiss_doc.py  myRag.py

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 git add .

(rag) 😀…:~/rag👉 git commit -m '合併前'

(rag) 😀…:~/rag👉 git status

(rag) 😀…:~/rag👉 git log

(rag) 😀…:~/rag👉 git merge faiss_doc

(rag) 😀…:~/rag👉 git branch 

(rag) 😀…:~/rag👉 git branch -d faiss_doc

(rag) 😀…:~/rag👉 git branch 

(rag) 😀…:~/rag👉 git branch -d faiss_pdf

(rag) 😀…:~/rag👉 git branch -D faiss_pdf

(rag) 😀…:~/rag👉 git branch
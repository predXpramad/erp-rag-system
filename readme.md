---



\# 🚀 Steps to Run the ERP RAG System (End-to-End)



---



\## 1️⃣ Prerequisites



Ensure the following are installed on your system:



\### Software



\* \*\*Python 3.10 or above\*\*

\* \*\*Git\*\*

\* \*\*Ollama (Local LLM runtime)\*\*

&nbsp; 👉 \[https://ollama.com/download](https://ollama.com/download)



\### Hardware (Recommended)



\* Minimum \*\*8 GB RAM\*\*

\* CPU is sufficient (GPU optional)



---



\## 2️⃣ Open the Project Directory



```bash

cd erp-rag-system

```



You should see:



```

backend/

scripts/

data/

requirements.txt

```



---



\## 3️⃣ Create \& Activate Virtual Environment



\### Create virtual environment



```bash

python -m venv venv

```



\### Activate



\*\*Windows (PowerShell):\*\*



```powershell

venv\\Scripts\\activate

```



\*\*Linux / macOS:\*\*



```bash

source venv/bin/activate

```



---



\## 4️⃣ Install Python Dependencies



```bash

pip install -r requirements.txt

```



If `requirements.txt` is missing:



```bash

pip install fastapi uvicorn pydantic pdfplumber nltk sentence-transformers faiss-cpu

```



---



\## 5️⃣ Install \& Prepare Local LLM (Ollama)



\### Verify Ollama installation



```bash

ollama --version

```



\### Pull model (one-time)



```bash

ollama pull mistral

```



\### Optional test



```bash

ollama run mistral

```



(Type a question → confirm response → press `Ctrl+C`)



---



\## 6️⃣ Add ERP Documents



Place \*\*one or more PDF files\*\* inside:



```

data/raw\_docs/

```



Example:



```

data/raw\_docs/

&nbsp;├── erp\_user\_manual.pdf

&nbsp;├── finance\_policy.pdf

```



---



\## 7️⃣ Run Document Ingestion



This step:



\* Reads PDFs

\* Cleans text

\* Chunks content

\* Stores metadata



```bash

python -m scripts.ingest\_all

```



Expected output:



```

Ingested XX chunks

```



---



\## 8️⃣ Build Embeddings \& FAISS Vector Index



This step:



\* Converts chunks into embeddings

\* Builds FAISS index



```bash

python -m backend.embeddings.embedder

```



Expected output:



```

FAISS index built with XX vectors

```



---



\## 9️⃣ Start the Backend Server



```bash

uvicorn backend.app:app --reload

```



Backend will run at:



```

http://127.0.0.1:8000

```



---



\## 🔟 Open the UI (IMPORTANT)



🚫 Do NOT open HTML files directly

✅ Open in browser:



```

http://127.0.0.1:8000

```



You will see the \*\*ERP Assistant UI\*\*.



---



\## 1️⃣1️⃣ Use the Application



\* Ask ERP-related questions

\* Answers are generated using:



&nbsp; \* FAISS retrieval

&nbsp; \* ERP document context

&nbsp; \* Local LLM (Ollama)

\* Sources are shown for transparency



---



\## 🔄 Typical End-to-End Flow



1\. User enters question in UI

2\. FastAPI `/ask` endpoint is called

3\. Query → embedding

4\. FAISS retrieves relevant chunks

5\. Prompt built using retrieved context

6\. Ollama generates answer

7\. Answer + sources returned to UI



---



\## 🧹 Re-Index / Reset Data (When Documents Change)



If you add or remove PDFs:



```bash

python -m scripts.ingest\_all

python -m backend.embeddings.embedder

```



Then restart backend:



```bash

uvicorn backend.app:app --reload

```



---



\## 🛑 Common Issues \& Fixes



\### Issue: No answer or irrelevant answer



✔ Ensure:



\* PDFs exist in `data/raw\_docs`

\* Ingestion + embedding steps were run



\### Issue: Ollama not found



✔ Restart terminal after installing Ollama



\### Issue: Port already in use



✔ Stop old server or change port:



```bash

uvicorn backend.app:app --reload --port 8001

```



---



\## ✅ Final Status



✔ Fully local RAG system

✔ No cloud API dependency

✔ ERP document grounding

✔ UI + backend properly linked

✔ Interview / demo / submission ready



---




-----

# 🚀 ERP RAG System (End-to-End Local Deployment)

This repository contains the complete instructions for setting up and running a local Retrieval-Augmented Generation (RAG) system, designed to answer questions based on your custom ERP documentation.

It leverages FastAPI for the backend, FAISS for vector indexing, and **Ollama** for running a local Large Language Model (LLM), ensuring a fully private, offline, and cloud-independent solution.

-----

## 1\. Prerequisites

Ensure you have the following software and hardware resources available before beginning the setup.

### 💻 Software

  * **Python 3.10 or above**
  * **Git**
  * **Ollama (Local LLM Runtime)**
      * 👉 [https://ollama.com/download](https://ollama.com/download)

### ⚙️ Hardware (Recommended)

  * Minimum **8 GB RAM**
  * CPU is sufficient (GPU is optional for faster LLM inference)

-----

## 2\. Setup and Installation

Follow these steps sequentially to set up the project environment and dependencies.

### 2.1. Open the Project Directory

Navigate to the project's root directory:

```bash
cd erp-rag-system
```

The structure should look like this:

```
backend/
scripts/
data/
requirements.txt
```

### 2.2. Create & Activate Virtual Environment

It is highly recommended to use a virtual environment.

#### Create

```bash
python -m venv venv
```

#### Activate

| Operating System | Command |
| :--- | :--- |
| **Windows (PowerShell)** | `venv\Scripts\activate` |
| **Linux / macOS** | `source venv/bin/activate` |

### 2.3. Install Python Dependencies

Install the required libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is missing, run:
>
> ```bash
> pip install fastapi uvicorn pydantic pdfplumber nltk sentence-transformers faiss-cpu
> ```

-----

## 3\. Ollama (Local LLM) Configuration

The RAG system requires a local LLM running via Ollama.

### 3.1. Verify Ollama Installation

Confirm that Ollama is correctly installed and accessible from your terminal.

```bash
ollama --version
```

### 3.2. Pull the Base Model (One-Time)

Download the `mistral` model, which will be used for generation.

```bash
ollama pull mistral
```

### 3.3. Optional Test

Run the model directly to ensure it is working. Press `Ctrl+C` to exit.

```bash
ollama run mistral
```

-----

## 4\. Document Ingestion and Indexing

This is the core process where your ERP documents are turned into a searchable knowledge base.

### 4.1. Add ERP Documents

Place **one or more PDF files** containing your ERP documentation inside the following directory:

```
data/raw_docs/
```

**Example:**

```
data/raw_docs/
 ├── erp_user_manual.pdf
 └── finance_policy.pdf
```

### 4.2. Run Document Ingestion (Preprocessing)

This script reads the PDFs, cleans the text, and chunks the content for indexing.

```bash
python -m scripts.ingest_all
```

**Expected output:**

```
Ingested XX chunks
```

### 4.3. Build Embeddings & FAISS Vector Index

This script converts the preprocessed text chunks into numerical embeddings and builds the **FAISS** vector index for fast retrieval.

```bash
python -m backend.embeddings.embedder
```

**Expected output:**

```
FAISS index built with XX vectors
```

-----

## 5\. Run the Application

The system is now ready to be served.

### 5.1. Start the Backend Server

Run the FastAPI application using `uvicorn`. The `--reload` flag is useful for development.

```bash
uvicorn backend.app:app --reload
```

The backend server will be accessible at:

```
http://127.0.0.1:8000
```

### 5.2. Open the UI

Access the ERP Assistant UI by opening the backend address in your web browser.

✅ Open in browser:

```
http://127.0.0.1:8000
```

> 🚫 **Crucial:** Do NOT open any HTML files directly from the file system; the UI must be served by the backend.

-----

## 6\. System Flow and Maintenance

### 6.1. Typical End-to-End Flow

The following steps describe how the RAG system processes a user's question:

1.  User enters question in the UI.
2.  FastAPI `/ask` endpoint is called.
3.  The user's **Query is converted to an embedding**.
4.  **FAISS retrieves** the most relevant text chunks from the ERP documents (context).
5.  A comprehensive **Prompt is built** using the original question and the retrieved context.
6.  **Ollama (local LLM) generates the answer** based *only* on the provided context.
7.  Answer and sources are returned to the UI for display.

### 6.2. Re-Index / Reset Data

If you modify, add, or remove PDF documents from `data/raw_docs`, you must re-run the ingestion and embedding steps:

```bash
python -m scripts.ingest_all
python -m backend.embeddings.embedder
```

After re-indexing, **restart the backend server**:

```bash
uvicorn backend.app:app --reload
```

-----

## 7\. Common Issues & Fixes

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| **No answer or irrelevant answer** | Missing or outdated knowledge base. | ✔ Ensure PDFs exist in `data/raw_docs` and ingestion/embedding steps were run *successfully*. |
| **Ollama not found** | Terminal session not recognizing the installation path. | ✔ **Restart the terminal** after installing Ollama. |
| **Port already in use** | An old server instance is running, or another application is using port 8000. | ✔ **Stop the old server** process or change the port:<br>`uvicorn backend.app:app --reload --port 8001` |

-----

## ✅ Final Status

  * ✔ Fully local RAG system running on your machine.
  * ✔ **No cloud API dependency** for embeddings or LLM.
  * ✔ Answers grounded in your custom ERP documentation.
  * ✔ UI, backend, and LLM properly linked.
  * ✔ Ready for interview, demo, or internal submission.

-----

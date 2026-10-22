# enterprise-knowledge-assistant
An enterprise-grade RAG microservice built with FastAPI, LangChain, Google Gemini, and AstraDB featuring multi-tenant metadata filtering and messy data ingestion pipelines

# 🏢 Enterprise Knowledge Assistant (AI RAG Microservice)

A production-ready Retrieval-Augmented Generation (RAG) microservice designed for enterprise environments. It ingests messy unstructured documents, handles semantic chunking with metadata tagging for secure multi-tenancy, and serves high-accuracy answers via a scalable FastAPI backend.

## 🚀 Tech Stack
* **Framework:** FastAPI, Uvicorn, Pydantic v2
* **Orchestration:** LangChain (Retrieval Chains, Recursive Text Splitters)
* **Vector Database:** AstraDB (Serverless Cassandra-backed vector storage with metadata filtering)
* **LLM & Embeddings:** Google Gemini (`gemini-3.8-flash` & `gemini-embedding-2-preview`)

---

## 🛠️ Project Architecture
1. **Ingestion Pipeline (`app/ingester.py`):** Cleans and chunks raw corporate documents (HR, Legal, Engineering) and injects security/department metadata.
2. **Vector Store (`app/rag.py`):** Manages dense vector generation and indexes documents into a serverless AstraDB collection.
3. **API Service (`app/main.py`):** Exposes high-performance REST endpoints with optional department-level multi-tenant filtering.

---

## ⚙️ Local Setup & Installation
# 🚀 How to Run the Enterprise Knowledge Assistant

Follow these steps to start the document ingestion pipeline and run the local FastAPI backend.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.10 or higher** installed.
- An active `.env` file configured with your Google Gemini and AstraDB credentials.
- The project dependencies installed.
- A Python virtual environment (`venv`) created in the project directory.

## Step 1: Open Terminal and Activate the Virtual Environment

Navigate to your project directory and activate your Python virtual environment.

### Windows (PowerShell)

```powershell
cd C:\Giri\Learning\enterprise-knowledge-assistant
.\venv\Scripts\activate
```

### macOS / Linux

```bash
cd path/to/enterprise-knowledge-assistant
source venv/bin/activate
```

**Verify activation:** Ensure `(venv)` appears at the beginning of your terminal prompt.

## Step 2: Run the Document Ingestion Pipeline

Before querying the AI, you need to parse, chunk, and embed your sample enterprise documents into your AstraDB vector database.

Run the ingestion script:

```bash
python -m app.ingester
```

### Expected Output

```text
Starting document ingestion pipeline...
-> Splitting messy data yielded 3 clean chunks.
-> Successfully embedded and stored chunks into AstraDB!
```

This step prepares your documents for retrieval by converting them into embeddings and storing them in AstraDB.

> **Note:** The exact output may vary depending on your documents and ingestion implementation.

## Step 3: Start the FastAPI Backend Server

Launch the FastAPI application using Uvicorn with automatic reloading enabled:

```bash
uvicorn app.main:app --reload
```

### Expected Output

```text
INFO:     Will watch for changes in these directories: [...]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started server process [...]
INFO:     Application startup complete.
```

Your backend is now running locally.

## Step 4: Test the RAG Endpoint

Open the interactive Swagger UI in your browser:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Follow these steps to test the RAG endpoint:

1. Expand the `POST /api/query` route.
2. Click **Try it out**.
3. Enter the following JSON payload in the request body:

   ```json
   {
     "question": "What is the policy for microservices deployment?",
     "department_filter": "Engineering"
   }
   ```

4. Click **Execute**.
5. Review the API response, including the generated answer and source metadata returned by your implementation.

## 🎯 What Happens Under the Hood?

The Enterprise Knowledge Assistant uses a Retrieval-Augmented Generation (RAG) workflow:

1. **Document ingestion:** Loads and processes enterprise documents.
2. **Text chunking:** Splits documents into smaller, searchable chunks.
3. **Embedding generation:** Converts text chunks into vector embeddings.
4. **Vector storage:** Stores embeddings and associated metadata in AstraDB.
5. **Semantic retrieval:** Retrieves relevant document chunks based on the user's question and optional department filter.
6. **Answer generation:** Uses Google Gemini to generate a response grounded in the retrieved context.

## 🛠️ Technologies Used

- **Python** — Application development
- **FastAPI** — REST API backend
- **Uvicorn** — ASGI server
- **LangChain** — LLM and RAG integration
- **Google Gemini** — Large language model
- **AstraDB** — Vector database for semantic search

---

**You're all set!** Your Enterprise Knowledge Assistant is ready to ingest documents and answer questions through the FastAPI endpoint.

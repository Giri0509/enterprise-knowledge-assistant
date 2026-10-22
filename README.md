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

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/enterprise-knowledge-assistant.git](https://github.com/YOUR_USERNAME/enterprise-knowledge-assistant.git)
   cd enterprise-knowledge-assistant

🚀 How to Run the Enterprise Knowledge Assistant
Follow these steps in your terminal to spin up your document ingestion pipeline and local FastAPI backend.

Prerequisites
Python 3.10 or higher installed.

Active .env file configured with your Google Gemini and AstraDB credentials.

Step 1: Open Terminal & Activate Virtual Environment
Navigate to your project directory and activate your Python virtual environment:

On Windows (PowerShell):

PowerShell
cd C:\Giri\Learning\enterprise-knowledge-assistant
.\venv\Scripts\activate
On macOS / Linux:

Bash
cd path/to/enterprise-knowledge-assistant
source venv/bin/activate
(Ensure (venv) appears at the beginning of your terminal prompt).

Step 2: Run the Document Ingestion Pipeline
Before querying your AI, you need to parse, chunk, and embed your sample enterprise documents into your serverless AstraDB vector database.

Run the ingestion script:

Bash
python -m app.ingester
Expected Output:

Plaintext
Starting document ingestion pipeline...
-> Splitting messy data yielded 3 clean chunks.
-> Successfully embedded and stored chunks into AstraDB!
Step 3: Start the FastAPI Backend Server
Now launch your production-ready FastAPI service using Uvicorn with auto-reload enabled:

Bash
uvicorn app.main:app --reload
Expected Output:

Plaintext
INFO:     Will watch for changes in these directories: [...]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started server process [...]
INFO:     Application startup complete.
Step 4: Test Your RAG Endpoint Live
Open your browser and navigate to the interactive Swagger UI:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Expand the POST /api/query route.

Click Try it out.

Pass the following JSON payload into the request body:

JSON
{
  "question": "What is the policy for microservices deployment?",
  "department_filter": "Engineering"
}
Click Execute to see your live RAG response, synthesized text, and metadata source attribution!

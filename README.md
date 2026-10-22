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

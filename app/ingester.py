from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag import vector_store

def ingest_sample_enterprise_data():
    """
    Simulates ingesting messy enterprise documents (e.g., from HR, Legal, or Engineering)
    with custom metadata tagging for secure multi-tenant filtering.
    """
    
    # 1. Raw "messy" enterprise documents text (Simulating messy data dumps)
    raw_documents = [
        Document(
            page_content="[CONFIDENTIAL] Engineering Policy 2026: All microservices must be deployed using Docker containers. "
                         "Vercel is strictly reserved for serverless frontend applications or lightweight FastAPI endpoints "
                         "that do not exceed execution timeout limits.",
            metadata={"department": "Engineering", "security_level": "internal", "source": "eng_handbook.txt"}
        ),
        Document(
            page_content="HR Benefit Update: Dental insurance coverage has increased to 80% for all full-stack and FDE engineers "
                         "effective Q2. Submit receipts to the finance portal within 30 days.",
            metadata={"department": "HR", "security_level": "public", "source": "hr_benefits.pdf"}
        ),
        Document(
            page_content="Legal Compliance: Client data containing PII must never be stored in local volatile vector stores. "
                         "Always enforce metadata tenant isolation keys when querying AstraDB collections.",
            metadata={"department": "Legal", "security_level": "restricted", "source": "compliance_guide.docx"}
        )
    ]

    # 2. Use Recursive Text Splitter to break documents into clean logical chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    docs_to_store = text_splitter.split_documents(raw_documents)

    print(f"-> Splitting messy data yielded {len(docs_to_store)} clean chunks.")

    vector_store.add_documents(docs_to_store)
    print("-> Successfully embedded and stored chunks into AstraDB!")

if __name__ == "__main__":
    print("Starting document ingestion pipeline...")
    ingest_sample_enterprise_data()

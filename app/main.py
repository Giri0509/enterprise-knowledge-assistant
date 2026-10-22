from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from app.rag import vector_store, llm

app = FastAPI(
    title="Enterprise Knowledge Assistant API",
    version="1.0.0",
    description="AI Forward Deployed Engineer RAG Microservice"
)

class QueryRequest(BaseModel):
    question: str
    department_filter: str = None

@app.get("/")
def home():
    return {"status": "online", "message": "Enterprise Knowledge Assistant RAG API is live!"}

@app.post("/api/query")
def query_knowledge_base(request: QueryRequest):
    """
    RAG Endpoint: Retrieves relevant context from AstraDB and generates an answer using Gemini.
    Demonstrates enterprise metadata multi-tenancy filtering.
    """
    try:
        # 1. Configure the retriever with optional tenant/department metadata filtering
        search_kwargs = {"k": 2}
        if request.department_filter:
            search_kwargs["filter"] = {"department": request.department_filter}

        retriever = vector_store.as_retriever(search_kwargs=search_kwargs)

        # 2. Define the enterprise-grade prompt structure
        system_prompt = (
            "You are an AI Forward Deployed Engineer assistant. "
            "Use the retrieved enterprise context below to answer the user's question accurately. "
            "If you cannot find the answer in the context, state clearly that you do not know.\n\n"
            "Context:\n{context}"
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        # 3. Construct the LangChain RAG chain
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)

        response = rag_chain.invoke({"input": request.question})

        return {
            "question": request.question,
            "answer": response["answer"],
            "sources": [
                doc.metadata.get("source", "unknown") for doc in response.get("context", [])
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
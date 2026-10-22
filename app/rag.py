from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_astradb import AstraDBVectorStore
from app.config import settings

# 1. Initialize Google Gemini Embeddings 
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    google_api_key=settings.GOOGLE_API_KEY
)

# 2. Initialize the Astra DB Vector Store connection
vector_store = AstraDBVectorStore(
    embedding=embeddings,
    collection_name=settings.ASTRA_DB_COLLECTION,
    api_endpoint=settings.ASTRA_DB_API_ENDPOINT,
    token=settings.ASTRA_DB_APPLICATION_TOKEN,
)

# 3. Initialize the Gemini LLM with the active 2026 model string
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0.3,
    convert_system_message_to_human=True
)
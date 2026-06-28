"""
RAG Pipeline

Author : Vansh Anand
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from rag.loader import load_documents


embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def create_vector_store():

    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50

    )

    chunks = splitter.split_documents(docs)

    vector_store = Chroma.from_documents(

        documents=chunks,

        embedding=embedding,

        persist_directory="./database/chroma_db"

    )

    return vector_store


vector_store = create_vector_store()


def retrieve_context(query):

    results = vector_store.similarity_search(query, k=2)

    context = ""

    for doc in results:

        context += doc.page_content + "\n"

    return context

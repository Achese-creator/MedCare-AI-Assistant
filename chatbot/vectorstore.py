from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from chatbot.config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
)


def get_embeddings():
    """
    Initialize the embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def create_vectorstore(chunks):
    """
    Create a FAISS vector database.
    """

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    return vectorstore


from pathlib import Path


def save_vectorstore(vectorstore):
    """
    Save the FAISS index.
    """

    Path(FAISS_INDEX_PATH).mkdir(parents=True, exist_ok=True)

    vectorstore.save_local(FAISS_INDEX_PATH)


def load_vectorstore():
    """
    Load the FAISS index.
    """

    embeddings = get_embeddings()

    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )
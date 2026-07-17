from pathlib import Path

from chatbot.config import SEARCH_TYPE, TOP_K, FAISS_INDEX_PATH
from chatbot.document_loader import load_documents
from chatbot.text_splitter import split_documents
from chatbot.vectorstore import (
    create_vectorstore,
    save_vectorstore,
    load_vectorstore,
)


def get_retriever():
    """
    Load the FAISS vector database.
    If it doesn't exist, build it automatically.
    """

    index_path = Path(FAISS_INDEX_PATH)

    # Check whether the FAISS index exists
    if not (index_path / "index.faiss").exists():
        print("FAISS index not found. Building vector database...")

        documents = load_documents()
        chunks = split_documents(documents)

        vectorstore = create_vectorstore(chunks)
        save_vectorstore(vectorstore)

        print("Vector database created successfully.")

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={"k": TOP_K},
    )

    return retriever
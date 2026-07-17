from chatbot.config import SEARCH_TYPE, TOP_K
from chatbot.vectorstore import load_vectorstore


def get_retriever():
    """
    Load the FAISS vector database and create
    a retriever.
    """

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": TOP_K
        }
    )

    return retriever
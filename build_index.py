from chatbot.loader import load_documents
from chatbot.logger import logger
from chatbot.splitter import split_documents
from chatbot.vectorstore import create_vectorstore, save_vectorstore


def main():
    logger.info("=" * 60)
    logger.info("Building FAISS Vector Database")
    logger.info("=" * 60)

    logger.info("Loading documents...")
    documents = load_documents()
    logger.info(f"Loaded {len(documents)} documents.")

    logger.info("Splitting documents...")
    chunks = split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks.")

    logger.info("Creating vector database...")
    vectorstore = create_vectorstore(chunks)

    logger.info("Saving vector database...")
    save_vectorstore(vectorstore)

    logger.info("Vector database built successfully!")
    logger.info("Saved to: database/faiss_index")


if __name__ == "__main__":
    main()
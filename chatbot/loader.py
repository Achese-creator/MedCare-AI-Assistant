from pathlib import Path
from langchain_core.documents import Document


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data"


def load_documents(data_folder=DATA_PATH):
    """
    Load all .txt files from the data folder into LangChain Documents.
    """

    data_path = Path(data_folder)

    documents = []

    for file in data_path.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        documents.append(
            Document(
                page_content=text,
                metadata={"source": file.name},
            )
        )

    return documents
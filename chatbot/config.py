from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

FAISS_INDEX_PATH = BASE_DIR / "database" / "faiss_index"

LLM_MODEL = "llama-3.3-70b-versatile"

TEMPERATURE = 0.2
MAX_TOKENS = 400

TOP_K = 3
SEARCH_TYPE = "similarity"
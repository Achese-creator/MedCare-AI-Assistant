"""
Application configuration.
"""

# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ==========================
# Vector Database
# ==========================

FAISS_INDEX_PATH = "database/faiss_index"

# ==========================
# Groq Model
# ==========================

LLM_MODEL = "llama-3.3-70b-versatile"

# ==========================
# Generation Parameters
# ==========================

TEMPERATURE = 0.2

MAX_TOKENS = 400

# ==========================
# Retrieval
# ==========================

TOP_K = 3

SEARCH_TYPE = "similarity"
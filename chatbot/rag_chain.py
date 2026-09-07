import time

from chatbot.config import (
    LLM_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
)
from chatbot.llm import get_llm
from chatbot.prompts import SYSTEM_PROMPT


class RAGChatbot:
    """
    Retrieval-Augmented Generation chatbot.
    """

    def __init__(self, retriever):
        self.client = get_llm()
        self.retriever = retriever

    def ask(self, question: str):
        """Answer a question using Retrieval-Augmented Generation."""

        try:
            start_time = time.perf_counter()
            
            # Retrieve relevant documents
            documents = self.retriever.invoke(question)

            context = "\n\n".join(doc.page_content for doc in documents)

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""
Hospital Knowledge Base:

{context}

Customer Question:

{question}

Instructions:
- Answer ONLY using the hospital knowledge base.
- If the answer cannot be found, clearly say so.
- Never invent information.
""",
                },
            ]

            response = self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                temperature=TEMPERATURE,
                max_completion_tokens=MAX_TOKENS,
            )

            answer = response.choices[0].message.content
            response_time = time.perf_counter() - start_time

            sources = []
            for doc in documents:
                source = doc.metadata.get("source", "Unknown")
                if source not in sources:
                    sources.append(source)

            return {
                "success": True,
                "answer": answer,
                "sources": sources,
                "documents": documents,
                "response_time": round(response_time, 2),
            }

        except Exception as e:
            from chatbot.logger import logger

            logger.exception("Error while processing user question.")

            return {
                "success": False,
                "answer": (
                    "I'm sorry, but I encountered an unexpected error while "
                    "processing your request. Please try again."
                ),
                "sources": [],
                "documents": [],
                "response_time": 0.0,
                "error": str(e),
            }
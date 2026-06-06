from rag.retriever import SchemaRetriever
from utils.gemini_client import GeminiClient


class RAGSchemaGenerator:

    def __init__(self):

        self.retriever = SchemaRetriever()

        self.llm = GeminiClient()

    def generate_schema(
        self,
        requirement: str
    ):

        documents = (
            self.retriever.retrieve(
                requirement
            )
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        response = (
            self.llm.generate_schema_response(
                requirement=requirement,
                context=context
            )
        )

        return response
from rag.vector_store import VectorStoreManager


class SchemaRetriever:

    def __init__(self):

        self.vector_store = (
            VectorStoreManager()
            .load_vector_store()
        )

    def retrieve(
        self,
        query: str,
        k: int = 3
    ):

        results = (
            self.vector_store
            .similarity_search(
                query,
                k=k
            )
        )

        return results
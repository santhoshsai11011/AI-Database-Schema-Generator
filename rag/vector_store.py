from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


class VectorStoreManager:

    def __init__(self):

        self.embedding_model = (
            GoogleGenerativeAIEmbeddings(
                model="models/gemini-embedding-2"
            )
        )

    def create_vector_store(
        self,
        chunks: list
    ):

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=self.embedding_model
        )

        return vector_store

    def save_vector_store(
        self,
        vector_store,
        save_path="vector_store/faiss_index"
    ):

        vector_store.save_local(
            save_path
        )

    def load_vector_store(
        self,
        save_path="vector_store/faiss_index"
    ):

        vector_store = FAISS.load_local(
            save_path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

        return vector_store
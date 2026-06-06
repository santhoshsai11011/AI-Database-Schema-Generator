from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


class EmbeddingGenerator:

    def __init__(self):

        self.embedding_model = (
            GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-2"
    )
        )

        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100
            )
        )

    def load_knowledge_base(
        self,
        file_path: str
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    def create_chunks(
        self,
        text: str
    ):

        chunks = self.text_splitter.split_text(
            text
        )

        return chunks

    def generate_embeddings(
        self,
        chunks: list
    ):

        embeddings = []

        for chunk in chunks:

            vector = (
                self.embedding_model
                .embed_documents([chunk])[0]
            )

            embeddings.append(
                {
                    "text": chunk,
                    "embedding": vector
                }
            )

        return embeddings
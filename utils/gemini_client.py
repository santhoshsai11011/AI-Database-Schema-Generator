import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_schema_response(self, requirement: str):

        prompt = f"""
You are an expert database architect.

Analyze the following requirement and identify:

1. Entities
2. Attributes
3. Primary Keys
4. Relationships

Requirement:

{requirement}

Return the answer in a structured format.
"""

        response = self.model.generate_content(prompt)

        return response.text
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

        self.model = genai.GenerativeModel("gemini-2.0-flash-lite")

    def generate_schema_response(
        self,
        requirement: str,
        context: str = ""
    ):
        prompt = f"""
You are an expert Database Architect.

Reference Context:
{context}

User Requirements:
{requirement}

Generate ONLY valid JSON.

Output format:

{{
    "entities": [
        {{
            "name": "",
            "attributes": [],
            "primary_key": ""
        }}
    ],
    "relationships": [
        {{
            "source": "",
            "target": "",
            "type": ""
        }}
    ]
}}

Rules:

1. Return ONLY JSON.
2. No markdown.
3. No explanations.
4. No code blocks.
5. Ensure valid JSON syntax.
"""

        response = self.model.generate_content(prompt)

        return response.text
from utils.gemini_client import GeminiClient

client = GeminiClient()

response = client.generate_schema_response(
    "Library Management System"
)

print(response)
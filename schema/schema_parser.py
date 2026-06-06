import json


class SchemaParser:

    @staticmethod
    def parse(response: str):

        response = response.strip()

        try:

            return json.loads(
                response
            )

        except json.JSONDecodeError:

            raise ValueError(
                "Invalid JSON received from Gemini."
            )
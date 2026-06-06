import json


class SchemaParser:

    @staticmethod
    def parse(response: str):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace(
                "```json",
                ""
            )

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        try:

            return json.loads(
                response
            )

        except json.JSONDecodeError:

            raise ValueError(
                "Invalid JSON received from Gemini."
            )
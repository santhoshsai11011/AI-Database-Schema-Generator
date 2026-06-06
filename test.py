from rag.rag_chain import RAGSchemaGenerator

generator = (
    RAGSchemaGenerator()
)

schema = (
    generator.generate_schema(
        """
University Management System

Students enroll in courses.

Courses are taught by instructors.

Each instructor belongs to a department.
"""
    )
)

print(type(schema))

print()

print(schema)
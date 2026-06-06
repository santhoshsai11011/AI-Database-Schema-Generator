from schema.er_generator import (
    ERDiagramGenerator
)

sample_schema = {
    "entities": [
        {
            "name": "Student",
            "attributes": [
                "student_id",
                "name"
            ]
        },
        {
            "name": "Course",
            "attributes": [
                "course_id",
                "title"
            ]
        }
    ],
    "relationships": [
        {
            "source": "Student",
            "target": "Course",
            "type": "many_to_many"
        }
    ]
}

diagram = (
    ERDiagramGenerator.generate(
        sample_schema
    )
)

diagram.render(
    "er_diagram",
    format="png",
    cleanup=True
)

print(
    "ER Diagram generated successfully."
)
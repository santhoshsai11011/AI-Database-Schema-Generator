from schema.sql_generator import SQLGenerator

sample_schema = {
    "entities": [
        {
            "name": "Student",
            "attributes": [
                "student_id",
                "name"
            ],
            "primary_key": "student_id"
        },
        {
            "name": "Course",
            "attributes": [
                "course_id",
                "title"
            ],
            "primary_key": "course_id"
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

sql = SQLGenerator.generate(
    sample_schema
)

print(sql)
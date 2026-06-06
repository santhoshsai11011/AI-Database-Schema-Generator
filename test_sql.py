from schema.sql_generator import SQLGenerator

sample_schema = {
    "entities": [
        {
            "name": "Student",
            "attributes": [
                "student_id",
                "name",
                "email"
            ],
            "primary_key": "student_id"
        },
        {
            "name": "Course",
            "attributes": [
                "course_id",
                "course_name"
            ],
            "primary_key": "course_id"
        }
    ]
}

sql = SQLGenerator.generate(
    sample_schema
)

print(sql)
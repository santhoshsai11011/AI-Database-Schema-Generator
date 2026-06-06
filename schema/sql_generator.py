class SQLGenerator:

    @staticmethod
    def generate(schema_json):

        sql_statements = []

        entities = schema_json.get(
            "entities",
            []
        )

        relationships = schema_json.get(
            "relationships",
            []
        )

        # -------------------------
        # Entity Tables
        # -------------------------

        for entity in entities:

            table_name = entity.get(
                "name"
            )

            attributes = entity.get(
                "attributes",
                []
            )

            primary_key = entity.get(
                "primary_key"
            )

            columns = []

            for attribute in attributes:

                if attribute == primary_key:

                    columns.append(
                        f"{attribute} INT PRIMARY KEY"
                    )

                else:

                    columns.append(
                        f"{attribute} VARCHAR(255)"
                    )

            create_table = (
                f"CREATE TABLE {table_name} (\n    "
                + ",\n    ".join(columns)
                + "\n);"
            )

            sql_statements.append(
                create_table
            )

        # -------------------------
        # Many-to-Many Relationships
        # -------------------------

        for relationship in relationships:

            if relationship.get(
                "type"
            ) == "many_to_many":

                source = relationship.get(
                    "source"
                )

                target = relationship.get(
                    "target"
                )

                source_pk = (
                    source.lower() + "_id"
                )

                target_pk = (
                    target.lower() + "_id"
                )

                junction_table = (
                    f"CREATE TABLE {source}_{target} (\n"
                    f"    {source_pk} INT,\n"
                    f"    {target_pk} INT,\n\n"
                    f"    PRIMARY KEY (\n"
                    f"        {source_pk},\n"
                    f"        {target_pk}\n"
                    f"    )\n"
                    f");"
                )

                sql_statements.append(
                    junction_table
                )

        return "\n\n".join(
            sql_statements
        )
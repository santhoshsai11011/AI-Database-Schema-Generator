import os

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph

class ERDiagramGenerator:

    @staticmethod
    def generate(schema_json):

        diagram = Digraph(
            comment="ER Diagram"
        )

        entities = schema_json.get(
            "entities",
            []
        )

        relationships = schema_json.get(
            "relationships",
            []
        )

        # -------------------------
        # Entities
        # -------------------------

        for entity in entities:

            entity_name = entity.get(
                "name"
            )

            attributes = entity.get(
                "attributes",
                []
            )

            label = (
                entity_name
                + "\\n"
                + "\\n".join(attributes)
            )

            diagram.node(
                entity_name,
                label,
                shape="box"
            )

        # -------------------------
        # Relationships
        # -------------------------

        for relationship in relationships:

            source = relationship.get(
                "source"
            )

            target = relationship.get(
                "target"
            )

            rel_type = relationship.get(
                "type"
            )

            diagram.edge(
                source,
                target,
                label=rel_type
            )
        output_path = "er_diagram"
        diagram.render(
            output_path,
            format="png",
            cleanup=True
        )
        return output_path + ".png"
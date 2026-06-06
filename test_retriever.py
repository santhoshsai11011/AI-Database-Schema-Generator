from rag.retriever import SchemaRetriever

retriever = SchemaRetriever()

results = retriever.retrieve(
    "Hospital Management System"
)

print()

for i, doc in enumerate(results, start=1):

    print(
        f"\nRESULT {i}"
    )

    print(
        "-" * 50
    )

    print(
        doc.page_content[:500]
    )
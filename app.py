import streamlit as st
from rag.rag_chain import RAGSchemaGenerator
from schema.sql_generator import SQLGenerator
from schema.er_generator import ERDiagramGenerator

st.set_page_config(
    page_title="AI Database Schema Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #ffffff;
}

.main {
    background-color: #ffffff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #1e3a5f;
}

.stTextArea textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #cbd5e1;
}

.stButton button {
    width: 100%;
    background-color: #4DA6FF;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    height: 45px;
}

.stButton button:hover {
    background-color: #3399FF;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #F5FAFF;
}

</style>
""", unsafe_allow_html=True)

#Gemini Client Initialization

try:
    rag_generator = RAGSchemaGenerator()
except Exception as e:
    st.error(str(e))
    st.stop()
    
    
# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("Settings")

    st.markdown("---")

    st.subheader("Technology Stack")

    st.write("Python")
    st.write("Streamlit")
    st.write("Gemini API")
    st.write("LangChain")
    st.write("FAISS")
    st.write("MySQL")

    st.markdown("---")

    st.caption("Database Schema Generation System")

# -----------------------------
# Header
# -----------------------------

st.title("AI Database Schema Generator")

st.write(
    """
    Generate normalized database schemas from natural language requirements.
    """
)

st.markdown("---")

# -----------------------------
# Input Area
# -----------------------------

st.subheader("Requirement Specification")

user_input = st.text_area(
    label="Enter project requirements",
    height=250,
    placeholder="""
Example:

Develop a Library Management System.

A library manages books and members.
Each member can borrow multiple books.
Borrow records should contain issue date and return date.
"""
)

generate = st.button("Generate Schema")

# -----------------------------
# Output Section
# -----------------------------

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Schema Definition")

    schema_output = st.empty()

with col2:

    st.subheader("SQL Schema")

    sql_output = st.empty()

# -----------------------------
# ER Diagram Section
# -----------------------------

st.markdown("---")

st.subheader("ER Diagram")

diagram_output = st.empty()

# -----------------------------
# Schema Generation
# -----------------------------

if generate:

    if not user_input.strip():

        st.warning(
            "Please enter project requirements."
        )

    else:

        with st.spinner(
            "Analyzing requirements..."
        ):

            try:

                response = (
                    rag_generator.generate_schema(
                    user_input
                )
            )

                sql_schema = (
                    SQLGenerator.generate(
                        response
                    )
                )

                schema_output.json(response)

                sql_output.code(
                sql_schema,
                language="sql")

                diagram_path = (
                    ERDiagramGenerator.generate(response))

                diagram_output.image(
                    diagram_path,
                    use_container_width=True
                )

            except Exception as e:

                st.error(s
                    f"Generation failed: {e}"
                )
# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "AI-Powered Database Schema Generator"
)
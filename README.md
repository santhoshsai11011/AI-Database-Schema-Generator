# AI-Powered Database Schema Generator

## Overview

AI-Powered Database Schema Generator is an intelligent database design system that converts natural language software requirements into normalized database schemas.

The system leverages Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Large Language Models to automatically identify entities, attributes, keys, relationships, SQL schemas, and ER diagrams from user requirements.

The goal of this project is to reduce manual database design effort and accelerate the initial stages of software development.

---

## Features

### Natural Language to Database Schema

Convert plain English requirements into structured database schemas.

Example:

> Develop a Library Management System where members can borrow books and each borrowing record contains issue date and return date.

Generated Output:

* Entities
* Attributes
* Primary Keys
* Relationships

---

### Retrieval-Augmented Generation (RAG)

The system uses a custom knowledge base containing database design principles and common schema patterns.

Pipeline:

```text
User Requirement
        ↓
Vector Search (FAISS)
        ↓
Relevant Context Retrieval
        ↓
Gemini LLM
        ↓
Schema Generation
```

---

### Semantic Search using FAISS

* Text chunking
* Vector embeddings
* Similarity search
* Context retrieval

Improves schema quality by grounding responses with database design knowledge.

---

### Structured JSON Schema Generation

Generated schemas are converted into machine-readable JSON.

Example:

```json
{
  "entities": [
    {
      "name": "Student",
      "attributes": [
        "student_id",
        "name",
        "email"
      ],
      "primary_key": "student_id"
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
```

---

### Automated SQL Schema Generation

Automatically generates SQL DDL statements.

Example:

```sql
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);
```

---

### Relationship-Aware SQL Generation

Supports:

* One-to-One
* One-to-Many
* Many-to-Many

Many-to-Many relationships automatically generate junction tables.

Example:

```sql
CREATE TABLE Student_Course (
    student_id INT,
    course_id INT,

    PRIMARY KEY (
        student_id,
        course_id
    )
);
```

---

### ER Diagram Generation

Automatically generates Entity Relationship Diagrams using Graphviz.

Generated diagrams visually represent:

* Entities
* Attributes
* Relationships

---

### Interactive Streamlit Interface

Users can:

* Enter project requirements
* Generate schemas
* View SQL scripts
* View ER diagrams

All from a single web interface.

---

## System Architecture

```text
Natural Language Requirement
                ↓
        Streamlit UI
                ↓
        RAG Pipeline
                ↓
      Knowledge Retrieval
                ↓
         Gemini API
                ↓
       Structured JSON
                ↓
      SQL Generator
                ↓
     ER Diagram Generator
```

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM

* Google Gemini API

### RAG Components

* LangChain
* FAISS

### Embeddings

* Gemini Embeddings

### Database

* MySQL

### Visualization

* Graphviz

---

## Project Structure

```text
Database Schema Generator/
│
├── app.py
│
├── data/
│   └── database_design_kb.txt
│
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_chain.py
│
├── schema/
│   ├── schema_parser.py
│   ├── sql_generator.py
│   └── er_generator.py
│
├── utils/
│   └── gemini_client.py
│
├── vector_store/
│
├── test_embeddings.py
├── test_vector_store.py
├── test_retriever.py
├── test_rag.py
├── test_sql.py
├── test_er.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Database-Schema-Generator
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Graphviz Installation

### Windows

Download Graphviz:

https://graphviz.org/download/

Install Graphviz and add:

```text
C:\Program Files\Graphviz\bin
```

to your system PATH.

Verify installation:

```bash
dot -V
```

Expected output:

```text
dot - graphviz version ...
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## Example Workflow

### Input

```text
Develop a Library Management System.

A library manages books and members.
Members can borrow multiple books.
Borrow records contain issue date and return date.
```

### Output

#### Schema JSON

```json
{
  "entities": [
    {
      "name": "Book"
    },
    {
      "name": "Member"
    },
    {
      "name": "Borrowing"
    }
  ]
}
```

#### SQL

```sql
CREATE TABLE Book (...);

CREATE TABLE Member (...);

CREATE TABLE Borrowing (...);
```

#### ER Diagram

Generated automatically and displayed in the application.

---

## Future Enhancements

* SQL Export
* JSON Export
* ER Diagram Download
* PostgreSQL Support
* MongoDB Schema Generation
* Database Reverse Engineering
* Multi-Database Support
* Deployment on Streamlit Cloud

---

## Resume Highlights

* Built an AI-powered system that converts natural language requirements into normalized database schemas.
* Implemented a Retrieval-Augmented Generation (RAG) pipeline using vector embeddings and semantic search.
* Automated SQL schema creation and ER diagram generation.
* Integrated FAISS-based semantic retrieval for context-aware schema generation.
* Developed an interactive Streamlit application for end-to-end database design automation.

---

## License

This project is intended for educational and portfolio purposes.

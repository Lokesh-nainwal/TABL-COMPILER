# TABL-COMPILER
The Hinglish SQL Compiler lets users write SQL-like commands in Hinglish (Hindi + English) and executes them using a Python-based system. It supports operations like INSERT, SELECT, JOIN, and GROUP BY with a user-friendly Streamlit GUI and in-memory database.


# TABL ARCHITECTURE
Our current approach focuses on designing a mini-compiler that interprets Hinglish commands into SQL-like actions using a modular and layered architecture. The project is developed using Python for the backend and Streamlit for the frontend GUI.
🔧 System Design (Modules Overview):
1.	lex.py (Lexer)
o	Converts Hinglish input into tokens (e.g., "students mein daal value" → INSERT, INTO, IDENTIFIER)
o	Implements lexical analysis using pattern matching and regular expressions
2.	parser.py (Parser)
o	Parses token sequences into Abstract Syntax Trees (ASTs)
o	Identifies command types like CREATE, INSERT, SELECT, UPDATE, etc.
o	Supports nested commands (like loops) and multi-column conditions
3.	semantic.py (Semantic Analyzer & Executor)
o	Stores tables in an in-memory database (DATABASE = {})
o	Validates primary keys, data types, and WHERE clause conditions
o	Executes operations like JOIN, GROUP BY, LOOP-based inserts, etc.
4.	test_parser.py / test_semantic.py (Testing)
o	Used for verifying parsing and semantic outputs for a range of sample commands
o	Prints tokens, ASTs, and execution results for debugging
5.	streamlit_app.py (Frontend UI)
o	Built using Streamlit to simulate an online SQL editor
o	Accepts user input, displays parsed output, shows table data, and logs results
o	GUI includes Run, Table Viewer, and Output Log

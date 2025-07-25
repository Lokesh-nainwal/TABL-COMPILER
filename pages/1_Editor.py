import streamlit as st
import pandas as pd
from streamlit_ace import st_ace
from compiler.lexer import tokenize
from compiler.parser import parse
from compiler.semantic import check_ast, get_database

st.set_page_config(page_title="TABL Compiler Editor", layout="wide")

# -------------------- Theme Toggle --------------------
theme_mode = st.sidebar.radio(" Choose Theme", ["Light Mode", " Dark Mode"])

if theme_mode == "Dark Mode":
    editor_theme = "monokai"
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #121212;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #f57c00 !important;
            color: #fff !important;
            font-weight: 600;
            padding: 10px 24px;
            border-radius: 10px;
            transition: 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff9800 !important;
        }
        .stTextArea textarea {
            background-color: #2a2a2a !important;
            color: white !important;
        }
        h1, h2, h3, h4 {
            color: #ffffff !important;
        }
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

else:
    editor_theme = "chrome"
    st.markdown("""
        <style>
        body, .stApp {
            background: linear-gradient(180deg, #ffffff, #f7f9fc);
            color: #111111;
        }
        .stButton>button {
            background-color: #2196f3 !important;
            color: white !important;
            font-weight: bold;
            padding: 10px 24px;
            border-radius: 10px;
            transition: 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #1e88e5 !important;
        }
        h1, h2, h3, h4 {
            color: #0d47a1 !important;
        }
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

# -------------------- Title --------------------
st.title("TABL Compiler - Colorful Editor")

# -------------------- Editor + Table Viewer Layout --------------------
editor_col, table_col = st.columns([2, 1])

# -------------------- Editor --------------------
with editor_col:
    st.subheader("Write Your TABL Commands")

    code = st_ace(
        placeholder="Example:\nbana table students (id int primary key, naam varchar, roll int);\ndaal mein students value id = 1 aur naam = 'Lucky' aur roll = 100;\nnikal se students;",
        language="sql",
        theme=editor_theme,
        height=300,
        font_size=15,
        key="tabl_sql_editor"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Run Commands"):
            st.session_state.output = ""
            if code:
                commands = [cmd.strip() for cmd in code.strip().split(';') if cmd.strip()]
                for i, command in enumerate(commands, 1):
                    try:
                        tokens = tokenize(command)
                        ast = parse(tokens)
                        output = check_ast(ast)
                        st.session_state.output += f"[Command {i}] {output}\n"
                    except Exception as e:
                        st.session_state.output += f"[Command {i}]  Error: {str(e)}\n"
            else:
                st.warning(" Please enter some commands.")

    with col2:
        if st.button("Clear Output"):
            st.session_state.output = ""

# -------------------- Table Viewer --------------------
with table_col:
    st.subheader(" Table Viewer")
    db = get_database()
    if not db:
        st.info("No tables created yet.")
    else:
        selected_table = st.selectbox("Select Table", list(db.keys()))
        table = db[selected_table]

        if "schema" in table:
            columns = [col["name"] for col in table["schema"]]
            rows = table["rows"]
            if rows:
                df = pd.DataFrame(rows, columns=columns)
                st.dataframe(df, use_container_width=True)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"{selected_table}.csv",
                    mime="text/csv"
                )
            else:
                st.warning(" This table has no rows yet.")
        else:
            st.error("Invalid table format.")

# -------------------- Output Log --------------------
st.markdown("---")
st.subheader("Output Log")
st.code(st.session_state.output or "No output yet.", language='text')

import streamlit as st

st.set_page_config(page_title="How to Use TABL Compiler", layout="wide")
st.title("TABL Compiler - Command Reference Guide")

st.markdown("""
Welcome to **TABL Compiler**! This page shows all the Hinglish SQL commands you can use in this project — with simple syntax, explanations, and examples.
""")

# --------------------- 1. CREATE ----------------------
st.markdown("### 1. Create Table")
st.markdown("Define a new table with column names, types, and optional primary key.")
st.code("""
bana table students (id int primary key, naam varchar, rollno int)
bana table marks (sid int primary key, subject varchar, marks int)
""", language="sql")

# --------------------- 2. INSERT ----------------------
st.markdown("###  2. Insert Data")
st.markdown("Insert rows into tables using column=value syntax.")
st.code("""
students mein daal value id = 1 aur naam = 'Shobhit' aur rollno = 22
students mein daal value id = 2 aur naam = 'Ravi' aur rollno = 22
marks mein daal value sid = 2 aur subject = 'Math' aur marks = 91
""", language="sql")

# --------------------- 3. SELECT ----------------------
st.markdown("###  3. Select Data")
st.markdown("View data using SELECT (`nikal`) keyword.")

st.markdown("**All Columns**")
st.code("""
students se nikal
""", language="sql")

st.markdown("**Specific Columns**")
st.code("""
students se nikal naam, rollno
""", language="sql")

st.markdown("**With WHERE Clause (jaha)**")
st.code("""
students se nikal naam jaha rollno = 22
""", language="sql")

# --------------------- 4. GROUP BY ----------------------
st.markdown("### 4. Group Data (jodkar)")
st.markdown("Group records by a specific column.")
st.code("""
students se nikal rollno jodkar rollno
marks se nikal marks jodkar subject
""", language="sql")

# --------------------- 5. DELETE ----------------------
st.markdown("### 5. Delete Rows")
st.markdown("Remove records based on condition.")
st.code("""
mita students jaha naam = 'Lub'
mita marks jaha sid = 5
""", language="sql")

# --------------------- 6. UPDATE ----------------------
st.markdown("###  6. Update Data")
st.markdown("Change existing values using `badal` and `set kar`.")
st.code("""
badal students set kar rollno = 35 jaha naam = 'Shobhit'
badal marks set kar marks = 95 jaha sid = 1
""", language="sql")

# --------------------- 7. JOIN ----------------------
st.markdown("###  7. Join Tables")
st.markdown("Combine two tables using a common column.")
st.code("""
students jodo marks on id = sid
""", language="sql")

# --------------------- 8. LOOP ----------------------
st.markdown("###  8. Insert in Loops (baar)")
st.markdown("Insert rows multiple times for testing or automation.")
st.code("""
3 baar students mein daal value id = 100 aur naam = 'Dummy' aur rollno = 0
""", language="sql")

# --------------------- End ----------------------
st.markdown("""
---

This guide helps you understand all commands your TABL Compiler supports. Click "Launch Editor" from the sidebar to get started!

Feel free to copy & modify the examples.
""")

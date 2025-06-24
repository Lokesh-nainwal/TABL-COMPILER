import streamlit as st

# Set wide layout and page title
st.set_page_config(page_title="TABL Compiler", layout="wide")

# ---------------------- SIDEBAR ----------------------
with st.sidebar:
    st.markdown("## TABL Compiler Menu")

    st.markdown("#### 🔹 Navigation")
    if st.button("Launch Editor"):
        st.switch_page("pages/1_Editor.py")

    if st.button(" How It Works"):
        st.switch_page("pages/2_How_to_Use_.py")

    st.markdown("---")
    st.markdown("####  GitHub")
    st.markdown(
        "<div style='text-align:center'>"
        "<a href='https://github.com/' target='_blank'>"
        "<button style='background:#f57c00;color:white;padding:10px 20px;border:none;border-radius:8px;font-weight:bold;'>View on GitHub</button>"
        "</a>"
        "</div>",
        unsafe_allow_html=True
    )

# ---------------------- MAIN PAGE ----------------------
st.markdown("""
    <style>
    /* Base Layout */
    body, .main, .stApp {
        background-color: #eef2f7;
        font-family: 'Segoe UI', sans-serif;
        color: #111;
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #3f51b5, #1a237e);
        padding: 60px 30px;
        color: white;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 40px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }

    .hero-section h1 {
        font-size: 5rem;
        font-weight: 800;
        margin-bottom: 15px;
    }

    .hero-section p {
        font-size: 1.4rem;
        max-width: 800px;
        margin: auto;
        line-height: 1.6;
    }

    /* Features Section */
    .features-section {
        background-color: #ffffff;
        padding: 60px 40px;
        border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
    }

    .features-section h2 {
        text-align: center;
        color: #1a237e;
        font-size: 2rem;
        margin-bottom: 40px;
    }

    .features-grid {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 30px;
    }

    .feature-box {
        background: #f7f9fc;
        border-radius: 12px;
        padding: 30px;
        width: 280px;
        text-align: center;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }

    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
        background-color: #fff;
    }

    .feature-box h3 {
        font-size: 1.3rem;
        margin-bottom: 12px;
        color: #1a237e;
        font-weight: 600;
    }

    .feature-box p {
        font-size: 0.95rem;
        color: #333;
        line-height: 1.5;
    }

    /* Footer */
    .footer {
        background-color: #1a237e;
        color: white;
        padding: 25px;
        text-align: center;
        font-size: 14px;
        margin-top: 60px;
        border-radius: 8px;
    }

    /* Button Styling (Optional Streamlit Buttons) */
    .stButton>button {
        background-color: #f57c00 !important;
        color: white !important;
        font-size: 16px;
        font-weight: 600;
        padding: 10px 25px;
        border: none;
        border-radius: 8px;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #e65100 !important;
        transform: scale(1.02);
        cursor: pointer;
    }
</style>

""", unsafe_allow_html=True)

# 🟨 Feature Section
st.markdown("""
<div class="hero-section">
    <h1>TABL Compiler</h1>
    <p>Create and run Simple hindi-based SQL queries in your browser. No setup needed — just write, run, and see the result instantly.</p>
</div>
""", unsafe_allow_html=True)

# 🟨 Feature Section
st.markdown("""
<div class="features-section">
    <h2 style='text-align:center; color:#1a237e;'>Key Features</h2>
    <div class="features-grid">
        <div class="feature-box">
            <h3>No Installation</h3>
            <p>Use it directly in your browser. You don't have to download or install anything.</p>
        </div>
        <div class="feature-box">
            <h3>Write in Hinglish</h3>
            <p>Use simple mix-language commands like <code>bana table students</code> or <code>table mein daal</code> to work with data.</p>
        </div>
        <div class="feature-box">
            <h3>Run Many Commands</h3>
            <p>Write and run multiple commands at once, separated by semicolons. All results appear together.</p>
        </div>
        <div class="feature-box">
            <h3>Instant Table View</h3>
            <p>As soon as you insert data, you’ll see it displayed in an organized table on the screen.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 🔵 Footer
st.markdown("""
<div class="footer">
    &copy; 2025 TABL Compiler | Created by Lucky | Powered by Streamlit
</div>
""", unsafe_allow_html=True)

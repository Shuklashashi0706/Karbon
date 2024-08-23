import streamlit as st
import json
from model import probe_model_5l_profit

# Initialize session state for results
if 'result' not in st.session_state:
    st.session_state['result'] = None

def page1():
    st.title("📊 Financial Model Evaluation")

    st.header("📝 Page 1 - Upload Your JSON File")

    st.write("Welcome to the Financial Model Evaluator! 🎉 Please upload your JSON file containing financial data, and we'll process it for you.")

    uploaded_file = st.file_uploader("📂 Choose a JSON file", type="json")

    if uploaded_file is not None:
        st.success("File uploaded successfully! 🎉")
        data = json.load(uploaded_file)
        st.session_state['result'] = probe_model_5l_profit(data['data'])
        st.write("Data processed successfully. ✅")
        st.info("👉 Navigate to **Page 2 - Results** from the sidebar to view the analysis results.")

def page2():
    st.header("🔍 Page 2 - Results")

    if 'result' in st.session_state and st.session_state['result'] is not None:
        st.subheader("📈 Model Output:")
        st.write("Here are the analysis results based on your uploaded data:")
        result = st.session_state['result']

        for key, value in result["flags"].items():
            st.write(f"🔹 **{key}:** {value}")
    else:
        st.warning("⚠️ No results to display. Please upload and process a file on **Page 1 - Upload**.")

# Sidebar Navigation
page = st.sidebar.selectbox("🌐 Choose a page", ["Page 1 - Upload", "Page 2 - Results"])

if page == "Page 1 - Upload":
    page1()
elif page == "Page 2 - Results":
    page2()

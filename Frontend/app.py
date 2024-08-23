
import streamlit as st
import json

from model import probe_model_5l_profit



if 'result' not in st.session_state:
    st.session_state['result'] = None


def page1():
    st.title("Financial Model Evaluation")

    st.header("Page 1 - Upload JSON File")

    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        data = json.load(uploaded_file)

        result = probe_model_5l_profit(data['data'])

        st.session_state['result'] = result
        st.write("Data processed successfully.")
        st.write("Navigate to Page 2 to view the results.")


# Page 2 - Display Results
def page2():
    st.header("Page 2 - Results")

    if 'result' in st.session_state and st.session_state['result'] is not None:
        st.subheader("Model Output:")
        result = st.session_state['result']

        for key, value in result["flags"].items():
            st.write(f"{key}: {value}")
    else:
        st.write("No results to display. Please upload and process a file on Page 1.")


page = st.sidebar.selectbox("Choose a page", ["Page 1 - Upload", "Page 2 - Results"])

if page == "Page 1 - Upload":
    page1()
elif page == "Page 2 - Results":
    page2()

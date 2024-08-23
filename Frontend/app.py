import streamlit as st
import requests 
import json

# Streamlit App
st.title("Model Prediction Web App")

# Page 1 - Upload data
st.header("Page 1 - Upload Data")
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Display file details
    st.write("File uploaded successfully. You can now click Submit.")
    
    # Convert file to JSON
    file_data = json.load(uploaded_file)
    st.write(file_data)
    # On Submit button click
    if st.button("Submit"):
        # Send the file data to the Flask API
        response = requests.post("http://127.0.0.1:5000/predict", json={"data": file_data})
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            st.session_state['result'] = result
            st.write("Data submitted successfully.")
            st.write("Navigate to Page 2 to view the results.")
        else:
            st.write(f"Error: {response.json()}")


# Page 2 - Display Results
st.header("Page 2 - Results")

if 'result' in st.session_state:
    st.subheader("Model Output:")
    result = st.session_state['result']
    
    for key, value in result["flags"].items():
        st.write(f"{key}: {value}")
else:
    st.write("No results to display. Please upload a file on Page 1 and submit.")

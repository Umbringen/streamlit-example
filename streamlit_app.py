import streamlit as st
import os
import subprocess
import base64
import pandas as pd

import subprocess
subprocess.run(["pip", "install", "pandas"])

# Function to run the Python script
def run_script(uploaded_files):
    # Command to run your Python script
    command = ["python", "script.py"]  # Replace "your_script.py" with your actual script name
    
    # Add uploaded files as arguments to the command
    for file in uploaded_files:
        command.append(file.name)
    
    # Run the script
    subprocess.run(command)

# Function to save the output file
def save_output_file():
    output_file_path = "output_file.csv"  # Output file path
    st.write("Output File Path:", output_file_path)  # Debugging
    if os.path.exists(output_file_path):
        with open(output_file_path, "rb") as file:
            b64 = base64.b64encode(file.read()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="output_file.csv">Download Output File</a>'
            st.markdown(href, unsafe_allow_html=True)
    else:
        st.write("Output file not found.")

# Main function
def main():
    st.title("Python Script Runner")

    # File upload
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)

    if uploaded_files:
        st.write("Files uploaded:")
        for file in uploaded_files:
            st.write(file.name)

        # Button to run script
        if st.button("Run Script"):
            run_script(uploaded_files)
            st.write("Script executed successfully!")

            # Save output file
            save_output_file()

if __name__ == "__main__":
    main()

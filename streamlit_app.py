import streamlit as st
import pandas as pd
import os
import base64

# Function to concatenate uploaded files
def concatenate_files(uploaded_files):
    concatenated_df = pd.DataFrame()
    for file in uploaded_files:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
            concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
    return concatenated_df

# Function to save condensed file
def save_condensed_file(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="condensed_data.csv">Download Condensed File</a>'
    st.markdown(href, unsafe_allow_html=True)

# Main function
def main():
    st.title("Multiple Files Condenser")

    # File upload
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)

    if uploaded_files:
        st.write("Files uploaded:")
        for file in uploaded_files:
            st.write(file.name)

        # Button to process files
        if st.button("Condense Files"):
            condensed_df = concatenate_files(uploaded_files)
            st.write("Condensed DataFrame:")
            st.write(condensed_df)

            # Save condensed file
            save_condensed_file(condensed_df)

if __name__ == "__main__":
    main()

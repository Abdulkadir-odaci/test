import streamlit as st
import pandas as pd
import json
import io

def convert_json_to_csv(json_file):
    """
    Convert JSON file to CSV format
    """
    try:
        # Read JSON file
        json_data = json.load(json_file)
        
        # Handle both single object and list of objects
        if isinstance(json_data, dict):
            df = pd.json_normalize(json_data)
        else:
            df = pd.json_normalize(json_data)
            
        return df
    except Exception as e:
        st.error(f"Error converting file: {str(e)}")
        return None

# Set page config
st.set_page_config(page_title="JSON to CSV Converter", layout="wide")

# Add title and description
st.title("JSON to CSV Converter")
st.write("Upload a JSON file and convert it to CSV format")

# File uploader
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Add a spinner during conversion
    with st.spinner("Converting..."):
        # Convert JSON to DataFrame
        df = convert_json_to_csv(uploaded_file)
        
        if df is not None:
            # Show preview of the data
            st.subheader("Preview of converted data")
            st.dataframe(df.head())
            
            # Convert DataFrame to CSV
            csv = df.to_csv(index=False)
            
            # Create download button
            st.download_button(
                label="Download CSV file",
                data=csv,
                file_name="converted_file.csv",
                mime="text/csv"
            )
            
            # Show additional statistics
            st.subheader("File Statistics")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"Number of rows: {len(df)}")
            with col2:
                st.write(f"Number of columns: {len(df.columns)}")
            
            # Show column names
            st.subheader("Column Names")
            st.write(", ".join(df.columns))
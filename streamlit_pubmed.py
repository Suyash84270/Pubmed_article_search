
# streamlit_pubmed.py
import streamlit as st
import pandas as pd
from datetime import datetime
from pubmed_module import search_pubmed  # Import the search function

# App Title
st.title("PubMed Article Search")

# Input Fields
authors_input = st.text_input("Enter authors (comma-separated)", "")
topics_input = st.text_input("Enter topics (comma-separated)", "")
start_date = st.date_input("Start date", value=pd.to_datetime("2012-03-01"))
end_date = st.date_input("End date", value=pd.to_datetime("2022-12-31"))
retmax = st.number_input("Maximum number of results", min_value=1, value=50)

# Search Button
if st.button("Search PubMed"):
    # Process the input values
    authors = [a.strip() for a in authors_input.split(",") if a.strip()] if authors_input else []
    topics = [t.strip() for t in topics_input.split(",") if t.strip()] if topics_input else []
    
    # Convert date inputs (which are date objects) to datetime objects
    start_date_dt = datetime.combine(start_date, datetime.min.time())
    end_date_dt = datetime.combine(end_date, datetime.min.time())
    
    # Call the search function from your module
    df = search_pubmed(authors, topics, start_date_dt, end_date_dt, retmax=retmax)
    
    # Display the DataFrame
    st.write("Search Results:", df)
    
    # Convert DataFrame to CSV for download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download results as CSV",
        data=csv,
        file_name='PubMed_results.csv',
        mime='text/csv'
    )

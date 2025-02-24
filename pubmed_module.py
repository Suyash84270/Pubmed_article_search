# pubmed_module.py
import pandas as pd
from Bio import Entrez
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set email and API key for NCBI Entrez
Entrez.email = 'saikatsinha21@gmail.com'
Entrez.api_key = os.getenv('ENTREZ_API_KEY')

def search_pubmed(authors, topics, start_date, end_date, retmax=50):
    """
    Search PubMed for articles based on authors, topics, and publication date range.

    Parameters:
        authors (list): List of author names.
        topics (list): List of topics.
        start_date (datetime): Start date for search.
        end_date (datetime): End date for search.
        retmax (int): Maximum number of articles to fetch.

    Returns:
        DataFrame: A pandas DataFrame containing the search results.
    """
    # Build the date range string
    try:
        date_range = f'("{start_date.strftime("%Y/%m/%d")}"[Date - Create] : "{end_date.strftime("%Y/%m/%d")}"[Date - Create])'
    except Exception as e:
        logger.error("Error formatting dates: %s", e)
        raise

    # Build the query dynamically
    queries = []
    if authors:
        author_queries = [f'{author}[Author]' for author in authors]
        queries.append('(' + ' OR '.join(author_queries) + ')')
    if topics:
        topic_queries = [f'{topic}[Title/Abstract]' for topic in topics]
        queries.append('(' + ' OR '.join(topic_queries) + ')')
    
    full_query = (' AND '.join(queries) + ' AND ' + date_range) if queries else date_range
    logger.debug("Constructed query: %s", full_query)
    
    # Search PubMed
    try:
        handle = Entrez.esearch(db='pubmed', retmax=retmax, term=full_query)
        record = Entrez.read(handle)
        id_list = record.get('IdList', [])
        logger.info("Found %d articles.", len(id_list))
    except Exception as e:
        logger.error("Error during PubMed search: %s", e)
        raise

    # Prepare a DataFrame for results
    df = pd.DataFrame(columns=[
        'PubmedID', 'Title', 'Publication Date', 
        'Non-academic Author(s)', 'Company Affiliation(s)', 
        'Corresponding Author Email'
    ])
    
    month_mapping = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    
    # Process each article
    for pmid in id_list:
        try:
            handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
            records = Entrez.read(handle)
        except Exception as e:
            logger.error("Error fetching article with PMID %s: %s", pmid, e)
            continue
        
        for article in records.get('PubmedArticle', []):
            # Extract title
            try:
                title = article['MedlineCitation']['Article'].get('ArticleTitle', '')
            except Exception as e:
                logger.warning("Missing title for PMID %s: %s", pmid, e)
                title = ''
            
            # Extract publication date
            try:
                pub_date = article['MedlineCitation']['Article']['Journal']['JournalIssue'].get('PubDate', {})
                year = pub_date.get('Year', '')
                month = pub_date.get('Month', '')
                day = pub_date.get('Day', '')
                month = month_mapping.get(month, month)
                if year:
                    if month and day:
                        publication_date = f"{year}-{month}-{day}"
                    elif month:
                        publication_date = f"{year}-{month}-01"
                    else:
                        publication_date = f"{year}-01-01"
                else:
                    publication_date = ''
            except Exception as e:
                logger.error("Error extracting publication date for PMID %s: %s", pmid, e)
                publication_date = ''
            
            # Process author affiliations
            non_academic_authors = []
            company_affiliations = []
            corresponding_author_email = ''
            
            if 'AuthorList' in article['MedlineCitation']['Article']:
                for author in article['MedlineCitation']['Article']['AuthorList']:
                    full_name = ''
                    if 'LastName' in author and 'ForeName' in author:
                        full_name = f"{author['LastName']} {author['ForeName']}".strip()
                    
                    if 'AffiliationInfo' in author and author['AffiliationInfo']:
                        affiliation = author['AffiliationInfo'][0].get('Affiliation', '')
                        # Check for company affiliation indicators
                        if any(comp in affiliation.lower() for comp in ['pharma', 'biotech', 'inc', 'ltd', 'corp']):
                            company_affiliations.append(affiliation)
                        else:
                            if full_name:
                                non_academic_authors.append(full_name)
                        
                        # Check for email in the affiliation string
                        if '@' in affiliation and not corresponding_author_email:
                            for word in affiliation.split():
                                if '@' in word:
                                    corresponding_author_email = word.strip('.,;()')
                                    break
            
            non_academic_authors = ', '.join(set(non_academic_authors))
            company_affiliations = ', '.join(set(company_affiliations))
            
            new_row = {
                'PubmedID': pmid,
                'Title': title,
                'Publication Date': publication_date,
                'Non-academic Author(s)': non_academic_authors,
                'Company Affiliation(s)': company_affiliations,
                'Corresponding Author Email': corresponding_author_email
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    return df

if __name__ == '__main__':
    # For basic testing purposes only; in production, use a proper test suite.
    try:
        # Define test parameters
        test_authors = ['Smith', 'Doe']
        test_topics = ['cancer', 'therapy']
        test_start_date = datetime(2020, 1, 1)
        test_end_date = datetime(2020, 12, 31)
        result_df = search_pubmed(test_authors, test_topics, test_start_date, test_end_date, retmax=10)
        print(result_df)
    except Exception as e:
        logger.error("An error occurred during PubMed search: %s", e)

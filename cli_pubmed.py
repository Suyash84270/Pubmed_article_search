
# cli_pubmed.py
import argparse
from datetime import datetime
from pubmed_module import search_pubmed  # Import the search function from your module

def main():
    parser = argparse.ArgumentParser(description="Search PubMed articles.")
    parser.add_argument("--authors", type=str, help="Comma-separated list of authors", default="")
    parser.add_argument("--topics", type=str, help="Comma-separated list of topics", default="")
    parser.add_argument("--start_date", type=str, help="Start date in YYYY-MM-DD format", required=True)
    parser.add_argument("--end_date", type=str, help="End date in YYYY-MM-DD format", required=True)
    parser.add_argument("--output", type=str, help="Output CSV file name", default="PubMed_results.csv")
    parser.add_argument("--retmax", type=int, help="Maximum number of results to fetch", default=50)
    
    args = parser.parse_args()
    
    # Process input arguments
    authors = [a.strip() for a in args.authors.split(",") if a.strip()] if args.authors else []
    topics = [t.strip() for t in args.topics.split(",") if t.strip()] if args.topics else []
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
    
    # Perform the search
    df = search_pubmed(authors, topics, start_date, end_date, retmax=args.retmax)
    
    # Save the results to CSV
    df.to_csv(args.output, index=False)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()

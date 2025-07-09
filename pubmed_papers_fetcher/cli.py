# pubmed_papers_fetcher/cli.py

import argparse
from pubmed_papers_fetcher.fetcher import search_pubmed, fetch_details, save_to_csv


def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with pharma/biotech authors."
    )
    parser.add_argument(
        "query",
        type=str,
        help="PubMed query string."
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug output."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Output filename (CSV). If omitted, prints to console."
    )

    args = parser.parse_args()

    if args.debug:
        print(f"Searching PubMed for: {args.query}")

    ids = search_pubmed(args.query)
    if args.debug:
        print(f"Found IDs: {ids}")

    details = fetch_details(ids)
    if args.debug:
        print(f"Fetched details for {len(details)} papers.")

    save_to_csv(details, args.file)


if __name__ == "__main__":
    main()

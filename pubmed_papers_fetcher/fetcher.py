
from typing import List, Dict, Optional
import requests
import xml.etree.ElementTree as ET

import pandas as pd

PUBMED_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

COMPANY_KEYWORDS = [
    "pharma",
    "biotech",
    "laboratories",
    "inc",
    "ltd",
    "llc",
    "gmbh",
    "corp",
    "biopharma",
    "therapeutics",
    "biomedical",
    "healthcare",
    "company",
    "co."
]


def search_pubmed(query: str) -> List[str]:
    """Search PubMed for the query and return a list of PubMed IDs."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": "100",
        "retmode": "json"
    }
    resp = requests.get(PUBMED_ESEARCH_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["esearchresult"]["idlist"]


def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch details for each PubMed ID."""
    ids_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml"
    }
    resp = requests.get(PUBMED_EFETCH_URL, params=params)
    resp.raise_for_status()

    root = ET.fromstring(resp.content)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle") or "N/A"
        date = article.findtext(".//PubDate/Year") or "Unknown"

        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//AffiliationInfo/Affiliation")
            if affiliation:
                affil_lower = affiliation.lower()
                if any(kw in affil_lower for kw in COMPANY_KEYWORDS) and "university" not in affil_lower:
                    name_parts = []
                    if author.findtext("ForeName"):
                        name_parts.append(author.findtext("ForeName"))
                    if author.findtext("LastName"):
                        name_parts.append(author.findtext("LastName"))
                    name = " ".join(name_parts)
                    non_academic_authors.append(name)
                    company_affiliations.append(affiliation)

                    # Heuristic: check if there's an email
                    if "@" in affiliation and not corresponding_email:
                        corresponding_email = affiliation.split()[-1].strip()

        if non_academic_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": date,
                "Non-academicAuthor(s)": "; ".join(non_academic_authors),
                "CompanyAffiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email or "N/A"
            })

    return results


def save_to_csv(data: List[Dict], filename: Optional[str] = None) -> None:
    """Save the data to CSV."""
    df = pd.DataFrame(data)
    if filename:
        df.to_csv(filename, index=False)
    else:
        print(df.to_csv(index=False))

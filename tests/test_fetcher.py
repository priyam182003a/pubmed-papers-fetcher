# tests/test_fetcher.py

from pubmed_papers_fetcher.fetcher import search_pubmed, fetch_details

def test_search_pubmed():
    ids = search_pubmed("cancer")
    assert isinstance(ids, list)
    assert len(ids) > 0

def test_fetch_details():
    ids = search_pubmed("cancer")
    details = fetch_details(ids[:2])
    assert isinstance(details, list)
    assert len(details) > 0
    assert "PubmedID" in details[0]

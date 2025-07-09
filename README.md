📚 PubMed Papers Fetcher


This Python project fetches research papers from PubMed based on a user-specified query, filters papers that have at least one author affiliated with a pharmaceutical or biotech company, and saves the results to a CSV file.

It supports:

PubMed’s full query syntax

A flexible command-line interface

Debug logging and output to file or console

Typed Python, Poetry for packaging, and good code organization

📂 Project Structure

pubmed_papers_fetcher/
  __init__.py            # Makes this folder a Python module
  fetcher.py             # Core functions: search PubMed, fetch details, filter, save CSV
  cli.py                 # Command-line interface using argparse / typer
tests/
  test_fetcher.py        # Unit tests (example)
pyproject.toml           # Poetry dependency & build config
README.md                # This file

2️⃣ Install Poetry:
curl -sSL https://install.python-poetry.org | python3 -
Add it to your PATH if needed (Poetry will show instructions).

3️⃣ Install project dependencies:
poetry install


📌 Command Line Options
Option	Description
-h, --help	Show usage instructions.
-d, --debug	Print debug logs during execution.
-f, --file	Specify output filename for CSV export.



✅ How Non-Academic Authors Are Identified
The program uses simple heuristics:

An author’s affiliation must contain company-like keywords (e.g., pharma, biotech, inc, ltd, corp).

The affiliation must not contain "university" to filter out purely academic institutions.

Email addresses are extracted heuristically from the affiliation text if possible.




🔬 Tools & Libraries Used
Python 3.12+

Requests — HTTP calls to PubMed E-utilities API.

Pandas — easy CSV writing.

Poetry — dependency management & packaging.

Argparse or Typer — for the CLI.

✅ License
MIT — free to modify and distribute.

✅ LLM used: This project was developed with assistance from an AI Large Language Model (ChatGPT). Conversation-based suggestions were used to plan code structure, heuristics, and command-line usage.LINK : https://chatgpt.com/share/686e41c1-e614-8013-b5b4-5fbfac74516d

🚀 How to Run
Run the tool with your query:

poetry run get-papers-list "drug discovery" --debug --file new_results.csv


Example explanation:

"drug discovery" → your PubMed search query.

--debug → shows debug output: found IDs, filter info, etc.

--file new_results.csv → writes results to new_results.csv.



✅ How to Run Tests
To verify that everything works correctly, run:

poetry run pytest

This command will:

Run all test files in the tests/ folder.

Make sure the PubMed API returns valid results.

Check that the filtering and CSV logic work as expected.

You should see output like:

tests/test_fetcher.py ..   [100%]
2 passed in 3.5s

This confirms the code is working correctly!


👋 Author
Built as an example for research automation using PubMed + Python + LLM-assisted code planning.

Happy coding! 🔬✨

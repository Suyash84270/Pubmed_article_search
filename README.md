# 🔍 PubMed Article Search: Your Intelligent Research Assistant

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)


**Transform how you explore medical literature** – a powerful toolkit combining CLI efficiency with Streamlit's interactivity for precision PubMed searches. Developed by researchers, for researchers.



## 🚀 Features That Accelerate Discovery

### 📊 Smart Filter Matrix
- **Triple-Threat Filtering**  
  `Authors × Topics × Date Range` matrix for surgical precision.
- **Live PubMed API Integration**  
  Real-time access to 35M+ biomedical citations.
- **Export-Ready Analysis**  
  One-click CSV exports with full metadata preservation.

### ⚡ Dual Interface Power
```bash
# CLI for automated workflows
get-papers-list --topics "CRISPR COVID" --authors "Zhang, Doudna" --start_date 2020-01-01
```

<img src="https://github.com/user-attachments/assets/ee012491-daf2-4d08-a5c1-1d7ee7fcd51a" alt="Screenshot 2025-02-13 161704" width="500">
![Screenshot 2025-02-13 161631](https://github.com/user-attachments/assets/41dac1f9-c081-4f87-b903-300728d63482)

---

## 📁 Project Structure

```plaintext
pubmedsearch/
├── pubmed_module.py       # Core module with functions to search PubMed
├── streamlit_pubmed.py    # Streamlit web app for interactive article search
├── cli_pubmed.py          # CLI for fetching and exporting articles (registered as 'get-papers-list')
├── pyproject.toml         # Poetry configuration for dependency management and packaging
├── README.md              # Project documentation
├── LICENSE                # Project license (MIT)
└── .env                   # Environment variables (e.g., ENTREZ_API_KEY)
```

---

## 🛠 Tech Stack Deep Dive

| **Layer**          | **Technology**       | **Purpose**                           |
|--------------------|----------------------|---------------------------------------|
| **Data Fetch**     | BioPython Entrez     | PubMed API integration                |
| **Processing**     | Pandas               | Data structuring & transformation     |
| **Interface**      | Streamlit            | Interactive web dashboard             |
| **Packaging**      | Poetry               | Dependency management                 |
| **Execution**      | Click/Argparse       | CLI command crafting                  |

---

## ⚙️ Installation in 3 Minutes

1. **Get the Code**
   ```bash
   git clone https://github.com/Saikatsinha007/PubMed-Article-Search.git
   cd PubMed-Article-Search/pubmedsearch
   ```

2. **Setup with Poetry** *(Dependency Magic)*
   ```bash
   # Install Poetry (if not already installed)
   curl -sSL https://install.python-poetry.org | python3 -
   
   poetry install --no-dev  # Install production dependencies
   ```

3. **Configure API Key**  
   Create a `.env` file in the project root:
   ```ini
   ENTREZ_API_KEY=your_ncbi_key_here  # Get yours at https://www.ncbi.nlm.nih.gov
   ```

---

## 💻 Usage Scenarios

### Scenario 1: Rapid Literature Survey
```bash
poetry run get-papers-list \
  --start_date 2022-01-01 \
  --end_date 2023-12-31 \
  --topics "AI Drug Discovery" \
  --max_results 500 \
  --output breakthrough_drugs.csv
```

### Scenario 2: Competitive Analysis Dashboard
```python
# Example snippet from streamlit_pubmed.py
st.sidebar.date_input("Select Date Range", [])
st.sidebar.multiselect("Focus Areas", ["Immunotherapy", "Gene Editing"])
```

<img src="https://via.placeholder.com/600x200.png?text=Real-time+Search+Analytics" alt="Dashboard Mockup" width="600"/>

---

## 🤔 FAQ

**Q: How many results can I export?**  
A: The default is 50, configurable via the `--max_results` flag.

**Q: Can I search by institution?**  
A: The current version filters by author name. Institution-based filtering is planned for v2.1!

**Q: Is my API key stored securely?**  
A: Absolutely! The API key is stored locally in your `.env` file and never committed to version control.

---

## 🌟 What's Next? (Roadmap)

- [ ] PubMed Central full-text search integration
- [ ] Automated citation network graphs
- [ ] Journal impact factor filtering
- [ ] Collaborative filtering recommendations

**Help us build the future of research tools!** – See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 License & Attribution

**MIT Licensed** – Free for academic and commercial use.

**Standing on Giants' Shoulders:**
- [BioPython](https://biopython.org) for PubMed integration.
- [Streamlit](https://streamlit.io) for instant web interfaces.
- [Pandas](https://pandas.pydata.org) for robust data manipulation.

---

**Start your discovery journey today** – Because every great breakthrough begins with the right literature!

# Country Analyzer CLI

A Python command-line application that fetches country data from a public API, analyzes it, and allows users to explore statistics, search countries, and rank them by population.

---

## Features

-  Fetch country data from REST Countries API  
-  Global statistics (count, total, average population)  
-  Filter countries by region  
-  Search countries by name  
-  Top 10 most populated countries  
-  Save results to JSON files  

---

## Project Structure

```
country_analyzer_cli/
│
├── main.py        # CLI controller
├── api.py         # API requests
├── services.py    # data processing & logic
├── utils.py       # input & file handling
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TUO_USERNAME/country_analyzer_cli.git
cd country_analyzer_cli
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

---

## CLI Menu

```
=== COUNTRY ANALYZER ===
1. Global stats
2. Filter by region
3. Search country
4. Top 10 population
0. Exit
```

---

## Example Output

### Global stats

```json
{
  "count": 250,
  "total population": 7800000000,
  "avg_population": 31200000,
  "most_populated": {
    "name": "China",
    "population": 1400000000
  }
}
```

---

### Top 10 population

```
China --> 1400000000
India --> 1380000000
USA --> 330000000
...
```

---

## Output Files

The application automatically generates:

```
global_stats.json
europe_countries.json
search_italy.json
top_10_population.json
```

---

## API Used

- https://restcountries.com/v3.1

## Author

Lorenzo Massarelli

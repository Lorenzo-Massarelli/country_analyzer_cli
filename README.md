# Country Analyzer CLI

A Python CLI application that fetches country data from a public API, analyzes it, and allows users to explore statistics, search countries, and rank them by population.

---

## Architecture
- main.py → CLI controller (menu & flow)
- api.py → API requests
- services.py → data processing & logic
- utils.py → input & file handling
- requirements.txt
- README.md



## Features
- Fetch real-time country data from API
- Global statistics (count, total population, average, most populated)
- Filter countries by region
- Search countries by name
- Top 10 most populated countries
- Save results to JSON files



## How to run
1. Clone the repository
```bash
git clone https://github.com/your-username/country-analyzer.git
cd country-analyzer

2. Install dependencies
```bash
pip install -r requirements.txt

3.Run the application
```bash
python main.py



## Example
1.Global stats
{
  "count": 250,
  "total population": 7800000000,
  "avg_population": 31200000,
  "most_populated": {
    "name": "China",
    "population": 1400000000
  }
}

2.Top 10 population
China --> 1400000000
India --> 1380000000
USA --> 330000000
…

3.Output Files
global_stats.json
europe_countries.json
search_italy.json
top_10_population.json




## API Used
- https://restcountries.com/v3.1




## Author
Lorenzo Massarelli

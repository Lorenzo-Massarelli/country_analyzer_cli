from api import fetch_countries
from utils import get_input, save_json
from services import (normalize_countries, stats, filter_by_region, search_country, top_10_population)

def main():
    raw_data=fetch_countries()
    countries=normalize_countries(raw_data)
    
    while True:
        print("\n=== COUNTRY ANALYZER ===")
        print("1. Global stats")
        print("2. Filter by region")
        print("3. Search country")
        print("4. Top 10 population")
        print("0. Exit")
        
        choice = get_input("Choose option: ")
        
        if choice == "1":
            result = stats(countries)
            print(result)
            save_json(result, "global_stats.json")

        elif choice == "2":
            region = get_input("Region: ")
            filtered = filter_by_region(countries, region)
            result=stats(filtered)
            print(result)
            save_json(result, f"{region.lower()}_countries.json")
            
        elif choice == "3":
            name=get_input("Country name: ")
            result=search_country(countries, name)
            print(result)
            save_json(result, f"search_{name.lower()}.json")
            
        elif choice == "4":
            result=top_10_population(countries)
            for c in result:
                print(f"{c['name']} --> {c['population']}")
            save_json(result, "top_10_population.json")
            
        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
        
        
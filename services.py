def normalize_country(c):
    return {
        "name": c.get("name", {}).get("common"),
        "population": c.get("population", 0),
        "region": c.get("region"),
        "capital": c.get("capital", [None])[0] if c.get("capital") else None,
        "area": c.get("area", 0),
        "languages": list(c.get("languages", {}).values()),
        "currencies": list(c.get("currencies", {}).keys())
    }



def normalize_countries(data):
    return [normalize_country(c) for c in data]



def search_country(countries, name):
    return [ c for c in countries if c['name'] and name.lower() in c['name'].lower() ]



def most_populated(countries):
    return max(countries, key=lambda c: c["population"], default=None)



def filter_by_region(countries, region):
    return [ c for c in countries if c["region"] and c["region"].lower() == region.lower() ]



def top_10_population(countries):
    return sorted(countries, key=lambda c: c['population'], reverse=True)[:10]



def stats(countries):
    if not countries:
        return {"count": 0, "total population": 0, "avg_population": 0, "most_populated": None}
    
    total = sum(c["population"] for c in countries)
    
    return {
        "count": len(countries),
        "total population": total,
        "avg_population": total / len(countries),
        "most_populated": most_populated(countries)
    }
import requests

BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

def run_adql_query(query):
    params = {
        "query": query,
        "format": "json"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def get_exoplanets(limit=5):
    query = f"SELECT TOP {limit} pl_name, pl_orbper, pl_rade FROM pscomppars ORDER BY pl_name ASC"
    return run_adql_query(query)

def get_exoplanet_details(name):
    query = f"SELECT * FROM pscomppars WHERE pl_name = '{name}'"
    result = run_adql_query(query)
    return result[0] if result else None
 

from googlesearch import search

try:
    results = list(search("EcoVadis site:ecovadis.com", num_results=3))
    print("Results:", results)
except Exception as e:
    print("Search failed:", e)

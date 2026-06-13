# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ClientDesk
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query.strip(): return []
        q = query.lower()
        results = [item for item in self.data 
                   if any(q in str(v).lower() for v in item.values())]
        return sorted(results, key=lambda x: sum(1 for k,v in x.items() if isinstance(v,str) and q in v.lower()), reverse=True)

def add_search_to_main():
    # Append this class definition to the end of your main.py file
    pass

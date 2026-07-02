# === Stage 61: Add performance timing for core list and search operations ===
# Project: ClientDesk
import time
from datetime import timedelta

def _time_operation(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        print(f"[ClientDesk] {func.__name__} took {duration_ms:.2f}ms")
        return result
    wrapper.__name__ = func.__name__
    return wrapper

def benchmark_list_clients(clients, limit=5):
    ops = []
    for i in range(limit):
        start = time.perf_counter()
        filtered = [c for c in clients if 'active' in str(c).lower()]
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        ops.append({
            "iteration": i + 1,
            "duration_ms": round(duration_ms, 2),
            "items_found": len(filtered)
        })
    return ops

def benchmark_search_clients(clients, query):
    if not query:
        start = time.perf_counter()
        result = clients.copy()
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        return [{
            "query": "",
            "duration_ms": round(duration_ms, 2),
            "items_found": len(result)
        }]

    ops = []
    for i in range(3):
        start = time.perf_counter()
        filtered = [c for c in clients if query.lower() in str(c.get('name', '')).lower()]
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        ops.append({
            "iteration": i + 1,
            "duration_ms": round(duration_ms, 2),
            "items_found": len(filtered)
        })
    return ops

# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ClientDesk
from typing import Callable, TypeVar, Generic, List, Optional
T = TypeVar('T')

class SortableItem(Generic[T]):
    def __init__(self, title: str, date: datetime.date, priority: int, last_update: datetime.datetime):
        self.title = title
        self.date = date
        self.priority = priority
        self.last_update = last_update
    
    @property
    def sort_key(self) -> tuple[str, datetime.date, int, datetime.datetime]:
        return (self.title.lower(), self.date, -self.priority, self.last_update)

def get_sort_function(sort_by: str) -> Callable[[List[SortableItem[T]]], List[SortableItem[T]]]:
    if sort_by == 'title':
        return lambda x: sorted(x, key=lambda i: i.sort_key)
    elif sort_by == 'date':
        return lambda x: sorted(x, key=lambda i: (i.date, -i.priority))
    elif sort_by == 'priority':
        return lambda x: sorted(x, key=lambda i: (-i.priority, i.title.lower()))
    else:
        return lambda x: sorted(x, key=lambda i: i.sort_key)

def apply_sorting(items: List[SortableItem[T]], sort_by: str = 'title') -> List[SortableItem[T]]:
    if not items:
        return items
    try:
        from datetime import date, datetime
        # Ensure attributes are present and valid for sorting
        sorted_items = get_sort_function(sort_by)(items)
        return sorted_items
    except Exception as e:
        print(f"Sorting error: {e}")
        return items

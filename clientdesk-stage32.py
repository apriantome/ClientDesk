# === Stage 32: Add pagination helpers for long console output ===
# Project: ClientDesk
def paginate_output(lines, page_size=10):
    """Yields chunks of output lines for console pagination."""
    total_pages = (len(lines) + page_size - 1) // page_size if lines else 0
    current_page = 0
    while True:
        yield f"[Page {current_page + 1}/{total_pages}]"
        start = current_page * page_size
        end = min(start + page_size, len(lines))
        for line in lines[start:end]:
            print(line)
        if end >= len(lines):
            break
        current_page += 1

def clear_screen():
    """Clears terminal screen and moves cursor to top."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

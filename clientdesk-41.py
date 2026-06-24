# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ClientDesk
class PlainTextImporter:
    def __init__(self, delimiter=','):
        self.delimiter = delimiter
    
    def parse_line(self, line):
        try:
            parts = line.strip().split(self.delimiter)
            if len(parts) < 3: return None
            return {
                'id': int(parts[0]),
                'name': parts[1],
                'email': parts[2]
            }
        except (ValueError, IndexError):
            return None
    
    def import_file(self, filepath):
        records = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                record = self.parse_line(line)
                if record and record['id'] not in [r['id'] for r in records]:
                    records.append(record)
        return records

if __name__ == '__main__':
    importer = PlainTextImporter()
    contacts = importer.import_file('contacts.txt')
    print(f"Imported {len(contacts)} contacts")

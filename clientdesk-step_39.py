# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ClientDesk
def repair_data_integrity(db_path):
    with open(db_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line]
    
    contacts = {}
    meetings = []
    tasks = []
    history = []
    
    errors_fixed = 0
    
    for i, line in enumerate(lines):
        parts = line.split('|')
        
        try:
            if not parts or len(parts) < 2:
                continue
            
            entity_type = parts[0].lower()
            
            if entity_type == 'contact':
                name = parts[1]
                phone = parts[2] if len(parts) > 2 else ''
                
                if not name:
                    errors_fixed += 1
                    continue
                
                contacts[name] = {'phone': phone, 'notes': parts[3] if len(parts) > 3 else '', 'created_at': i}
            
            elif entity_type == 'meeting':
                client_name = parts[1]
                date_str = parts[2] if len(parts) > 2 else ''
                
                if not client_name:
                    errors_fixed += 1
                    continue
                
                meetings.append({'client': client_name, 'date': date_str, 'notes': parts[3] if len(parts) > 3 else '', 'created_at': i})
            
            elif entity_type == 'task':
                client_name = parts[1]
                description = parts[2] if len(parts) > 2 else ''
                
                if not client_name:
                    errors_fixed += 1
                    continue
                
                tasks.append({'client': client_name, 'description': description, 'status': parts[3] if len(parts) > 3 else 'pending', 'created_at': i})
            
            elif entity_type == 'history':
                date_str = parts[1]
                action = parts[2] if len(parts) > 2 else ''
                
                history.append({'date': date_str, 'action': action, 'notes': parts[3] if len(parts) > 3 else '', 'created_at': i})
        
        except Exception:
            errors_fixed += 1
    
    with open(db_path, 'w', encoding='utf-8') as f:
        for name, data in sorted(contacts.items()):
            f.write(f"contact|{name}|{data['phone']}|{data['notes']}\n")
        
        for meeting in meetings:
            f.write(f"meeting|{meeting['client']}|{meeting['date']}|{meeting['notes']}\n")
        
        for task in tasks:
            f.write(f"task|{task['client']}|{task['description']}|{task['status']}\n")
        
        for entry in history:
            f.write(f"history|{entry['date']}|{entry['action']}|{entry['notes']}\n")
    
    return errors_fixed

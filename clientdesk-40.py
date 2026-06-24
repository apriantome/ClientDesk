# === Stage 40: Add plain text report export ===
# Project: ClientDesk
def export_report_to_txt(self, report_data):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for section in ["contacts", "meetings", "tasks", "history"]:
            if section in report_data and report_data[section]:
                f.write(f"\n=== {section.upper()} ===\n")
                for item in report_data[section]:
                    line = "\t".join(str(v) for v in item.values())
                    f.write(line + "\n")
        f.write("\n--- End of Report ---\n")

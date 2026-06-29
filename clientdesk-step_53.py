# === Stage 53: Add command help text and usage examples ===
# Project: ClientDesk
HELP_TEXT = """ClientDesk v1.0 - Lightweight Client Follow-up System
Usage: python clientdesk.py <command> [options]
Commands:
  init          Initialize project files and database schema
  contacts      List all registered clients (c) or add new ones (a)
  meetings      View upcoming appointments (m) or schedule new ones (s)
  tasks         Manage follow-up tasks for specific clients (t)
  history       Show interaction logs with a client (h)
  stats         Display summary statistics on active clients and tasks (x)
Options:
  -f, --file    Specify custom database file path (default: data.db)
  -v, --verbose Enable detailed logging output
Examples:
  python clientdesk.py contacts add --name "Acme Corp" --email "contact@acme.com"
  python clientdesk.py meetings s --client "Acme Corp" --date "2023-12-01" --time "14:00"
  python clientdesk.py tasks t --client "Acme Corp" --task "Send invoice" --due "tomorrow"
  python clientdesk.py history h --client "Acme Corp"
"""

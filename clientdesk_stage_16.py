# === Stage 16: Add argparse support for the most common commands ===
# Project: ClientDesk
import argparse

def main():
    parser = argparse.ArgumentParser(description="ClientDesk: Lightweight client follow-up system")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Contacts command
    contacts_parser = subparsers.add_parser('contacts', help='Manage contacts')
    contacts_parser.set_defaults(func=contacts_handler)
    contacts_add = contacts_parser.add_parser('add', parents=[_common_args()])
    contacts_del = contacts_parser.add_parser('del', parents=[_common_args()])

    # Meetings command
    meetings_parser = subparsers.add_parser('meetings', help='Manage meetings')
    meetings_parser.set_defaults(func=meetings_handler)
    meetings_add = meetings_parser.add_parser('add', parents=[_common_args()])
    meetings_del = meetings_parser.add_parser('del', parents=[_common_args()])

    # Tasks command
    tasks_parser = subparsers.add_parser('tasks', help='Manage tasks')
    tasks_parser.set_defaults(func=tasks_handler)
    tasks_add = tasks_parser.add_parser('add', parents=[_common_args()])
    tasks_del = tasks_parser.add_parser('del', parents=[_common_args()])

    # History command
    history_parser = subparsers.add_parser('history', help='View interaction history')
    history_parser.set_defaults(func=history_handler)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        return 1
    return args.func(**vars(args))

def _common_args():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--name', required=True, help='Entity name')
    p.add_argument('--desc', default='', help='Description')
    p.add_argument('--date', default=None, help='Date (YYYY-MM-DD)')
    return p

def contacts_handler(**kwargs): pass
def meetings_handler(**kwargs): pass
def tasks_handler(**kwargs): pass
def history_handler(**kwargs): pass

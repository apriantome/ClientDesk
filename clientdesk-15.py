# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ClientDesk
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        if not text.strip(): return None
        parts = text.split(maxsplit=1)
        cmd = parts[0]
        args = parts[1].strip() if len(parts) > 1 else ""
        handler = self.handlers.get(cmd)
        if handler:
            try:
                result = handler(args)
                return f"OK: {result}" if isinstance(result, str) else "OK"
            except Exception as e:
                return f"ERROR: {e}"
        return None

    def register(self, cmd, handler):
        self.handlers[cmd.lower()] = handler

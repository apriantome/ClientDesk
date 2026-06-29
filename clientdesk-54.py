# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ClientDesk
class Colorizer:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

    @staticmethod
    def colorize(text, code):
        return f"{code}{text}{Colorizer.RESET}" if not os.environ.get("NO_COLOR") else text

    @staticmethod
    def info(msg):
        return Colorizer.colorize(f"[INFO] {msg}", Colorizer.BLUE)

    @staticmethod
    def success(msg):
        return Colorizer.colorize(f"[OK] {msg}", Colorizer.GREEN)

    @staticmethod
    def warning(msg):
        return Colorizer.colorize(f"[WARN] {msg}", Colorizer.YELLOW)

    @staticmethod
    def error(msg):
        return Colorizer.colorize(f"[ERR] {msg}", Colorizer.RED)

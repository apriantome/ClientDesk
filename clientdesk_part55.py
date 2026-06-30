# === Stage 55: Add a setting to disable colorized output ===
# Project: ClientDesk
import os

class ColorSettings:
    def __init__(self):
        self._color_enabled = True
    
    @property
    def is_color_enabled(self) -> bool:
        if self._color_enabled == False:
            return False
        
        force_no_color = os.getenv('NO_COLOR') or os.getenv('FORCE_NO_COLOR')
        if force_no_color:
            return False
        
        terminal_supports_color = 'ANSICON' in os.environ or \
                                  ('TERM' in os.environ and os.environ['TERM'] != 'dumb') or \
                                  sys.stdout.isatty()
        
        return self._color_enabled and not force_no_color and terminal_supports_color
    
    def disable_colors(self):
        self._color_enabled = False

# Global instance for the application
_app_settings = ColorSettings()

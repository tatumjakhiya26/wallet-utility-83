import logging
import sys
from pathlib import Path
from typing import Optional

class WalletLogger:
    """Configures logging for wallet operations with fallback error handling."""
    
    def __init__(self, log_file: Optional[str] = "wallet.log", level: int = logging.INFO):
        self.logger = logging.getLogger("wallet_utility")
        self.logger.setLevel(level)
        self.logger.handlers.clear()
        
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Default console logging stream
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        if log_file:
            self._setup_file_handler(log_file, formatter)

    def _setup_file_handler(self, log_file: str, formatter: logging.Formatter) -> None:
        """Sets up file logging while catching file system permission and path errors."""
        try:
            path = Path(log_file).resolve()
            path.parent.mkdir(parents=True, exist_ok=True)
            
            file_handler = logging.FileHandler(path, encoding='utf-8', delay=True)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except (PermissionError, OSError, ValueError) as err:
            # Edge case handling: invalid paths or permission denied defaults gracefully to console
            self.logger.warning(f"File logging disabled for '{log_file}': {err}")

    def log_safe(self, level: int, msg: str, *args, **kwargs) -> None:
        """Safely logs strings with fallback encoding for unexpected raw byte data."""
        try:
            clean_msg = str(msg).encode('utf-8', errors='replace').decode('utf-8')
            self.logger.log(level, clean_msg, *args, **kwargs)
        except Exception as err:
            sys.stderr.write(f"Unrecoverable logging exception: {err}\n")

    def get_logger() -> logging.Logger:
        return self.logger
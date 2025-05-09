import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, name=__name__, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Prevent duplicate handlers if logger already initialized
        if not self.logger.handlers:
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)

            log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

            file_handler = logging.FileHandler(log_filename)
            console_handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

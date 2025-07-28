import logging
import os
from datetime import datetime

# Set logs_path to project root, not current working directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_path = os.path.join(project_root, "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_file_path = os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

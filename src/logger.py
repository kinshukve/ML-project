import logging
import os
from datetime import datetime

# 1. Create the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the directory path where logs will be stored
logs_dir_path = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' directory if it doesn't already exist
os.makedirs(logs_dir_path, exist_ok=True)

# 4. Join the directory path and the file name to get the full file path
LOG_FILE_PATH = os.path.join(logs_dir_path, LOG_FILE)

# 5. Configure the logging behavior
logging.basicConfig(
    filename=LOG_FILE_PATH,
    # Standard format: [ Timestamp ] LineNumber LoggerName - LogLevel - Message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Optional: A quick test to verify it works
if __name__ == "__main__":
    logging.info("Logging has started successfully.")
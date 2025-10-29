# logger_setup.py
import logging
import os

LOG_FILE = os.path.join(os.getcwd(), "test_log.log")

# configure logging immediately, before pytest imports any test modules
logging.basicConfig(
    filename=LOG_FILE,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("==== Test Session Started ====")

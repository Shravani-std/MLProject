"""
Logging : provides flexible way to record events(logs) in py programs

          instead of using print() use logging so we can control:
            Levels (debug, info, warning, error, critical).
            Destinations (console, file, syslog, email, etc.).
            Format (timestamps, module names, messages, etc.).
            Propagation (logs flow from child loggers → parent loggers → root logger)."""



# Example
"""
import logging

# configure root logger
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# Module-level logger
logger = logging.getLogger(__name__)

def run():
    logger.info("Program Started")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Something went wrong!")
    logger.info("Program Finished")

run()

Output: 
2025-09-06 09:00:00 [INFO] __main__: Program started
2025-09-06 09:00:00 [ERROR] __main__: Something went wrong!
Traceback (most recent call last):
  File "app.py", line 12, in run
    1 / 0
ZeroDivisionError: division by zero
2025-09-06 09:00:00 [INFO] __main__: Program finished

"""
# my_logging.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("MyApp")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")

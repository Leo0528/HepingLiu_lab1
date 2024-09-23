import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logger level

# Create handlers
c_handler = logging.StreamHandler()  # Console handler
f_handler = logging.FileHandler('file.log')  # File handler

# Set levels for handlers
c_handler.setLevel(logging.WARNING)  # Only log WARNING and above to console
f_handler.setLevel(logging.ERROR)  # Only log ERROR and above to file

# Create formatters
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set formatters to handlers
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Log messages
logger.warning('This is a warning')
logger.error('This is an error')




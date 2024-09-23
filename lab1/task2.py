import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#level = logging.INFO, it means 
logging.info('Admin logged in')

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt = '%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')
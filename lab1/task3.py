import logging

name = 'John'
logging.error(f'{name} raised an error')
#f-string

a = 5
b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception occured", exc_infno=True)

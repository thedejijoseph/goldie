import cv2
import sys
import json
from datetime import datetime
import ast
import os

from dotenv import load_dotenv
load_dotenv()
LOG_FILE = os.getenv('LOG_FILE_PATH')


def send_to_console(level, message, data):
    categories_to_ignore = ast.literal_eval(os.getenv('LOG_CATEGORIES_TO_IGNORE'))
    if data['cat'] not in categories_to_ignore:
        print('[{0}]'.format(datetime.now()), level + ':', message, json.dumps(data))

def send_to_file(filename, level, message, data):
    with open(filename, 'w') as log_file:
        categories_to_ignore = ast.literal_eval(os.getenv('LOG_CATEGORIES_TO_IGNORE'))
        if data['cat'] not in categories_to_ignore:
            log = f'{datetime.now()} {level}: {message} {json.dumps(data)}\n'
            log_file.write(log)

def send_to_sqs():
    pass

def log_error(message, data):
    send_to_console('ERROR', message, data)
    sys.exit(0)

def log_info(message, data):
    send_to_console('INFO', message, data)
    send_to_file(LOG_FILE, 'INFO', message, data)

def log_debug(message, data):
    send_to_console('DEBUG', message, data)
"""start the slack connector"""
from src.slack_info import start

try:
    start()
except Exception as e:
       raise e
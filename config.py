from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

"""
**************************************************
Class: Config

get all the enviromental variables
assign Constant variables for better usage in the
app.
**************************************************
"""

class Config(object):
     # set path to env file
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY")
    TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

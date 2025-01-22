""" calling the function user_list and conversation_list"""

from src import connector_info
from configparser import ConfigParser


def start():
    """
    args: none
    returns : response 
    """
    config = ConfigParser()
    config.read('config/connector_config.cfg')

    BASE_URL = config['baseUrl']['base_url']
    FILESLIST_ENDPOINT = config['endpoints']['files_list']
    USERINFO_ENDPOINT = config['endpoints']['users_info']
    API_KEY = config['credentials']['api_key']

    connector_info.conversation_list(BASE_URL,FILESLIST_ENDPOINT,API_KEY)
    connector_info.user_list(BASE_URL,USERINFO_ENDPOINT,API_KEY)



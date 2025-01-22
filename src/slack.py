import logging
import requests
import json
# Configure logging
logging.basicConfig(level=logging.INFO, filename="slack.log",filemode="w")

class SlackAPI:
    def __init__(self):
        """
        Initialize the SlackAPI with the given token."""
        self.base_url = "https://slack.com/api/"
        self.token = "token"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    # def usergroups_list(self):
    #     """
    #     Fetches the list of user groups in the Slack workspace and logs it to 'slack.log'.
    #     """
    #     endpoint = "usergroups.list"
    #     url = f"{self.base_url}{endpoint}"
    #     try:
    #         logging.info("Fetching user groups...")
    #         response = requests.get(url, headers=self.headers)
    #         response.raise_for_status()
    #         data = response.json()
    #         if not data.get("ok"):
    #             logging.error(f"Error fetching user groups: {data.get('error')}")
    #             return
    #         pretty_data = json.dumps(data, indent=4)
    #         logging.info(f"User Groups Data:\n{pretty_data}")
    #     except requests.exceptions.RequestException as e:
    #         logging.error(f"HTTP Request failed: {e}")
    def files_list(self):
        """Fetches the list of files in the Slack workspace"""
        endpoint = "files.list"
        url = f"{self.base_url}{endpoint}"
        try:
            logging.info("Fetching files list...")
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching files list: {data.get('error')}")
                return
            pretty_data = json.dumps(data, indent=4)
            logging.info(f"Files List Data:\n{pretty_data}")
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")

        

    def get_users_list(self):
        """ function to get users list

        """
        endpoint = f"{self.base_url}/users.list"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching users list: {data.get('error')}")
                return None
            logging.info("Successfully fetched users list.")
            #logging.info(data.get("members", []))
            pretty_data=json.dumps(data,indent=4)
            logging.info(f'Json data = {pretty_data}')
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None
    

    def users_info(self, user_id):
        """
        Fetches information about a specific user and logs it to 'slack.log'.
        """
        endpoint = "users.info"
        url = f"{self.base_url}{endpoint}"
        params = {"user": user_id}
        try:
            logging.info(f"Fetching information for user ID: {user_id}")
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching user info: {data.get('error')}")
                return None
            pretty_data = json.dumps(data, indent=4)
            logging.info(f"User Info for {user_id}:\n{pretty_data}")
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")

a=SlackAPI ()
#a.usergroups_list()
a.get_users_list()  
a.users_info("USLACKBOT")
a.users_info("U08996D78D7")
a.files_list()
        
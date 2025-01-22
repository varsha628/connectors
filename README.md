# connectors
# Test Connector

connectors created for training purpose

# Functionalities 

- Fetch files list from Workspace 
- Fetch user info from workspace 

# Installations

### Packages 
```shell
pip install -r requirements.txt
```
# Configurations

### Logging Configurations

LOG_LEVEL = DEBUG
LOG_FILE_NAME = slack.log

# Run unit test cases 

To run unittest cases `pytest` module is required 

To execute unit test cases for slack Connector, perform following steps:

1. Create a virtual environment
2. Enable virtual environment
3. Install required libraries from `requirements.txt`.
4. Execute `pytest`

# To start connector
steps:
1. create a virtual env and activate it
2. install the required modules/packages
3. add required functions and test cases
4. install pre-commit: pip install pre-commit
5. activate it: pre-commit install
6. Add the changes to git
7. commit the changes 
8. pre-commit autoupdate


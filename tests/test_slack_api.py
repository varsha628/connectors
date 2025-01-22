from src.slack import SlackAPI, a
from unittest.mock import patch
import requests
from typing import Any
import pytest


def test_invalid_token():
    """Test for invalid Slack API token"""
    slack_api = SlackAPI()
    response = slack_api.files_list()
    assert response is None, "Expected None for invalid token."

def test_network_error():
    """Test for network error during API call"""
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError
        slack_api = SlackAPI()
        response = slack_api.files_list()
        assert response is None, "Expected None for a network error."


def test_empty_token():
    """Test for empty Slack API token."""
    slack_api = SlackAPI()
    response = slack_api.files_list()
    assert response is None, "Expected None for empty token."



 




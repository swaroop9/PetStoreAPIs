import requests
from utils.configuration import *

# Base URL
baseUrl = getConfig()['API']['baseUrl']

# params
params = payload()['login']


def test_logIn_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user/login"

    # Make API request
    response = requests.request("GET", url, params=params)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert "logged in user session" in resp_body['message']


def test_logOut_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user/logout"

    # Make API request
    response = requests.request("GET", url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == 'ok'

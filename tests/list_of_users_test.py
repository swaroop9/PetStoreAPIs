import requests
from utils.configuration import *

# Base URL
baseUrl = getConfig()['API']['baseUrl']

# Body
list_of_users_payload = json.dumps(payload()['listPayload'])

# Additional headers.
headers = {
    'Content-Type': 'application/json'
}


def test_create_users_with_array():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user/createWithArray"

    # Make API request
    response = requests.request("POST", url, headers=headers, data=list_of_users_payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == 'ok'


def test_create_users_with_list():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user/createWithList"

    # Make API request
    response = requests.request("POST", url, headers=headers, data=list_of_users_payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == 'ok'

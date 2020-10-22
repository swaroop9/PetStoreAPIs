import requests
from utils.configuration import *

# Base URL
baseUrl = getConfig()['API']['baseUrl']

# Body
create_payload = json.dumps(payload()['createPayload'])
update_payload = json.dumps(payload()['updatePayload'])

# Additional headers.
headers = {
    'Content-Type': 'application/json'
}


def test_create_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user"

    # Make API request
    response = requests.request("POST", url, headers=headers, data=create_payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == str(json.loads(create_payload)['id'])


def test_get_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user" + "/Poornas"

    # Make API request
    response = requests.request("GET", url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['id'] == json.loads(create_payload)['id']
    assert resp_body['username'] == json.loads(create_payload)['username']


def test_update_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user" + "/Poornas"

    # Make API request
    response = requests.request("PUT", url, headers=headers, data=update_payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == str(json.loads(update_payload)['id'])


def test_delete_user():
    # Create URL with the end point "/user" to Create user
    url = baseUrl + "/user" + "/Poornas"

    # Make API request
    response = requests.request("DELETE", url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['message'] == json.loads(create_payload)['username']

import json

from src.utilities.requestUtilities import RequestsUtilities
import pytest

ru = RequestsUtilities()

#test case for get
@pytest.mark.API
@pytest.mark.GET_API
def test_get_api_for_single_user():
    endpoint = 'api/users/2'
    get_rs = ru.get(endpoint, expected_status_code=200)
    assert get_rs['data']['id'] == 2 , f"Expected Response '2' Actual Response {get_rs['data']['id']}"
    assert get_rs['data']['email'] is not None, f"Expected Response not None Actual Response {get_rs['data']['email']}"


#test case for Post
@pytest.mark.API
@pytest.mark.Post_API
def test_add_user_details():
    endpoint = 'api/users'
    payload = {"name": "morpheus","job": "leader"}
    payloads = json.dumps(payload)
    post_rs = ru.post(endpoint, payloads, expected_status_code=201)
    assert post_rs['name'] == payload['name'] , f"Expected Response {payload['name']} Actual Response {post_rs['name'] }"
    assert post_rs['job'] == payload['job'], f"Expected Response {payload['job']} Actual Response {post_rs['job']}"


#test case for PUT
@pytest.mark.API
@pytest.mark.PUT_API
def test_update_user_details():
    endpoint = 'api/users/2'
    payload = {"name": "Demo","job": "associate"}
    put_rs = ru.put(endpoint, payload, expected_status_code=200)
    assert put_rs['name'] == payload['name'] , f"Expected Response {payload['name']} Actual Response {put_rs['name'] }"
    assert put_rs['job'] == payload['job'], f"Expected Response {payload['job']} Actual Response {put_rs['job']}"


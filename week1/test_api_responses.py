import pytest
import requests

@pytest.fixture()
def local_setup_teardown():
    print("Executing setup from 'local_setup_teardown' fixture from local file")
    yield
    print("Executing teardown from 'local_setup_teardown' fixture from local file")

@pytest.fixture()
def name_shadowing_fixture():
    print("Executing setup from 'name_shadowing_fixture' fixture from local file")
    yield
    print("Executing teardown from 'name_shadowing_fixture' fixture from local file")

@pytest.mark.postman
def test_post_api_call(global_setup_teardown, local_setup_teardown):
    url = "https://postman-echo.com/post"
    data = {"id": 1,
            "data": "new data",
            "list_data":["l1", "l2"]}
    print(f"Creating object {data=}")
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json().get("json").get("list_data") == ["l1", "l2"]
    assert 'application/json' in response.headers['Content-Type']
    assert response.elapsed.microseconds / 1000 < 1000

@pytest.mark.postman
def test_put_api_call(name_shadowing_fixture):
    url = "https://postman-echo.com/put"
    raw_txt = "Response text expected"
    response = requests.put(url, data=raw_txt)
    assert response.status_code == 200
    assert response.json().get("data") == raw_txt
    assert 'application/json' in response.headers['Content-Type']
    assert response.elapsed.microseconds / 1000 < 1000

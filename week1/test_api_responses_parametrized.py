import pytest, requests, json


def get_params():
    with open("configs/config.json") as f:
        data = json.load(f)
    params = {k:v["content_type"] for k, v in data["urls"].items()}
    return list(params.items())

params = get_params()

@pytest.mark.parametrize("url, content_type", params)
@pytest.mark.postman
@pytest.mark.parametrized
def test_get_api_call(url, content_type):
    response = requests.get(url)
    assert response.status_code == 200
    assert content_type in response.headers['Content-Type']
    el_tm = response.elapsed.microseconds / 1000
    assert el_tm < 1000, f"Slow response: {el_tm} ms"

@pytest.mark.postman
@pytest.mark.skip(reason="duplicated test")
def test_post_api_call():
    url = "https://postman-echo.com/post"
    data = {"id": 1, "data": "new data", "list_data":["l1", "l2"]}
    response = requests.post(url, data=data)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data.get("json").get("list_data") == ["l1", "l2"]
    assert 'application/json' in response.headers['Content-Type']
    el_tm = response.elapsed.microseconds / 1000
    assert el_tm < 1000, f"Slow response: {el_tm} ms"

@pytest.mark.postman
@pytest.mark.skip(reason="duplicated test")
def test_put_api_call():
    url = "https://postman-echo.com/put"
    raw_response_txt = "Response text expected"
    response = requests.put(url, data=raw_response_txt)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data.get("data") == raw_response_txt
    assert 'application/json' in response.headers['Content-Type']
    el_tm = response.elapsed.microseconds / 1000
    assert el_tm < 1000, f"Slow response: {el_tm} ms"

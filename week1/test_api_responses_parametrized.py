import pytest
import requests

@pytest.mark.parametrize("content_type, url",
                         [('application/json', "https://api.github.com"),
                            ('text/html', "https://jsonplaceholder.typicode.com"),
                            ('application/json', "https://dog.ceo/api/breeds/image/random"),
                            ('text/html', "https://w3schools.com/python/demopage.htm"),
                            ('text/html', "https://postman-echo.com/")])

@pytest.mark.postman
@pytest.mark.parametrized
def test_get_api_call(content_type, url):
    response = requests.get(url)
    assert response.status_code == 200
    assert content_type in response.headers['Content-Type']
    assert response.elapsed.microseconds / 1000 < 1000

@pytest.mark.postman
@pytest.mark.skip
def test_post_api_call():
    url = "https://postman-echo.com/post"
    data = {"id": 1, "data": "new data", "list_data":["l1", "l2"]}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json().get("json").get("list_data") == ["l1", "l2"]
    assert 'application/json' in response.headers['Content-Type']
    assert response.elapsed.microseconds / 1000 < 1000

@pytest.mark.postman
@pytest.mark.skip
def test_put_api_call():
    url = "https://postman-echo.com/put"
    raw_response_txt = "Response text expected"
    response = requests.put(url, data=raw_response_txt)
    assert response.status_code == 200
    assert response.json().get("data") == raw_response_txt
    assert 'application/json' in response.headers['Content-Type']
    assert response.elapsed.microseconds / 1000 < 1000

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


@pytest.fixture()
def data_load():
    data = {"id": 1,
            "data": "new data",
            "list_data": ["l1", "l2"]}
    return data

@pytest.fixture(params=["raw data 1", "raw data 2", "raw data 3"])
def get_raw_data(request):
    return request.param

@pytest.mark.usefixtures("class_setup_teardown")
class TestPostmanApi:

    @pytest.mark.postman
    def test_post_api_call(self, global_setup_teardown ,local_setup_teardown, data_load):
        url = "https://postman-echo.com/post"
        print(f"Creating object {data_load=}")
        response = requests.post(url, data=data_load)
        assert response.status_code == 200
        assert response.json().get("json").get("list_data") == ["l1", "l2"]
        assert 'application/json' in response.headers['Content-Type']
        el_tm = response.elapsed.microseconds / 1000
        assert el_tm < 1000, f"Slow response: {el_tm} ms"

    @pytest.mark.postman
    def test_put_api_call(self, name_shadowing_fixture, get_raw_data):
        url = "https://postman-echo.com/put"
        response = requests.put(url, data=get_raw_data)
        assert response.status_code == 200
        assert response.json().get("data") == get_raw_data
        assert 'application/json' in response.headers['Content-Type']
        el_tm = response.elapsed.microseconds / 1000
        assert el_tm < 1000, f"Slow response: {el_tm} ms"

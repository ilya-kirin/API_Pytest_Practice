import pytest

@pytest.fixture()
def global_setup_teardown():
    print("Executing setup from 'global_setup_teardown' fixture from conftest file")
    yield
    print("Executing teardown from 'global_setup_teardown' fixture from conftest file")

@pytest.fixture()
def name_shadowing_fixture():
    print("Executing setup from 'name_shadowing_fixture' fixture from conftest file")
    yield
    print("Executing teardown from 'name_shadowing_fixture' fixture from conftest file")
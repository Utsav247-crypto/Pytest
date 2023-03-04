import pytest

@pytest.fixture(scope='function',autouse=True)
def setup():
    print('login browser')
    yield
    print('close browser')

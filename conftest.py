import pytest
from slack_sdk import WebClient

@pytest.fixture(scope='function',autouse=True)
def setup():
    print('login browser')
    yield
    print('close browser')

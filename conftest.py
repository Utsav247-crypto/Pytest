import pytest
from slack_sdk import WebClient

@pytest.fixture(scope='function',autouse=True)
def setup():
    print('login browser')
    yield
    print('close browser')

def pytest_terminal_summary(terminalreporter):
    print(terminalreporter.config)
    if not hasattr(terminalreporter.config, 'workerinput'):
        client = WebClient(token='xoxb-4891217860754-4891249655875-8Id1BqTvJY1mQGzuK2uppTQE')
        client.chat_postMessage(channel="automation",text="My File")

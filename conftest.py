@pytest.fixture(autouse=True)
def setup():
    print('login browser')
    yield
    print('close browser')

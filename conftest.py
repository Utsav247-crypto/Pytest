import pytest
@pytest.fixture(scope='function',autouse=True)
def setup(request):
    print('login browser')
    session = request.node
    html = request.config._html
    report_content = html._generate_report(session)
    html._save_report(report_content)
    yield
    print('close browser')

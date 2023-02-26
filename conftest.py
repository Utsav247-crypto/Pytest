import pytest
@pytest.fixture(autouse=True)
def setup():
    print('login browser')
    yield
    print('close browser')
    
def setup(request):
    session = request.node
    html = request.config._html
    report_content = html._generate_report(session)
    html._save_report(report_content)

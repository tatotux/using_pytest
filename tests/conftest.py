# conftest.py

def pytest_sessionstart(session):
    """
    Called before test session starts.
    """
    session.testrail_results = []


def pytest_sessionfinish(session, exitstatus):
    """
    Called after all tests are executed.
    """
    for result in session.testrail_results:
        print(result)

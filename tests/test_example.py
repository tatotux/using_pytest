# tests/test_example.py
import pytest


def test_addition(request):
    assert 1 + 1 == 2
    request.session.testrail_results.append({
        "test_name": "test_addition",
        "status": "pass",
        "message": "1 + 1 == 2"
    })


def test_subtraction(request):
    assert 5 - 3 == 2
    request.session.testrail_results.append({
        "test_name": "test_subtraction",
        "status": "pass",
        "message": "5 - 3 == 2"
    })

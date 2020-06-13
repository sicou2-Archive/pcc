import pytest

import python_repos


# assert hn_submissions == "r.status code"
def test_get_requests():
    r = python_repos.get_requests()
    assert r.status_code == 200

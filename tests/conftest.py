import pytest

import hordelib


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    hordelib.initialise()

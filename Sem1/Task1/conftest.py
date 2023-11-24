import pytest


@pytest.fixture()
def good_word():
    return "молоко"


@pytest.fixture()
def bad_word():
    return "малоко"

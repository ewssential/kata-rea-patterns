import pytest


@pytest.fixture
def thing():
    pass


def test_correct_greeting(thing):
    assert "Hello Bob!" == thing.return_hello_name()


def test_fail(thing):
    assert "Wrong!" == thing.return_hello_name()

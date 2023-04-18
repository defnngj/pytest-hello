import pytest


@pytest.mark.env("test")
def test_hello(hello):
    print("hello:", hello)
    assert "hello" in hello


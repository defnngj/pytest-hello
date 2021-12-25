import pytest


@pytest.mark.env("test")
def test_case(hello):
    print("hello:", hello)
    assert "hello" in hello


import pytest
from typing import Any, Optional


def pytest_configure(config: Any) -> None:
    """
    register an additional marker
    """
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


def pytest_runtest_setup(item: Any) -> None:
    """
    Called to perform the setup phase for a test item.
    """
    env_names = [mark.args[0] for mark in item.iter_markers(name="env")]
    if env_names:
        if item.config.getoption("--env") not in env_names:
            pytest.skip("test requires env in {!r}".format(env_names))


@pytest.fixture(scope="function")
def hello(hello_name: str) -> str:
    """
    hello Hook function
    """
    return f"hello, {hello_name}"


@pytest.fixture(scope="function")
def hello_name(pytestconfig: Any) -> Optional[str]:
    """
    hello_name Hook function
    """
    names = pytestconfig.getoption("--hello")
    if len(names) == 0:
        return "虫师"
    if len(names) == 1:
        return names[0]
    return names[0]


def pytest_addoption(parser: Any) -> None:
    """
    Add pytest option
    """
    group = parser.getgroup("hello", "Hello")
    group.addoption(
        "--env",
        action="store",
        default=[],
        help="only run tests matching the environment {name}.",
    )
    group.addoption(
        "--hello",
        action="append",
        default=[],
        help="hello {name}",
    )

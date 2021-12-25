import pytest
from typing import Any, Optional


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )


def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("-E") not in envnames:
            pytest.skip("test requires env in {!r}".format(envnames))


@pytest.fixture(scope="function")
def hello(hello_name: str) -> str:
    return f"hello, {hello_name}"


@pytest.fixture(scope="function")
def hello_name(pytestconfig: Any) -> Optional[str]:
    names = pytestconfig.getoption("--hello")
    if len(names) == 0:
        return "虫师"
    if len(names) == 1:
        return names[0]
    return names[0]


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("hello", "Hello")
    group.addoption(
        "--hello",
        action="append",
        default=[],
        help="hello {name}",
    )
    group.addoption(
        "-E",
        action="store",
        metavar="NAME",
        help="only run tests matching the environment NAME.",
    )

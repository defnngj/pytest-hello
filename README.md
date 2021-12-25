# pytest-hello

> 开发pytest插件demo项目。

## 安装

```shell script
> git clone https://github.com/defnngj/pytest-hello
> cd pytest-hello
> python setup.py install
```

## 帮助

```shell script
> pytest --help
...

Hello:
  --hello=HELLO         hello {name}
  -E NAME               only run tests matching the environment NAME.

```

## 用法

`test_sample.py` 用例：

```python
import pytest


@pytest.mark.env("test")
def test_case(hello):
    print("hello:", hello)
    assert "hello" in hello

```

## 运行:

1. 设置非`test` 环境，跳过用例
 
```shell script
> pytest -vs test_sample.py -E dev
==================================================================== test session starts =====================================================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/tech/.local/share/virtualenvs/github-Gjuvl5X_/bin/python
cachedir: .pytest_cache
rootdir: /Users/tech/klpro/github/pytest-hello
plugins: hello-0.0.1
collected 1 item

test_sample.py::test_case SKIPPED (test requires env in ['test'])
```

2. 设置`test` 环境，运行用例, 未设置`--hello` 参数
 
```shell script
pytest -vs test_sample.py -E test
==================================================================== test session starts =====================================================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/tech/.local/share/virtualenvs/github-Gjuvl5X_/bin/python
cachedir: .pytest_cache
rootdir: /Users/tech/klpro/github/pytest-hello
plugins: hello-0.0.1
collected 1 item

test_sample.py::test_case hello: hello, 虫师
PASSED

```

2. 设置`test`环境，运行用例, 设置`--hello` 参数
 
```shell script
> pytest -vs test_sample.py -E test --hello jack
==================================================================== test session starts =====================================================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/tech/.local/share/virtualenvs/github-Gjuvl5X_/bin/python
cachedir: .pytest_cache
rootdir: /Users/tech/klpro/github/pytest-hello
plugins: hello-0.0.1
collected 1 item

test_sample.py::test_case hello: hello, jack
PASSED

```
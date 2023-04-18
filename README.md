# pytest-hello

> 开发pytest插件demo项目。

## 安装

* 下载安装

```shell script
> git clone https://github.com/defnngj/pytest-hello
> cd pytest-hello
> pip install .
```

* pip在线安装

```shell
> pip install -U https://github.com/defnngj/pytest-hello.git@master
```

## 帮助

```shell script
> pytest --help
...

Hello:
  --env=ENV             only run tests matching the environment {name}.
  --hello=HELLO         hello {name}
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

1. 不设置`--env`参数或设置参数值非`test`，跳过用例。
 
```shell
> pytest -vs test_sample.py --env dev

collected 1 item
test_sample.py::test_case SKIPPED (test requires env in ['test'])
```

2. 设置`--env`参数值为`test`， 同时未设置`--hello` 参数，默认值为“虫师”
 
```shell
> pytest -vs test_sample.py --env test

collected 1 item

test_sample.py::test_case hello: hello, 虫师
PASSED
```

3. 设置`--env`参数值为`test`, 同时设置`--hello` 参数值为`jack`。

```shell
> pytest -vs test_sample.py --env test --hello jack

collected 1 item

test_sample.py::test_case hello: hello, jack
PASSED
```
import re
import ast
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pytest_hello/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setuptools.setup(
    name="pytest-hello",
    version=version,
    author="bugmaster",
    author_email="fnngj@126.com",
    description="pytest hello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/defnngj/pytest-hello",
    packages=["pytest_hello"],
    include_package_data=True,
    install_requires=[
        "pytest",
    ],
    entry_points={"pytest11": ["hello = pytest_hello.pytest_hello"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Pytest",
    ],
    python_requires=">=3.7",
    setup_requires=["setuptools_scm"],
)
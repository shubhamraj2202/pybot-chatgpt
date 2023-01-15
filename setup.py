"""Package Release"""

from __future__ import annotations

from setuptools import find_packages, setup

setup(
    name="pyhelper-misc",
    version="2.0.0",
    description="Python Library Containing Generic Utilities and Helper Functions",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Shubham Raj",
    author_email="shubhamraj2202@gmail.com",
    url="https://github.com/shubhamraj2202/pyhelper",
    packages=find_packages(include=["pyhelper", "pyhelper.*"]),
    install_requires=[],
    tests_require=["pytest"],
    project_urls={
        "Bug Reports": "https://github.com/shubhamraj2202/pyhelper/issues",
    },
)

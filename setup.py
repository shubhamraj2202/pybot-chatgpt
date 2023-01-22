"""Package Release"""

from __future__ import annotations

from setuptools import find_packages, setup

setup(
    name="pybot-chatgpt",
    version="2.0.0",
    description="PythonBot wrapping ChatGPT API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Shubham Raj",
    author_email="shubhamraj2202@gmail.com",
    url="https://github.com/shubhamraj2202/pybot-chatgpt",
    packages=find_packages(include=["chatgpt", "chatgpt.*", "chatgpt.src"]),
    install_requires=["openai"],
    test_requires=["pytest", "mock"],
    project_urls={
        "Bug Reports": "https://github.com/shubhamraj2202/pybot-chatgpt/issues",
    },
    entry_points={
        "console_scripts": [
            "pybot = chatgpt.run:chatbot",
        ],
    },
)

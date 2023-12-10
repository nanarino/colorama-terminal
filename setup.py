# -*- coding:utf-8 -*-
import setuptools

with open("readme.md", "r", encoding='utf-8') as readme:
    description = readme.read()

setuptools.setup(
    name="colorama_terminal",
    version="0.0.1",
    description="在终端有颜色地打印python变量",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/nanarino/colorama-terminal",
    packages=['colorama_terminal'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
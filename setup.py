#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rimcli",
    version="0.0.9",
    author="Carlos Xavier Azua-Gonzalez, Alan Fleming",
    author_email="Azua-GonzalezCX@cardiff.ac.uk",
    maintainer="KOKOA-ESPOL",
    description="cli-extension for rapid and easy use of ReadIM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=["numpy<2.0", "matplotlib>=3.6", "ReadIM"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "rim-cli = rimcli:rcmain",
        ],
    },
)

"""
Created on Wed Apr  8 23:08:06 2020

@author: abutte2
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-abutte2", # Replace with your own username
    version="0.0.1",
    author="Arun Arun",
    author_email="arun.butte70@gmail.com",
    description="Comparision of two strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
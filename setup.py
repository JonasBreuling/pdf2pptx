from setuptools import setup, find_packages

name = "pdf2pptx"
version = "0.0.1"
author = "Jonas Breuling"
author_email = "breuling@inm.uni-stuttgart.de"
url = ""
description = "Convert *.pdf files to *.pptx files with fiven resolution."
long_description = ""
license = "LICENSE"

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    install_requires=[
        "pdf2image>=1.17.0",
        "python-pptx>=1.0.2",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
)
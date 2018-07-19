from setuptools import setup, find_packages
import re,os
version = "0.1.12"

setup(
    name='xlscsv',
    version = version,
    packages=[],
    python_requires='>=3.5.3',
    install_requires=[ 'xlrd', 'openpyxl'],
    scripts = ['xlscsv.py'],
    description = open('README.md').readlines()[1],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = "ahuigo",
    author_email = "ahui132@qq.com",
    license = "MIT",
    url = "http://github.com/ahuigo/xlscsv",   
)


#!/usr/bin/env python
from os import path as op
from setuptools import setup
version = "0.1.12"


def _read(fname='README.md', line=None):
    try:
        if line is None:
            return open(op.join(op.dirname(__file__), fname)).read()
        return open(op.join(op.dirname(__file__), fname)).readlines()[line].strip()
    except IOError:
        return ''


setup(
    name='xlparser',
    version="0.2.9",
    author="ahuigo",
    author_email="ahui132@qq.com",
    license="MIT",
    url="http://github.com/ahuigo/xlparser",
    python_requires='>=3.6.1',
    packages=[],
    package_dir={"": "."},
    py_modules=['xlparser'],
    install_requires=['xlrd', 'openpyxl>=2.5.4'],
    scripts=['xlparser.py'],
    description=_read(line=1),
    long_description=_read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],

)

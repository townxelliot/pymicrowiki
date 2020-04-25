"""
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import json
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pymicrowiki',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'pymicrowiki',
    ],
    python_requires='>=3.6, <4',
    install_requires=[
        'Flask',
    ],
    extras_require={
        'dev': [
        ],
    }
)

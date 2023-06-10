from setuptools import setup
from setuptools import Command
from Crypto import Random
from Crypto.Cipher import AES
import os

setup(
    name='datamerge',
    version='0.1.3',
    packages=['datamerge'],
    entry_points={
        'console_scripts': [
            'datamerge=datamerge.DataMergeLoader:main'
        ]
    }
)
#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='Ting',
      version='1.0',
      description='Python tcp ping utility',
      author='Mikhail Cherniak',
      author_email='',
      url='',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'ting = Ting:main',
          ],
      }
      )

#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='Ting',
      version='1.0',
      description='Python tcp ping utility',
      author='Mikhail Cherniak, Peter Hill',
      author_email='mikcherniak@gmail.com',
      url='',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'ting = Ting:main',
          ],
      }
      )

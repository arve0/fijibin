#!/usr/bin/env python
# encoding: utf-8

# readme
import os
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    print('README.rst missing')
    long_description = ''

from setuptools import setup


setup(name='fijibin',
      version=open(os.path.join('fijibin', 'VERSION')).read().strip(),
      description='Latest Life-Line version of Fiji for easy inclusion in python projects.',
      author='Arve Seljebu',
      author_email='arve.seljebu@gmail.com',
      url='https://github.com/arve0/fijibin',
      license='MIT',
      packages=['fijibin'],
      install_requires=[
          'pydebug'
      ],
      package_data={'fijibin': ['VERSION']},
      include_package_data=True,
      long_description=long_description)

#!/usr/bin/env python
# encoding: utf-8

# readme
import os
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    print('README.rst missing')
    long_description = ''

from setuptools import setup, find_packages
from setuptools.command.install import install
from fijibin.fetch import fetch

class CustomInstall(install):
    """Fetch Fiji and install package."""
    def run(self):
        fetch()
        install.run(self)

setup(name='fijibin',
      version='0.0.2',
      description='Latest Life-Line version of Fiji for easy inclusion in python projects.',
      author='Arve Seljebu',
      author_email='arve.seljebu@gmail.com',
      url='https://github.com/arve0/fijibin',
      license='MIT',
      packages=['fijibin'],
      long_description=long_description,
      cmdclass={'install': CustomInstall} )

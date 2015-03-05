# coding=utf-8
"""
appinstance
erik@a8.nl (04-03-15)
license: GNU-GPL2
"""
from setuptools import setup
setup(name='unittest',
      version='0.1',
      description='Console printer with linenumbers, stacktraces, logging, conversions and coloring..',
      url='https://github.com/erikdejonge/unittest',
      author='Erik de Jonge',
      author_email='erik@a8.nl',
      license='GPL',
      packages=['unittest'],
      zip_safe=True, requires=['pyprofiler'])

from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='withumb',
      version=version,
      description="Tools and utilities for the WiThumb",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='withumb iot usb',
      author='Petri Savolainen',
      author_email='petri@koodaamo.fi',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
         "pyserial",
         "esptool"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

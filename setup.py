from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='yahoowebapi',
      version=version,
      description="Python wrapper for Yahoo! web IPA",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='API Yahoo',
      author='Maksym Shalenyi (enkidulan)',
      author_email='enkidulan@gmail.com',
      url='https://github.com/enkidulan/yahoowebapi',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "furl",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

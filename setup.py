from setuptools import setup

import sys

if sys.version_info < (2, 5):
    sys.exit('Sorry, Python < 2.5 is not supported')

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    name='qtop',
    version='0.9.0rc5',
    description="""qtop: the fast text mode way to monitor your cluster's utilization and status;
      the time has come to take back control of your cluster's scheduling business""",
    license="MIT",
    long_description=long_description,
    author='Sotiris Fragkiskos',
    author_email='sfranky@gmail.com',
    url="https://github.com/qtop/qtop",
    packages=['source',
              'source.legacy',
              'source.plugins',
              'source.ui'
              ],
    package_dir={'source': 'source'},
    package_data={'source': ['qtopconf.yaml']}
)
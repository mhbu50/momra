from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in momra/__init__.py
from momra import __version__ as version

setup(
	name='momra',
	version=version,
	description='momra',
	author='momra',
	author_email='momra@momra.gov.sa',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

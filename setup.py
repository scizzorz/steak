import steak
from setuptools import setup

setup(
	name='steak',
	version=steak.__version__,
	description='Simplify writing and executing repetitive tasks.',
	long_description=open('README.rst').read(),
	url='https://github.com/scizzorz/steak',
	license='MIT',
	author='John Weachock',
	author_email='jweachock@gmail.com',
	py_modules=['steak'],
	include_package_data=True,
	scripts=['bin/grill'],
)

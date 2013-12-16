import os

def readme():
	'''Generate the RST README'''
	os.system('pandoc README.md -o README.rst')

def clean():
	'''Clean up generated files'''
	os.system('rm -rf *.pyc __pycache__ README.rst dist steak.egg-info')

def test():
	'''Run nosetests'''
	os.system('nosetests')

def lint():
	'''Run pylint'''
	os.system('pylint steak.py')

def dist():
	'''Run setup.py sdist'''
	readme()
	os.system('python3 setup.py sdist')

def upload():
	'''Run setup.py sdist and upload to PyPI'''
	dist()
	os.system('python3 setup.py sdist upload -r pypi')

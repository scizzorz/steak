import inspect
import traceback
from functools import wraps

__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

class BurnException(Exception):
	'''Can be raised when a steak is burned and no longer suitable
	for consumption.'''

class Grill(object):
	def __init__(self):
		self.steaks = {}

	def steak(self, func):
		if not isinstance(func, Steak):
			func = Steak(func)
			if not func.name.startswith('_'):
				self.steaks[func.qualname] = func
		return func

	def burn(self, message, *args):
		raise BurnException(message.format(*args))

	def main(self, args):
		if 'setup' in self:
			self['setup'].invoke()

		try:
			if not args and 'default' in self:
				self['default'].invoke()
			else:
				for arg in args:
					if arg in self:
						self[arg].invoke()
		finally:
			if 'teardown' in self:
				self['teardown'].invoke()

	def __getitem__(self, key):
		matches = [self.steaks[x] for x in self.steaks if x.startswith(key)]
		if matches:
			return matches[0]
		raise KeyError

	def __contains__(self, item):
		matches = [x for x in self.steaks if x.startswith(item)]
		return len(matches) > 0

class Steak(object):
	def __init__(self, func):
		self.func = func
		self.name = func.__name__
		self.doc = func.__doc__
		self.module = inspect.getmodule(func).__name__
		self.qual = ('') if (self.module == '__steak__') else (self.module + '.')
		self.qualname = self.qual + self.name
		self.valid = False

	def __call__(self, *args, **kwargs):
		if self.valid:
			return self.valid
		self.invoke(*args, **kwargs)

	def invoke(self, *args, **kwargs):
		print('Grilling {}...'.format(self.qualname))
		try:
			self.func(*args, **kwargs)
		except BurnException as ex:
			print('Burned :(')
		except Exception as ex:
			print('Charred :(')
			traceback.print_exc()
		else:
			self.valid = True
			return self.valid

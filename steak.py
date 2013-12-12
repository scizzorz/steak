import inspect
import traceback
from functools import wraps

__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

class BurnException(Exception):
	'''Can be raised when a steak is burned and no longer suitable
	for consumption.'''

STEAKS = {}


def steakify(func):
	if not isinstance(func, Steak):
		func = Steak(func)
		STEAKS[func.qualname] = func
	return func

class Steak(object):
	def __init__(self, func):
		self.func = func
		self.name = func.__name__
		self.doc = func.__doc__
		self.module = inspect.getmodule(func).__name__
		self.qual = ('') if (self.module == '__steak__') else (self.module + '.')
		self.qualname = self.qual + self.name

	def __call__(self, *args, **kwargs):
		print('Grilling...')
		try:
			self.func(*args, **kwargs)
		except BurnException as ex:
			print('Burned :(')
		except Exception as ex:
			print('Charred :(')
			traceback.print_exc()
			raise BurnException
		else:
			return True

def main(args):
	print('main')
	for arg in args:
		if arg in STEAKS:
			STEAKS[arg]()

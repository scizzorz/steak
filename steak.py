import inspect
import traceback
from getopt import getopt
from inspect import Parameter
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
			func = Steak(self, func)
			if not func.name.startswith('_'):
				self.steaks[func.qualname] = func

		return func

	def burn(self, message, *args):
		raise BurnException(message.format(*args))

	def highlight(self, string, color):
		if color > 7:
			color += 52
		return '\033[{color}m{string}\033[0m'.format(string=string, color=color+30)

	def main(self, args):
		if 'setup' in self:
			args = self['setup'].invoke(args)

		try:
			if not args and 'default' in self:
				self['default'].invoke()
			else:
				while args:
					name = args[0]
					if name in self:
						args = self[name].invoke(args[1:])
					else:
						self.burn('No task found')
		except BurnException as ex:
			print('Oops. Your {!r} steak was burned :( {}'.format(self[name], ex))
		except Exception as ex:
			traceback.print_exc()
			print('Oops. Your {!r} steak exploded :( {}'.format(self[name], ex))
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
	def __init__(self, grill, func):
		self.grill = grill
		self.func = func
		self.name = func.__name__
		self.doc = func.__doc__
		self.module = inspect.getmodule(func).__name__
		self.qual = ('') if (self.module == '__steak__') else (self.module + '.')
		self.qualname = self.qual + self.name

		self.valid = False
		self.args = []
		self.kwargs = []
		self.defaults = {}
		self.varargs = False

		sig = inspect.signature(self.func)
		for name, arg in sig.parameters.items():
			if arg.kind == Parameter.VAR_POSITIONAL:
				self.varargs = True
			elif arg.default == Parameter.empty:
				self.args.append(name)
			else:
				self.defaults[name] = arg.default
				if arg.default in (True, False):
					self.kwargs.append(name)
				else:
					self.kwargs.append(name + '=')

	def __call__(self, *args, **kwargs):
		return self.valid or self.call(*args, **kwargs)

	def invoke(self, args=[]):
		# FIXME: positional/keyword arguments explode when using varargs
		# eg: def f(a, b=False, *args) breaks if you provide 2 args
		# however, def f(a, *args, b=False) is totally fine because b is kw-only

		kwargs = self.defaults.copy()
		if self.kwargs:
			temp_kwargs, args = getopt(args, '', self.kwargs)
			temp_kwargs = self.parse_opts(*temp_kwargs)
			kwargs.update(temp_kwargs)

		posargs = []
		for arg in self.args:
			if not len(args):
				self.grill.burn('Wrong number of arguments')
			posargs.append(args[0])
			args = args[1:]

		if self.varargs:
			self.call(*(posargs + args), **kwargs)
			return []

		self.call(*posargs, **kwargs)
		return args

	def call(self, *args, **kwargs):
		self.func(*args, **kwargs)
		self.valid = True
		return self.valid

	def parse_opts(self, *opts):
		ret = {}
		for key, val in opts:
			if key[:2] == '--':
				key = key[2:]
			elif key[:1] == '-':
				key = key[1:]
			if val == '':
				val = True # FIXME: should be opposite of flag setting
			ret[key.replace('-', '_')] = val
		return ret

	def __str__(self):
		return self.qualname

	def __repr__(self):
		return self.grill.highlight(str(self), 1 if self.valid else 2)

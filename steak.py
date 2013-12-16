import inspect
import traceback
from getopt import getopt
from inspect import Parameter as Param

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

	@staticmethod
	def burn(message, *args):
		raise BurnException(message.format(*args))

	@staticmethod
	def highlight(string, color):
		if color > 7:
			color += 52
		return '\033[{color}m{string}\033[0m'.format(string=string, color=color+30)

	@staticmethod
	def log(message, *args):
		print(message.format(*args))

	def main(self, args):
		try:
			if 'setup' in self:
				args, _ = self['setup'].invoke(args)
			if not args and 'default' in self:
				self['default'].invoke()
			else:
				while args:
					name = args[0]
					if name in self:
						args, _ = self[name].invoke(args[1:])
					else:
						self.burn('No task found')
		except BurnException as ex:
			self.log('Oops. Your {!r} steak was burned :( {}', self[name] or name, ex)
		except Exception as ex:
			traceback.print_exc()
			self.log('Oops. Your {!r} steak exploded :( {}', self[name] or name, ex)
		finally:
			if 'teardown' in self:
				self['teardown'].invoke()

	def help(self):
		for key in sorted(self.steaks):
			self.log(self.steaks[key].help())

	def __getitem__(self, key):
		matches = [self.steaks[x] for x in self.steaks if x.startswith(key)]
		if matches:
			return matches[0]

	def __contains__(self, item):
		matches = [x for x in self.steaks if x.startswith(item)]
		return len(matches) > 0

	def __len__(self):
		return len(self.steaks)

class Steak(object):
	def __init__(self, grill, func):
		self.grill = grill
		self.func = func
		self.name = func.__name__
		self.doc = func.__doc__
		self.module = inspect.getmodule(func).__name__
		self.qual = ('') if (self.module == '__grill__') else (self.module + '.')
		self.qualname = self.qual + self.name

		self.store = None

		self.valid = None
		self.args = []
		self.kwargs = []
		self.defaults = {}
		self.varargs = None

		sig = inspect.signature(self.func)
		self.params = sig.parameters
		for name, arg in sig.parameters.items():
			if arg.kind in (Param.POSITIONAL_ONLY, Param.POSITIONAL_OR_KEYWORD):
				self.args.append(name)
			elif arg.kind == Param.VAR_POSITIONAL:
				self.varargs = name

			if arg.default is not Param.empty:
				self.defaults[name] = arg.default
				if arg.default in (True, False):
					self.kwargs.append(name)
				else:
					self.kwargs.append(name + '=')

	def __call__(self, *args, **kwargs):
		if self.valid is None:
			self.call(*args, **kwargs)
		return self.store

	def invoke(self, args=()):
		kwargs = self.defaults.copy()
		if self.kwargs:
			temp_kwargs, args = getopt(args, '', self.kwargs)
			temp_kwargs = self.parse_opts(*temp_kwargs)
			kwargs.update(temp_kwargs)

		posargs = []
		for arg in self.args:
			if arg in kwargs:
				posargs.append(kwargs[arg])
				del kwargs[arg]
			else:
				if not len(args):
					self.grill.burn('Wrong number of arguments')
				posargs.append(args[0])
				args = args[1:]

		if self.varargs:
			self.call(*(list(posargs) + list(args)), **kwargs)
			return (), self.store

		self.call(*posargs, **kwargs)
		return args, self.store

	def call(self, *args, **kwargs):
		try:
			self.store = self.func(*args, **kwargs)
		except:
			self.valid = False
			raise
		else:
			self.valid = True
		return self.store

	def parse_opts(self, *opts):
		ret = {}
		for key, val in opts:
			if key[:2] == '--':
				key = key[2:]
			elif key[:1] == '-':
				key = key[1:]
			if val == '' and key in self.defaults:
				val = not self.defaults[key]
			ret[key.replace('-', '_')] = val
		return ret

	def help(self):
		ret = [repr(self)]

		for arg, val in self.defaults.items():
			if val in (True, False):
				ret.append('[--%s]' % arg)
			else:
				ret.append('[--%s %s]' % (arg, val))

		for arg in self.args:
			if arg not in self.defaults:
				ret.append(arg)

		if self.varargs:
			ret.append('[%s...]' % self.varargs)

		ret = ' '.join(ret)
		if self.doc:
			ret += '\n\t' + self.doc

		return ret

	def __str__(self):
		return self.qualname

	def __repr__(self):
		color = 4
		if self.valid is True:
			color = 2
		elif self.valid is False:
			color = 1
		return self.grill.highlight(str(self), color)

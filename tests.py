import steak

def test_steak():
	grill = steak.Grill()
	@grill.steak
	def something():
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == []
	assert something.kwargs == []
	assert something.defaults == {}
	assert something.varargs is False

def test_steak_posargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == []
	assert something.defaults == {}
	assert something.varargs is False

def test_steak_kwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=None, b=False):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == ['a=', 'b']
	assert something.defaults == {'a': None, 'b': False}
	assert something.varargs is False

def test_steak_varargs():
	grill = steak.Grill()
	@grill.steak
	def something(*args):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == []
	assert something.kwargs == []
	assert something.defaults == {}
	assert something.varargs is True

def test_steak_poskwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=None, d=False):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b', 'c', 'd']
	assert something.kwargs == ['c=', 'd']
	assert something.defaults == {'c': None, 'd': False}
	assert something.varargs is False

def test_steak_posvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == []
	assert something.defaults == {}
	assert something.varargs is True

def test_steak_kwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=False, b=None, *c):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == ['a', 'b=']
	assert something.defaults == {'a': False, 'b': None}
	assert something.varargs is True

def test_steak_poskwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=False, d=None, *e):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b', 'c', 'd']
	assert something.kwargs == ['c', 'd=']
	assert something.defaults == {'c': False, 'd': None}
	assert something.varargs is True

def test_steak_posvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c, d=None, e=False):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == ['d=', 'e']
	assert something.defaults == {'d': None, 'e': False}
	assert something.varargs is True

def test_steak_poskwvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b=True, *c, d=None, e=False):
		'Something.'
		return True

	assert isinstance(something, steak.Steak)
	assert something.grill is grill
	assert something.name == 'something'
	assert something.doc == 'Something.'
	assert something.module == 'tests'
	assert something.qual == 'tests.'
	assert something.qualname == 'tests.something'
	assert something.store is None
	assert something.valid is None
	assert something.args == ['a', 'b']
	assert something.kwargs == ['b', 'd=', 'e']
	assert something.defaults == {'b': True, 'd': None, 'e': False}
	assert something.varargs is True

def test_invoke():
	grill = steak.Grill()
	@grill.steak
	def something():
		'Something.'
		return True

	assert something.invoke() == ((), True)

	assert something.invoke(('end',)) == (('end',), True)

def test_invoke_posargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b):
		'Something.'
		return (a, b)

	assert something.invoke(('one', 'two')) == ((), ('one', 'two'))

	assert something.invoke(('one', 'two', 'end')) == (('end',), ('one', 'two'))

def test_invoke_kwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=None, b=False):
		'Something.'
		return (a, b)

	assert something.invoke(('--a=one', '--b')) == ((), ('one', True))
	assert something.invoke(('--b', '--a=one')) == ((), ('one', True))
	assert something.invoke(('--a', 'one', '--b')) == ((), ('one', True))
	assert something.invoke(('--b', '--a', 'one')) == ((), ('one', True))
	assert something.invoke(('--a=one',)) == ((), ('one', False))
	assert something.invoke(('--a', 'one')) == ((), ('one', False))
	assert something.invoke(('--b',)) == ((), (None, True))
	assert something.invoke() == ((), (None, False))

	assert something.invoke(('--a=one', '--b', 'end')) == (('end',), ('one', True))
	assert something.invoke(('--b', '--a=one', 'end')) == (('end',), ('one', True))
	assert something.invoke(('--a', 'one', '--b', 'end')) == (('end',), ('one', True))
	assert something.invoke(('--b', '--a', 'one', 'end')) == (('end',), ('one', True))
	assert something.invoke(('--a=one', 'end')) == (('end',), ('one', False))
	assert something.invoke(('--a', 'one', 'end')) == (('end',), ('one', False))
	assert something.invoke(('--b', 'end')) == (('end',), (None, True))
	assert something.invoke(('end',)) == (('end',), (None, False))

def test_invoke_varargs():
	grill = steak.Grill()
	@grill.steak
	def something(*args):
		'Something.'
		return args

	assert something.invoke(('one',)) == ((), ('one',))

	assert something.invoke(('one', 'end')) == ((), ('one', 'end'))

def test_invoke_poskwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=None, d=False):
		'Something.'
		return (a, b, c, d)

	assert something.invoke(('--c=one', '--d', 'two', 'three')) == ((), ('two', 'three', 'one', True))
	assert something.invoke(('--d', '--c=one', 'two', 'three')) == ((), ('two', 'three', 'one', True))
	assert something.invoke(('--c', 'one', '--d', 'two', 'three')) == ((), ('two', 'three', 'one', True))
	assert something.invoke(('--d', '--c', 'one', 'two', 'three')) == ((), ('two', 'three', 'one', True))
	assert something.invoke(('--c=one', 'two', 'three')) == ((), ('two', 'three', 'one', False))
	assert something.invoke(('--c', 'one', 'two', 'three')) == ((), ('two', 'three', 'one', False))
	assert something.invoke(('--d', 'two', 'three')) == ((), ('two', 'three', None, True))
	assert something.invoke(('one', 'two')) == ((), ('one', 'two', None, False))

	assert something.invoke(('--c=one', '--d', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', True))
	assert something.invoke(('--d', '--c=one', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', True))
	assert something.invoke(('--c', 'one', '--d', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', True))
	assert something.invoke(('--d', '--c', 'one', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', True))
	assert something.invoke(('--c=one', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', False))
	assert something.invoke(('--c', 'one', 'two', 'three', 'end')) == (('end',), ('two', 'three', 'one', False))
	assert something.invoke(('--d', 'two', 'three', 'end')) == (('end',), ('two', 'three', None, True))
	assert something.invoke(('one', 'two', 'end')) == (('end',), ('one', 'two', None, False))

def test_invoke_posvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c):
		'Something.'
		return (a, b, c)

	assert something.invoke(('one', 'two')) == ((), ('one', 'two', ()))
	assert something.invoke(('one', 'two', 'three')) == ((), ('one', 'two', ('three',)))

	assert something.invoke(('one', 'two', 'three', 'end')) == ((), ('one', 'two', ('three', 'end')))

def test_invoke_kwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=False, b=None, *c):
		'Something.'
		return (a, b, c)

	assert something.invoke(('--b=one', '--a')) == ((), (True, 'one', ()))
	assert something.invoke(('--a', '--b=one')) == ((), (True, 'one', ()))
	assert something.invoke(('--b', 'one', '--a')) == ((), (True, 'one', ()))
	assert something.invoke(('--a', '--b', 'one')) == ((), (True, 'one', ()))
	assert something.invoke(('--b=one',)) == ((), (False, 'one', ()))
	assert something.invoke(('--b', 'one')) == ((), (False, 'one', ()))
	assert something.invoke(('--a',)) == ((), (True, None, ()))
	assert something.invoke() == ((), (False, None, ()))

	assert something.invoke(('--b=one', '--a', 'end')) == ((), (True, 'one', ('end',)))
	assert something.invoke(('--a', '--b=one', 'end')) == ((), (True, 'one', ('end',)))
	assert something.invoke(('--b', 'one', '--a', 'end')) == ((), (True, 'one', ('end',)))
	assert something.invoke(('--a', '--b', 'one', 'end')) == ((), (True, 'one', ('end',)))
	assert something.invoke(('--b=one', 'end')) == ((), (False, 'one', ('end',)))
	assert something.invoke(('--b', 'one', 'end')) == ((), (False, 'one', ('end',)))
	assert something.invoke(('--a', 'end')) == ((), (True, None, ('end',)))
	assert something.invoke(('end',)) == ((), (False, None, ('end',)))

def test_invoke_poskwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=False, d=None, *e):
		'Something.'
		return True

	assert False

def test_invoke_posvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c, d=None, e=False):
		'Something.'
		return True

	assert False

def test_invoke_poskwvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b=True, *c, d=None, e=False):
		'Something.'
		return True

	assert False

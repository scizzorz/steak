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
	def something(a, b, c=None, d=False, *e):
		'Something.'
		return (a, b, c, d, e)

	assert something.invoke(('--c=one', '--d', 'two', 'three')) == ((), ('two', 'three', 'one', True, ()))
	assert something.invoke(('--d', '--c=one', 'two', 'three')) == ((), ('two', 'three', 'one', True, ()))
	assert something.invoke(('--c', 'one', '--d', 'two', 'three')) == ((), ('two', 'three', 'one', True, ()))
	assert something.invoke(('--d', '--c', 'one', 'two', 'three')) == ((), ('two', 'three', 'one', True, ()))
	assert something.invoke(('--c=one', 'two', 'three')) == ((), ('two', 'three', 'one', False, ()))
	assert something.invoke(('--c', 'one', 'two', 'three')) == ((), ('two', 'three', 'one', False, ()))
	assert something.invoke(('--d', 'two', 'three')) == ((), ('two', 'three', None, True, ()))
	assert something.invoke(('one', 'two')) == ((), ('one', 'two', None, False, ()))

	assert something.invoke(('--c=one', '--d', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', True, ('end',)))
	assert something.invoke(('--d', '--c=one', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', True, ('end',)))
	assert something.invoke(('--c', 'one', '--d', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', True, ('end',)))
	assert something.invoke(('--d', '--c', 'one', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', True, ('end',)))
	assert something.invoke(('--c=one', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', False, ('end',)))
	assert something.invoke(('--c', 'one', 'two', 'three', 'end')) == ((), ('two', 'three', 'one', False, ('end',)))
	assert something.invoke(('--d', 'two', 'three', 'end')) == ((), ('two', 'three', None, True, ('end',)))
	assert something.invoke(('one', 'two', 'end')) == ((), ('one', 'two', None, False, ('end',)))

def test_invoke_posvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c, d=None, e=False):
		'Something.'
		return (a, b, c, d, e)

	assert something.invoke(('--d=one', '--e', 'two', 'three')) == ((), ('two', 'three', (), 'one', True))
	assert something.invoke(('--e', '--d=one', 'two', 'three')) == ((), ('two', 'three', (), 'one', True))
	assert something.invoke(('--d', 'one', '--e', 'two', 'three')) == ((), ('two', 'three', (), 'one', True))
	assert something.invoke(('--e', '--d', 'one', 'two', 'three')) == ((), ('two', 'three', (), 'one', True))
	assert something.invoke(('--d=one', 'two', 'three')) == ((), ('two', 'three', (), 'one', False))
	assert something.invoke(('--d', 'one', 'two', 'three')) == ((), ('two', 'three', (), 'one', False))
	assert something.invoke(('--e', 'two', 'three')) == ((), ('two', 'three', (), None, True))
	assert something.invoke(('one', 'two')) == ((), ('one', 'two', (), None, False))

	assert something.invoke(('--d=one', '--e', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', True))
	assert something.invoke(('--e', '--d=one', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', True))
	assert something.invoke(('--d', 'one', '--e', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', True))
	assert something.invoke(('--e', '--d', 'one', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', True))
	assert something.invoke(('--d=one', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', False))
	assert something.invoke(('--d', 'one', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), 'one', False))
	assert something.invoke(('--e', 'two', 'three', 'end')) == ((), ('two', 'three', ('end',), None, True))
	assert something.invoke(('one', 'two', 'end')) == ((), ('one', 'two', ('end',), None, False))

def test_invoke_poskwvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b=True, *c, d=None):
		'Something.'
		return (a, c, d, b)

	assert something.invoke(('--d=one', '--b', 'two')) == ((), ('two', (), 'one', False))
	assert something.invoke(('--b', '--d=one', 'two')) == ((), ('two', (), 'one', False))
	assert something.invoke(('--d', 'one', '--b', 'two')) == ((), ('two', (), 'one', False))
	assert something.invoke(('--b', '--d', 'one', 'two')) == ((), ('two', (), 'one', False))
	assert something.invoke(('--d=one', 'two')) == ((), ('two', (), 'one', True))
	assert something.invoke(('--d', 'one', 'two')) == ((), ('two', (), 'one', True))
	assert something.invoke(('--b', 'two')) == ((), ('two', (), None, False))
	assert something.invoke(('one',)) == ((), ('one', (), None, True))

	assert something.invoke(('--d=one', '--b', 'two', 'end')) == ((), ('two', ('end',), 'one', False))
	assert something.invoke(('--b', '--d=one', 'two', 'end')) == ((), ('two', ('end',), 'one', False))
	assert something.invoke(('--d', 'one', '--b', 'two', 'end')) == ((), ('two', ('end',), 'one', False))
	assert something.invoke(('--b', '--d', 'one', 'two', 'end')) == ((), ('two', ('end',), 'one', False))
	assert something.invoke(('--d=one', 'two', 'end')) == ((), ('two', ('end',), 'one', True))
	assert something.invoke(('--d', 'one', 'two', 'end')) == ((), ('two', ('end',), 'one', True))
	assert something.invoke(('--b', 'two', 'end')) == ((), ('two', ('end',), None, False))
	assert something.invoke(('one', 'end')) == ((), ('one', ('end',), None, True))

def test_call():
	grill = steak.Grill()
	@grill.steak
	def something():
		'Something.'
		return True

	assert something.call() == True

def test_call_posargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b):
		'Something.'
		return (a, b)

	assert something.call('one', 'two') == ('one', 'two')

def test_call_kwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=None, b=False):
		'Something.'
		return (a, b)

	assert something.call(a='one', b=True) == ('one', True)
	assert something.call(a='one') == ('one', False)
	assert something.call(b=True) == (None, True)
	assert something.call() == (None, False)

def test_call_varargs():
	grill = steak.Grill()
	@grill.steak
	def something(*args):
		'Something.'
		return args

	assert something.call('one') == ('one',)
	assert something.call('one', 'two') == ('one', 'two')

def test_call_poskwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=None, d=False):
		'Something.'
		return (a, b, c, d)

	assert something.call('one', 'two', c='three', d=True) == ('one', 'two', 'three', True)
	assert something.call('one', 'two', c='three') == ('one', 'two', 'three', False)
	assert something.call('one', 'two', d=True) == ('one', 'two', None, True)
	assert something.call('one', 'two') == ('one', 'two', None, False)

def test_call_posvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c):
		'Something.'
		return (a, b, c)

	assert something.call('one', 'two') == ('one', 'two', ())
	assert something.call('one', 'two', 'three') == ('one', 'two', ('three',))
	assert something.call('one', 'two', 'three', 'four') == ('one', 'two', ('three', 'four'))

def test_call_kwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a=False, b=None, *c):
		'Something.'
		return (a, b, c)

	assert something.call() == (False, None, ())
	assert something.call(True) == (True, None, ())
	assert something.call(True, 'one') == (True, 'one', ())
	assert something.call(True, 'one', 'two') == (True, 'one', ('two',))
	assert something.call(True, 'one', 'two', 'three') == (True, 'one', ('two', 'three'))

def test_call_poskwvarargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, c=None, d=False, *e):
		'Something.'
		return (a, b, c, d, e)

	assert something.call('one', 'two') == ('one', 'two', None, False, ())
	assert something.call('one', 'two', 'three') == ('one', 'two', 'three', False, ())
	assert something.call('one', 'two', 'three', True) == ('one', 'two', 'three', True, ())
	assert something.call('one', 'two', 'three', True, 'four') == ('one', 'two', 'three', True, ('four',))
	assert something.call('one', 'two', 'three', True, 'four', 'five') == ('one', 'two', 'three', True, ('four', 'five'))

def test_call_posvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b, *c, d=None, e=False):
		'Something.'
		return (a, b, c, d, e)

	assert something.call('one', 'two') == ('one', 'two', (), None, False)
	assert something.call('one', 'two', 'three') == ('one', 'two', ('three',), None, False)
	assert something.call('one', 'two', 'three', True) == ('one', 'two', ('three', True), None, False)
	assert something.call('one', 'two', 'three', True, 'four') == ('one', 'two', ('three', True, 'four'), None, False)

	assert something.call('one', 'two', d='fun') == ('one', 'two', (), 'fun', False)
	assert something.call('one', 'two', 'three', d='fun') == ('one', 'two', ('three',), 'fun', False)
	assert something.call('one', 'two', 'three', True, d='fun') == ('one', 'two', ('three', True), 'fun', False)
	assert something.call('one', 'two', 'three', True, 'four', d='fun') == ('one', 'two', ('three', True, 'four'), 'fun', False)

	assert something.call('one', 'two', e=True) == ('one', 'two', (), None, True)
	assert something.call('one', 'two', 'three', e=True) == ('one', 'two', ('three',), None, True)
	assert something.call('one', 'two', 'three', True, e=True) == ('one', 'two', ('three', True), None, True)
	assert something.call('one', 'two', 'three', True, 'four', e=True) == ('one', 'two', ('three', True, 'four'), None, True)

	assert something.call('one', 'two', d='fun', e=True) == ('one', 'two', (), 'fun', True)
	assert something.call('one', 'two', 'three', d='fun', e=True) == ('one', 'two', ('three',), 'fun', True)
	assert something.call('one', 'two', 'three', True, d='fun', e=True) == ('one', 'two', ('three', True), 'fun', True)
	assert something.call('one', 'two', 'three', True, 'four', d='fun', e=True) == ('one', 'two', ('three', True, 'four'), 'fun', True)

def test_call_poskwvarkwargs():
	grill = steak.Grill()
	@grill.steak
	def something(a, b=True, *c, d=None):
		'Something.'
		return (a, b, c, d)

	assert something.call('one') == ('one', True, (), None)
	assert something.call('one', False) == ('one', False, (), None)
	assert something.call('one', False, 'two') == ('one', False, ('two',), None)
	assert something.call('one', False, 'two', 'three') == ('one', False, ('two', 'three'), None)

	assert something.call('one', d='fun') == ('one', True, (), 'fun')
	assert something.call('one', False, d='fun') == ('one', False, (), 'fun')
	assert something.call('one', False, 'two', d='fun') == ('one', False, ('two',), 'fun')
	assert something.call('one', False, 'two', 'three', d='fun') == ('one', False, ('two', 'three'), 'fun')

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

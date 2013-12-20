import steak

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

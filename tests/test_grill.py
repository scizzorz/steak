import steak

def test_container():
	grill = steak.Grill()
	@grill.steak
	def something(x):
		return int(x)

	assert 'test_grill.something' in grill, grill.steaks
	assert 'test_grill.some' in grill
	assert 'test_grill.s' in grill
	assert len(grill) == 1
	assert grill['test_grill.something'] is something
	assert grill['test_grill.some'] is something
	assert grill['test_grill.s'] is something

def test_main():
	grill = steak.Grill()
	@grill.steak
	def something(x):
		return int(x)
	@grill.steak
	def magic(x):
		return int(x)

	grill.main([]) # nothing happens
	assert something.valid is None

	grill.main(['5']) # raise BurnException (how to catch it?)
	assert something.valid is None

	grill.main(['test_grill.something']) # raise BurnException (how to catch it?)
	assert something.valid is None

	grill.main(['test_grill.magic', '5'])
	assert magic.valid is True
	assert magic.store == 5
	assert magic(6) == 5

	grill.main(['test_grill.magic', '7'])
	assert magic.valid is True
	assert magic.store == 7
	assert magic(6) == 7

	grill.main(['test_grill.magic', '7', 'test_grill.magic', '8'])
	assert magic.valid is True
	assert magic.store == 8
	assert magic(6) == 8

def test_setup():
	setted_upped = False

	grill = steak.Grill()
	@grill.steak
	def something():
		pass
	@grill.steak
	def setup():
		nonlocal setted_upped
		setted_upped = True

	# need to mock the namespace
	grill.steaks['setup'] = setup

	assert setted_upped is False
	grill.main([])
	assert setted_upped is True

def test_teardown():
	teared_downed = False

	grill = steak.Grill()
	@grill.steak
	def something():
		pass

	@grill.steak
	def teardown():
		nonlocal teared_downed
		teared_downed = True

	# need to mock the namespace
	grill.steaks['teardown'] = teardown

	assert teared_downed is False
	grill.main([])
	assert teared_downed is True

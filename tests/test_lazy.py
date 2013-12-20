import steak

def test_lazy():
	grill = steak.Grill()
	@grill.steak
	def something(x, y):
		return x + y

	assert something(5, 6) == 11
	assert something.store == 11
	assert something(10, 11) == 11
	assert something(None, None) == 11
	assert something.call(6, 7) == 13
	assert something.store == 13
	assert something(5, 6) == 13
	assert something.call(8, 8) == 16
	assert something.store == 16
	assert something.call(9, 8) == 17
	assert something.store == 17

def test_valid():
	grill = steak.Grill()
	@grill.steak
	def something(x, y):
		return x / y

	assert something(10, 2) == 5.0
	assert something.valid

def test_invalid():
	grill = steak.Grill()
	@grill.steak
	def something(x, y):
		return x / y

	try:
		something(10, 0)
	except:
		pass

	assert not something.valid
	something(10, 2)
	assert not something.valid

eggs = 42


def local_shows_global() -> None:
	print('this is fucking local scope which displays global variable')
	# this will show global value
	print('>> this is global eggs:' + str(eggs))


def local_makes_local_scope() -> None:
	print('this is local scope with its copy of same variable')
	# an assignment on global variable will create a local variable with same name
	# this will make a local scoped variable
	eggs = 32
	print('>> this is eggs from local: ' + str(eggs))


def local_access_global() -> None:
	print('now we are accessing global eggs')
	global eggs
	print('>> global eggs:' + str(eggs))
	eggs = 31
	print('>> modified global eggs: ' + str(eggs))


print('>> Global eggs: ' + str(eggs))
local_shows_global()
local_makes_local_scope()
local_access_global()

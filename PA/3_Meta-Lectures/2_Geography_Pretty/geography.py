from functools import reduce

europe = {
	'italy': ['france','swiss','austria','san marino','vatican city'],
	'swiss': ['italy','france','austria','germany'],
	'france': ['italy','swiss','austria','germany','belgium','spain'],
	'san marino': ['italy'],
	'vatican city': ['italy'],
	'austria': ['italy','germany','france'],
	'germany': ['france'],
	'belgium': ['france'],
	'spain': ['france']
	}

def crossing(state,n):
	def crossing_rec(states,path,n):
		print(n,states)
		new_path = set(filter(lambda x: x not in path,reduce(lambda x,y: x + y,[europe[state] for state in states])))
		return crossing_rec( new_path, path.append(new_path), n-1 ) if n > 0 else states
	return crossing_rec({state},[],n)






def crossing_(state,n):
	def crossing_rec_(states,n):
		print(n,states)
		new_path = set(reduce(lambda x,y: x + y,[europe[state] for state in states]))
		return crossing_rec_( new_path, n-1 ) if n > 0 else states
	return crossing_rec_({state},n)

if __name__ == '__main__':
	crossing_('italy',3)
	print('----------------')
	crossing('italy',3)
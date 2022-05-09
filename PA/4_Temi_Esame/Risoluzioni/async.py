import threading

risultato= None

class future:
	def is_done(self):
		return risultato!=None
	def get_result(self):
		if risultato==None:
			raise MyException
		return risultato

class MyException(Exception):
    message= "the call has not yet completed its task"

def decora(method):
	def wrapper(*args):
		global risultato
		risultato= method(args[0])
	return wrapper
	
def asynchronous(method):
	class wrapper:
		def __init__(self):
			self.wrapped= method
		def start(self, num):
			global risultato
			risultato= None
			t= threading.Thread(target=decora(self.wrapped), args=([num]))
			t.start()
			return future()
	return wrapper()
asynchronous.NotYetDoneException = MyException
	
if __name__=='__main__':

	import time
	
	@asynchronous
	def long_process(num):
		time.sleep(10)
		return num * num
	
	result = long_process.start(12)
	
	for i in range(20):
		time.sleep(1)
		if result.is_done():
			print("[{1}]: result {0}".format(result.get_result(), i))
		else:
			print("[{0}]: not ready yet".format(i))

	result2 = long_process.start(13)
	try:
		print("result2 {0}".format(result2.get_result()))
	except asynchronous.NotYetDoneException as ex:
		print(ex.message)
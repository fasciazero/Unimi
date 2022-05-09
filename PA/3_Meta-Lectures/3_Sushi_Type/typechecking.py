import inspect

def type_checking(f):
	def wrapper(*args,**kwargs):
		type_errors = [(k,v,a) for (k,v),a in zip(inspect.signature(f).parameters.items(),args) if not isinstance(a,v.annotation) and not v.annotation == inspect.Parameter.empty]
		if len(type_errors) == 0:
			ret = f(*args)
			if isinstance(ret,inspect.signature(f).return_annotation) and inspect.signature(f).return_annotation != inspect.Signature.empty: return ret
			else: print(f,'with',args,': Wrong return type') 
		else: print(f,args,'Wrong type :','; '.join(['{} -> expected {} got {}'.format(name,expected,type(real)) for name,expected,real in type_errors]))
	return wrapper

@type_checking
def somma(x:int,y:int) -> int:
	return 'Mamma'

if __name__ == '__main__':
	somma(42,7)
	somma('ciao',7.2)
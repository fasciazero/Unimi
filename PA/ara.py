



def new_meta():
    class meta(type):
        def __new__(cls, classname, supers, classdic):
            classdic['sum'] = lambda x,y: x*y
            return type.__new__(cls, classname, supers, classdic)
    return meta




class calc(metaclass=new_meta()):

    def sum(*args):
        n=0
        for x in args:
            n+=x
        return n

cl = calc

print(cl.sum(10,20))
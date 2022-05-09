
def afterLog(name, value = None): print('*** I\'ve called ' + name + '()')
def beforeLog(name, value = None): print('*** I\'m going to call ' + name + '()')
def afterPostCondition(name, value = None):
    print('*** the value the call should return is ' + name + '() :- ' + str(value))
def beforePreCondition(name, value = None):
    print('***' + name + '() has been called with ' + str(value))
    

def dec_after(method, log):
    def newmethod(self, *args):
        result = method(self, *args)
        log(method.__name__, result)
        return result
    newmethod.__name__ = method.__name__
    return newmethod

def dec_before(method, log):
    def newmethod(self, *args):
        log(method.__name__, args)
        return method(self, *args)
    newmethod.__name__ = method.__name__
    return newmethod
        

def weaving(Person, pca):
    class Meta(type):
        def __new__(meta, classname, supers, classdict):
            for m,log in pca:
                if m in classdict.keys():
                    if log.__name__.startswith('after'): classdict[m] = dec_after(classdict[m],log)
                    if log.__name__.startswith('before'): classdict[m] = dec_before(classdict[m],log)
            return type.__new__(meta, classname, supers, classdict)
    Person = Meta('Person', (), dict(Person.__dict__))
    return Person

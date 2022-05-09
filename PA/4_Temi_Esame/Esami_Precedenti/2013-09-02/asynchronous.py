import threading

class myThread(threading.Thread):
    def __init__(self, target=None, args=(), *other):
        self.mytarget = target
        super().__init__(target=self.target, args=args, *other)
    def target(self, *args):
        self.result = self.mytarget(*args)
    def is_done(self):
        return not self.is_alive()
    def get_result(self):
        if self.is_done():
            return self.result
        else:
            raise asynchronous.NotYetDoneException('the call has not yet complete')

def asynchronous(F):
    class myProcess:
        def start(self, *args):
            t = myThread(target=F, args=args)
            t.start()
            return t
    return myProcess()

class NotYetDoneException(Exception):
    def __init__(self, message):
        self.message = message

asynchronous.NotYetDoneException = NotYetDoneException

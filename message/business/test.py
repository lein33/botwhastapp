from threading import Thread
from business.aigenerations import *
class CustomThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={},Verbose=None):
        Thread.__init__(self,group,target,name,args,kwargs)
        self.__return = None
    
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,**self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return
def add(n1,n2):
    return "hellow world"

thread = CustomThread(target=add,args=(3,4))
thread.start()
print(thread.join())
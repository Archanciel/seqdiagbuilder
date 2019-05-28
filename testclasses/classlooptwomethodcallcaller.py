from testclasses.classlooptwomethodcall import ClassLoopTwoMethodCall

class ClassLoopTwoMethodCallCaller:
    '''
    ClassLoopTwoMethodCallCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopTwoMethodCall()
        b.doB(p1)

from testclasses.classlooponemethodcall import ClassLoopOneMethodCall

class ClassLoopOneMethodCallCaller:
    '''
    ClassLoopOneMethodCallCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopOneMethodCall()
        b.doB(p1)

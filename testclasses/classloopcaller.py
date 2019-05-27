from testclasses.classloop import ClassLoop

class ClassLoopCaller:
    '''
    ClassA is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoop()
        b.doB(p1)

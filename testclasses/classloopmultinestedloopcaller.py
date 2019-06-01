from testclasses.classloopmultinestedloop import ClassLoopMultiNestedLoop

class ClassLoopMultiNestedLoopCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoop()
        b.doB(p1)

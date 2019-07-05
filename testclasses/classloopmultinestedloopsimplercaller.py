from testclasses.classloopmultinestedloopsimpler import ClassLoopMultiNestedLoopSimpler

class ClassLoopMultiNestedLoopSimplerCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimpler()
        b.doB(p1)

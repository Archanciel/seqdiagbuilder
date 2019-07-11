from testclasses.classloopmultinestedloopsimplerwithloopendunderif import ClassLoopMultiNestedLoopSimplerWithLoopEndUnderIf

class ClassLoopMultiNestedLoopSimplerWithLoopEndUnderIfCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimplerWithLoopEndUnderIf()
        b.doB(p1)

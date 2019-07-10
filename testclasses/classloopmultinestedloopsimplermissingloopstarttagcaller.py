from testclasses.classloopmultinestedloopsimplermissingloopstarttag import ClassLoopMultiNestedLoopSimplerMissingLoopStartTag

class ClassLoopMultiNestedLoopSimplerMissingLoopStartTagCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimplerMissingLoopStartTag()
        b.doB(p1)

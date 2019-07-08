from testclasses.classloopmultinestedloopsimpler2missingloopstarttag import ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag

class ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag()
        b.doB(p1)

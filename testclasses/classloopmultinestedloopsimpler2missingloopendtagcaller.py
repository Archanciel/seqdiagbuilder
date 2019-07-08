from testclasses.classloopmultinestedloopsimpler2missingloopendtag import ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag

class ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag()
        b.doB(p1)

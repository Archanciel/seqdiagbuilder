from testclasses.classloopnestedinnerone import ClassLoopNestedInnerOne

class ClassLoopNestedInnerOneCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNestedInnerOne()
        b.doB(p1)

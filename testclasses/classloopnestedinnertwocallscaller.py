from testclasses.classloopnestedinnertwocalls import ClassLoopNestedInnerTwoCalls

class ClassLoopNestedInnerTwoCallsCaller:
    '''
    ClassLoopNestedInnerTwoCallsCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNestedInnerTwoCalls()
        b.doB(p1)

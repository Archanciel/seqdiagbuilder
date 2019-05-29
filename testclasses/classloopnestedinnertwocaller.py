from testclasses.classloopnestedinnertwo import ClassLoopNestedInnerTwo

class ClassLoopNestedInnerTwoCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNestedInnerTwo()
        b.doB(p1)

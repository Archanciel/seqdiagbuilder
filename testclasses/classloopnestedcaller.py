from testclasses.classloopnested import ClassLoopNested

class ClassLoopNestedCaller:
    '''
    ClassA is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopNested()
        b.doB(p1)

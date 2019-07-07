from testclasses.classloopthreenestedloop import ClassLoopThreeNestedLoop

class ClassLoopThreeNestedLoopCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopThreeNestedLoop()
        b.doB(p1)

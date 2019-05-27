from testclasses.classtwoloops import ClassTwoLoops

class ClassTwoLoopsCaller:
    '''
    ClassA is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassTwoLoops()
        b.doB(p1)

from testclasses.classloopmultinestedloopsimpler2 import ClassLoopMultiNestedLoopSimpler2

class ClassLoopMultiNestedLoopSimplerCaller2:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopSimpler2()
        b.doB(p1)

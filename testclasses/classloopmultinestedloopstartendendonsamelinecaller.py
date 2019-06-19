from testclasses.classloopmultinestedloopstartendendonsameline import ClassLoopMultiNestedLoopStartEndEndOnSameLine

class ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller:
    '''
    ClassLoopNestedCaller is the entry point of our sequence diagram.
    '''

    def call(self, p1):
        '''
        call() is the entry method of our sequence diagram.
        '''
        b = ClassLoopMultiNestedLoopStartEndEndOnSameLine()
        b.doB(p1)

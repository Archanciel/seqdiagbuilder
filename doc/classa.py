from doc.classb import ClassB

class ClassA:
    '''
    ClassA is the entry point of our sequence diagram.
    '''

    def doA(self, p1):
        '''
        doWork() is the entry method of our sequence diagram.
        '''
        b = ClassB()
        b.doB(p1)

from testclasses.classleaf import ClassLeaf

class ClassMidLoop:
    def doMidLoop1(self, p1):
        '''
        Method with intermediate loop.
        '''
        c = ClassLeaf()
        a = 0

        for i in range(2):
            c.doC1(p1) #:seqdiag_loop_start 2 times
            a += 1 # dummy instruction
            c.doC2(p1) #:seqdiag_loop_end

    def doMidLoopSimple(self, p1):
        '''
        Method with intermediate loop calling simple leaf methods.
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC1(p1) #:seqdiag_loop_start 3 times
            a += 1 # dummy instruction
            c.doC2(p1) #:seqdiag_loop_end

    def doMidLoopLeafLoop(self, p1):
        '''
        Method with intermediate loop calling leaf class methods with loop.
        '''
        c = ClassLeaf()
        a = 0

        for i in range(2):
            c.doCLoop(p1)  #:seqdiag_loop_start 2 times
            a += 1  # dummy instruction
            c.doCLoopStartEnd(p1)  #:seqdiag_loop_end

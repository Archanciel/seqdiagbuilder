from testclasses.classleaf import ClassLeaf

class ClassTwoLoops:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop and
        :seqdiag loop end tags when more than one loop is declared in
        the same method.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            #:seqdiag_loop 3 times
            c.doC1(p1)
            a += 1 # dummy instruction
            c.doC2(p1)
            #:seqdiag_loop_end

        for i in range(6):
            #:seqdiag_loop 6 times
            c.doC1(p1)
            a += 1 # dummy instruction
            c.doC2(p1)
            #:seqdiag_loop_end

        print(a) # another dummy instruction
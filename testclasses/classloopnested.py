from testclasses.classleaf import ClassLeaf

class ClassLoopNested:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop and
        :seqdiag loop end tags with two nested loops.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            #:seqdiag_loop 3 times
            a += 1 # dummy instruction
            #:seqdiag_loop 5 times
            for i in range(5):
                c.doC1(p1)
                a += 1 # dummy instruction
            #:seqdiag_loop_end
            a += 1 # dummy instruction
            c.doC2(p1)
            a += 1 # dummy instruction
            #:seqdiag_loop_end

        print(a) # another dummy instruction
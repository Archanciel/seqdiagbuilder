from testclasses.classleaf import ClassLeaf

class ClassLoopMultiNestedLoopStartEndEndOnSameLine:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop start end and
        :seqdiag loop end tags located on the same line.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(2):
            a += 1 # dummy instruction
            for i in range(3):
                c.doC1(p1) #:seqdiag_loop_start 3 times :seqdiag_loop_start_end 2 times
                a += 1 # dummy instruction
            a += 1 # dummy instruction
            for j in range(2):
                c.doC2(p1) #:seqdiag_loop_start_end 2 times :seqdiag_loop_end
            a += 1 # dummy instruction

        c.doC3(p1)

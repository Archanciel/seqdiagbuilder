from testclasses.classleaf import ClassLeaf

class ClassLoopTwoMethodCall:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop and
        :seqdiag loop end tags with a loop inside which two methods are
        called.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC1(p1) #:seqdiag_loop_start 3 times
            a += 1 # dummy instruction
            c.doC2(p1) #:seqdiag_loop_end

        print(a) # another dummy instruction
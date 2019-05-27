from testclasses.classleaf import ClassLeaf

class ClassLoop:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag_loop and
        :seqdiag_loop_end tags.
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
            #:seqdiag_loop  end

        print(a) # another dummy instruction
from testclasses.classleaf import ClassLeaf

class ClassLoopNestedInnerTwoCalls:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop and
        :seqdiag loop end tags with two nested loops. The nested loop contains
        two calls to a leaf method.
        :seqdiag_note method doB note
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            a += 1 # dummy instruction
            c.doC3(p1) #:seqdiag_loop_start 3 times
            for i in range(5):
                c.doC1(p1) #:seqdiag_loop_start 5 times
                a += 1 # dummy instruction
                c.doC1(p1)  #:seqdiag_loop_end
            a += 1 # dummy instruction
            c.doC2(p1) #:seqdiag_loop_end
            a += 1 # dummy instruction

        c.doC1(p1)
        print(a) # another dummy instruction
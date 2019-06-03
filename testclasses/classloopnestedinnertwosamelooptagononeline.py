from testclasses.classleaf import ClassLeaf

class ClassLoopNestedInnerTwoSameLoopTagOnOneLine:
    '''
    This class is used to test the handling of the :seqdiag start end loop
    tag with two nested loops calling only one leaf method. To achieve this,
    2 loop start end tags are located on the same instruction line.
    '''

    def doB(self, p1):
        c = ClassLeaf()
        a = 0

        for i in range(3):
            a += 1 # dummy instruction
            for i in range(5):
                c.doCWithNote(p1) #:seqdiag_loop_start_end 3 times :seqdiag_loop_start_end 5 times

        c.doC1(p1)

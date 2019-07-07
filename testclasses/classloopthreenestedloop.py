from testclasses.classleaf import ClassLeaf

class ClassLoopThreeNestedLoop:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop start end
        tag with three nested loops. The nested loop contains a call to a method
        which call a method which does not contain any loop.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(2):
            for j in range(3):
                for k in range(4):
                    c.doC3(p1) #:seqdiag_loop_start_end 2 times :seqdiag_loop_start_end 3 times :seqdiag_loop_start_end 4 times


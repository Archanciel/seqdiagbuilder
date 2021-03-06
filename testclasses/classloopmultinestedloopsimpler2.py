from testclasses.classMidLoop import ClassMidLoop

class ClassLoopMultiNestedLoopSimpler2:
    def doB(self, p1):
        '''
        This class is used to test the handling of the :seqdiag loop and
        :seqdiag loop end tags with two nested loops. The nested loop contains
        a call to a method which itself causes nested loops to occur.
        :param p1:
        :return:
        '''
        c = ClassMidLoop()
        a = 0

        for i in range(2):
            a += 1 # dummy instruction
            for i in range(3):
                c.doMidLoopLeafLoop(p1) #:seqdiag_loop_start_end 2 times :seqdiag_loop_start_end 3 times
                a += 1 # dummy instruction

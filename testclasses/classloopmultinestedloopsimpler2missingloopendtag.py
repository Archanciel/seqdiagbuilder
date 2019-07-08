from testclasses.classMidLoop import ClassMidLoop

class ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag:
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
              # nxt line contains an error in the loop tagging: seqdiag loop start 2 times is used
              # instead of seqdiag loop start end 2 times !
                c.doMidLoopLeafLoop(p1) #:seqdiag_loop_start 2 times :seqdiag_loop_start_end 3 times
                a += 1 # dummy instruction

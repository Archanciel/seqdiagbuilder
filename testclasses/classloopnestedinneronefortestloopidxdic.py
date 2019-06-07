from testclasses.classleaf import ClassLeaf

class ClassLoopNestedInnerOneForTestLoopIdxDic:
    '''
    This class is used to test the LoopIndexDictionary. The loop tag have
    no time info.

    '''

    def doB(self, p1):
        c = ClassLeaf()
        a = 0

        for i in range(3):
            a += 1 # dummy instruction
            for i in range(5):
                c.doCWithNote(p1) #:seqdiag_loop_start 3 times :seqdiag_loop_start_end 5 times
                a += 1 # dummy instruction
            a += 1 # dummy instruction
            c.doC2(p1) #:seqdiag_loop_end
            a += 1 # dummy instruction

        c.doC1(p1)
        print(a) # another dummy instruction
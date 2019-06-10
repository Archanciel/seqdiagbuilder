from testclasses.classleaf import ClassLeaf

class ClassLoopTagOnMethodNotInRecordFlow:
    def doLoopStartAndLoopEndOnNotRecordedMethodCall(self, p1):
        '''
        This method is used to test the handling of the :seqdiag loop start
        and :seqdiag loop end placed on a method which is not monitored by the
        SeqDiagBuilder.recordFlow() static method.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC4NotRecordedInFlow(p1) #:seqdiag_loop_start 3 times
            a += 1 # dummy instruction
            c.doC4NotRecordedInFlow(p1) #:seqdiag_loop_end

        c.doC2(p1)

    def doLoopStartEndOnNotRecordedMethodCall(self, p1):
        '''
        This method is used to test the handling of the :seqdiag loop start end
        tag placed on a method which is not monitored by the
        SeqDiagBuilder.recordFlow() static method.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC4NotRecordedInFlow(p1) #:seqdiag_loop_start_end 3 times
            a += 1 # dummy instruction

        c.doC2(p1)

    def doLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall(self, p1):
        '''
        This method is used to test the handling of the :seqdiag loop start
        put on a call to a method recorded by the SeqDiagBuilder.recordFlow()
        static method and the corresponding :seqdiag loop end placed on a
        method which is not monitored by the SeqDiagBuilder.recordFlow() static
        method.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC4NotRecordedInFlow(p1) #:seqdiag_loop_start 3 times
            a += 1 # dummy instruction
            c.doC1(p1) #:seqdiag_loop_end

        c.doC2(p1)

    def doLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall(self, p1):
        '''
        This method is used to test the handling of the :seqdiag loop start
        put on a call to a method not recorded by the SeqDiagBuilder.recordFlow()
        static method and the corresponding :seqdiag loop end placed on a
        method which is monitored by the SeqDiagBuilder.recordFlow() satic
        method.
        :param p1:
        :return:
        '''
        c = ClassLeaf()
        a = 0

        for i in range(3):
            c.doC1(p1)  #:seqdiag_loop_start 3 times
            a += 1  # dummy instruction
            c.doC4NotRecordedInFlow(p1)  #:seqdiag_loop_end

        c.doC2(p1)

from seqdiagbuilder import SeqDiagBuilder

class ClassLeaf:
    def doC1(self, p1):
        '''
        This the first leaf method of our sequence diagram.
        '''

        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        SeqDiagBuilder.recordFlow()

    def doC2(self, p1):
        '''
        This the second leaf method of our sequence diagram.
        '''

        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        SeqDiagBuilder.recordFlow()

    def doC3(self, p1):
        '''
        This the third leaf method of our sequence diagram.
        :seqdiag_note doC3 method note
        '''

        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        SeqDiagBuilder.recordFlow()

    def doCWithNote(self, p1):
        '''
        This the first leaf method of our sequence diagram.
        :seqdiag_note doCWithNote method note
        '''

        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        SeqDiagBuilder.recordFlow()

    def doCLoop(self, p1):
        '''
        This the 4th leaf method of our sequence diagram.
        :seqdiag_note doCLoop method note
        '''
        a = 0

        for i in range(2):
            self.doC1(p1) #:seqdiag_loop_start 2 times
            a += 1 # dummy instruction
            self.doC2(p1) #:seqdiag_loop_end

    def doCLoopStartEnd(self, p1):
        '''
        This the 5th leaf method of our sequence diagram.
        :seqdiag_note doCLoopStartEnd method note
        '''
        a = 0

        for i in range(3):
            self.doC1(p1)  #:seqdiag_loop_start_end 3 times
            a += 1  # dummy instruction

    def doC4NotRecordedInFlow(self, p1):
        '''
        This method is not monitored by SeqDiagBuilder.recordFlow(). It
        is used to test putting a seqdiag loop command on a method call
        not monitored by SeqDiagBuilder.
        :seqdiag_note doC4NotRecordedInFlow method note
        '''
        a = 0
        a += 1
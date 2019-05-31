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

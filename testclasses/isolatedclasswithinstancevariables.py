from seqdiagbuilder import SeqDiagBuilder

if __name__ == '__main__':
    pass


class IsolatedClassWithInstanceVariables:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def analyse(self):
        '''

        :seqdiag_return Analysis
        :return:
        '''
        SeqDiagBuilder.recordFlow(3)
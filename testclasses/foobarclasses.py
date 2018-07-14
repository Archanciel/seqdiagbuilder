from seqdiagbuilder import SeqDiagBuilder

if __name__ == '__main__':
    pass


class Foo:
    def f(self, fParm):
        '''

        :param fParm:
        :seqdiag_return fReturn
        :return:
        '''
        b = Bar()
        e = Egg()

        b.g()
        e.h(1, 2)


class Bar:
    def g(self):
        '''

        :seqdiag_return gReturn
        :return:
        '''
        lo = LeafOne()
        lo.i()


class Egg:
    def h(self, hParm1, hParm2):
        lt = LeafTwo()
        lt.j()


class LeafOne:
    def i(self):
        SeqDiagBuilder.recordFlow()


class LeafTwo:
    def j(self):
        SeqDiagBuilder.recordFlow()
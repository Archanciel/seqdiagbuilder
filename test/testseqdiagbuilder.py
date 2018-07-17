import unittest
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone

from testclasses.isolatedclass import IsolatedClass
from testclasses.subtestpackage.isolatedclasssub import IsolatedClassSub
from testclasses.isolatedclasswithinstancevariables import IsolatedClassWithInstanceVariables
from testclasses.foobarclasses import *
from testclasses.subtestpackage.dsub import DSub
from testclasses.subtestpackage.caller import Caller


#from controller import Controller
#from pricerequester import PriceRequester


class Client:
    def do(self):
        c1 = ChildOne()
        c1.getCoordinate()


    def make(self):
        c1 = ChildOne()
        c1.compute()


    def perform(self):
        c1 = ChildOne()
        c1.computeTwo()


    def doCall(self):
        c1 = ChildOne()
        c1.computeThree()


    def doProcess(self):
        c1 = ChildOfChildTwo()
        c1.computeFour()


class Parent:
    def getCoordinate(self, location=''):
        '''

        :param location:
        :seqdiag_return Coord
        :return:
        '''
        SeqDiagBuilder.recordFlow()


    def getCoordinateNoneSelected(self, location=''):
        '''

        :param location:
        :seqdiag_return Coord
        :return:
        '''
        SeqDiagBuilder.recordFlow()


    def compute(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_return Analysis
        :return:
        '''
        pass


    def computeTwo(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_select_method
        :seqdiag_return Analysis
        :return:
        '''
        pass


    def computeThree(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_select_method
        :seqdiag_return Analysis
        :return:
        '''
        iso = IsolatedClass()
        iso.analyse()


    def computeFour(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_return Analysis
        :return:
        '''
        pass

    def inheritedMethod(self, inhArg):
        '''
        This a dummy merhod.
        :seqdiag_return inhMethResult
        :return:
        '''
        SeqDiagBuilder.recordFlow()


class ChildOne(Parent):
    def getCoordinate(self, location=''):
        iso = IsolatedClass()
        iso.analyse()

    def getCoordinateNoneSelected(self, location=''):
        iso = IsolatedClass()
        iso.analyse()

    def m(self):
        pass


    def compute(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_select_method
        :seqdiag_return Analysis
        :return:
        '''
        super().compute(size)
        iso = IsolatedClass()
        iso.analyse()


    def computeTwo(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_select_method
        :seqdiag_return Analysis
        :return:
        '''
        super().compute(size)
        iso = IsolatedClass()
        iso.analyse()


class ChildTwo(Parent):
    def l(self):
        pass


    def computeFour(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_select_method
        :seqdiag_return Analysis
        :return:
        '''
        iso = IsolatedClass()
        iso.analyse()


    def getCoordinateNoneSelected(self, location=''):
        SeqDiagBuilder.recordFlow()


class ChildThree(Parent):
    def getCoordinate(self, location=''):
        '''

        :param location:
        :seqdiag_return CoordSel
        :seqdiag_select_method
        :return:
        '''
        SeqDiagBuilder.recordFlow()


class ChildOfChildTwo(Parent):
    def l(self):
        pass


    def computeFour(self, size = 0):
        '''
        This a dummy merhod.
        :seqdiag_return Analysis
        :return:
        '''
        iso = IsolatedClass()
        iso.analyse()


class ClassA:
    def doWork(self):
        '''
        :seqdiag_return ClassAdoWorkRes
        :return:
        '''
        self.internalCall()


    def internalCall(self):
        '''
        :seqdiag_return ResultPrice
        :return:
        '''
        pr = self.internalInnerCall()
        b = ClassB()
        res = b.createRequest(1, 2)


    def internalInnerCall(self):
        '''
        :seqdiag_return ResultPrice
        :return:
        '''
        b = ClassB()
        res = b.createInnerRequest(1)

    def aMethod(self, aMarg):
        '''
        :seqdiag_return ResultAmeth
        :return:
        '''
        child = ChildTwo()
        child.inheritedMethod(aMarg)


class ClassB:
    def createInnerRequest(self, parm1):
        '''
        :seqdiag_return Bool
        :param parm1:
        :return:
        '''
        SeqDiagBuilder.recordFlow()


    def createRequest(self, parm1, parm2):
        '''
        :seqdiag_return Bool
        :param parm1:
        :return:
        '''
        SeqDiagBuilder.recordFlow()


class C:
    def c1(self, c1_p1):
        '''

        :param c1_p1:
        :seqdiag_return Cc1Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def c2(self, c2_p1):
        '''

        :param c2_p1:
        :seqdiag_return Cc2Return
        :return:
        '''
        d = DSub()
        d.d1(1)
    def c3(self, c3_p1):
        '''

        :param c3_p1:
        :seqdiag_return Cc3Return
        :return:
        '''
        d = DSub()
        d.d2(1)
        SeqDiagBuilder.recordFlow()
        self.c4(1)
    def c4(self, c4_p1):
        '''

        :param c4_p1:
        :seqdiag_return Cc4Return
        :return:
        '''
        d = DSub()
        d.d2(1)
        SeqDiagBuilder.recordFlow()
    def c5(self, c5_p1):
        '''

        :param c5_p1:
        :seqdiag_return Cc5Return
        :return:
        '''
        d = DSub()
        d.d3(1)
    def fibonaci(self, number):
        '''

        :param number:
        :seqdiag_return CfibonaciReturn
        :return:
        '''
        if number == 1:
            SeqDiagBuilder.recordFlow()
            return 1
        else:
            return number + self.fibonaci(number - 1)

class B:
    def b0(self, b1_p1):
        '''

        :param b1_p1:
        :seqdiag_return Bb1Return
        :return:
        '''
        pass
    def b1(self, b1_p1):
        '''

        :param b1_p1:
        :seqdiag_return Bb1Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def b2(self, b2_p1):
        '''

        :param b2_p1:
        :seqdiag_return Bb2Return
        :return:
        '''
        c = C()
        c.c1(1)
    def b3(self, b3_p1):
        '''

        :param b3_p1:
        :seqdiag_return Bb3Return
        :return:
        '''
        c = C()
        c.c1(1)
        c.c1(1)
    def b4(self, b4_p1):
        '''

        :param b4_p1:
        :seqdiag_return Bb4Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def b5(self, b5_p1):
        '''

        :param b5_p1:
        :seqdiag_return Bb5Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def b6(self, b6_p1):
        '''

        :param b6_p1:
        :seqdiag_return Bb6Return
        :return:
        '''
        c = C()
        c.c2(1)
    def b7(self, b7_p1):
        '''

        :param b7_p1:
        :seqdiag_return Bb7Return
        :return:
        '''
        c = C()
        c.c3(1)
        SeqDiagBuilder.recordFlow()
        d = DSub()
        d.d2(1)
    def b8(self, b8_p1):
        '''

        :param b8_p1:
        :seqdiag_return Bb8Return
        :return:
        '''
        c = C()
        c.c5(1)
        d = DSub()
        d.d2(1)

class A:
    def a0(self, a1_p1, a1_p2):
        '''
        :param a1_p1:
        :param a1_p2:
        :seqdiag_return Aa1Return
        :return:
        '''
        pass
    def a1(self, a1_p1, a1_p2):
        '''
        :param a1_p1:
        :param a1_p2:
        :seqdiag_return Aa1Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def a2(self, a2_p1):
        '''
        :param a2_p1:
        :seqdiag_return Aa2Return
        :return:
        '''
        b = B()
        b.b1(1)
    def a3(self, a3_p1):
        '''
        :param a3_p1:
        :seqdiag_return Aa3Return
        :return:
        '''
        b = B()
        b.b2(1)
    def a4(self, a4_p1):
        '''
        :param a4_p1:
        :seqdiag_return Aa4Return
        :return:
        '''
        b = B()
        b.b1(1)
        b.b1(1)
    def a5(self, a5_p1):
        '''
        :param a5_p1:
        :seqdiag_return Aa5Return
        :return:
        '''
        b = B()
        b.b1(1)
        b.b1(1)
        b.b1(1)
    def a6(self, a6_p1):
        '''
        :param a6_p1:
        :seqdiag_return Aa6Return
        :return:
        '''
        b = B()
        b.b2(1)
        b.b2(1)
    def a7(self, a7_p1):
        '''
        :param a7_p1:
        :seqdiag_return Aa6Return
        :return:
        '''
        b = B()
        b.b3(1)
    def a8(self, a8_p1, a8_p2):
        '''
        :param a8_p1:
        :param a8_p2:
        :seqdiag_return Aa8Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def a9(self, a9_p1):
        '''
        :param a9_p1:
        :seqdiag_return Aa9Return
        :return:
        '''
        SeqDiagBuilder.recordFlow()
    def a10(self, a10_p1):
        '''
        :param a10_p1:
        :seqdiag_return Aa10Return
        :return:
        '''
        b = B()
        b.b4(1)
        b.b5(1)
    def a11(self, a11_p1):
        '''
        :param a11_p1:
        :seqdiag_return Aa11Return
        :return:
        '''
        b = B()
        b.b6(1)
        b.b6(1)
    def a12(self, a12_p1):
        '''
        :param a12_p1:
        :seqdiag_return Aa12Return
        :return:
        '''
        b = B()
        b.b7(1)
        b.b7(1)
        SeqDiagBuilder.recordFlow()
    def a13(self, a13_p1):
        '''
        :param a13_p1:
        :seqdiag_return Aa13Return
        :return:
        '''
        b = B()
        b.b8(1)
        b.b8(1)


class TestSeqDiagBuilder(unittest.TestCase):
    def setUp(self):
        self.projectPath = 'D:\\Development\\Python\\seqdiagbuilder'

        SeqDiagBuilder.deactivate()


    def testCreateSeqDiagCommandsOnSimplestCallWithoutRecordFlowCallInLeafMethod(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a0')  # activate sequence diagram building
        entryPoint.a0(1, 2)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)
        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  No control flow recorded.</font></b>
<b><font color=red size=14>  Method activate() called: True.</font></b>
<b><font color=red size=14>  Method recordFlow() called: False.</font></b>
<b><font color=red size=14>  Specified entry point: A.a0 reached: False.</font></b>
endheader

actor USER

@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnSimplestCall(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a1')  # activate sequence diagram building
        entryPoint.a1(1, 2)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
	USER -> A: a1(a1_p1, a1_p2)
		activate A
		USER <-- A: return Aa1Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testCreateSeqDiagCommandsTwoLevelCallTwoDiffMethods(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a10')  # activate sequence diagram building
        entryPoint.a10(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
	USER -> A: a10(a10_p1)
		activate A
		A -> B: b4(b4_p1)
			activate B
			A <-- B: return Bb4Return
			deactivate B
		A -> B: b5(b5_p1)
			activate B
			A <-- B: return Bb5Return
			deactivate B
		USER <-- A: return Aa10Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testCreateSeqDiagCommandsOnTwoLevelCall(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a2')  # activate sequence diagram building
        entryPoint.a2(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
	USER -> A: a2(a2_p1)
		activate A
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		USER <-- A: return Aa2Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnThreeLevelCallingMidLevelMethodTwice(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a6')  # activate sequence diagram building
        entryPoint.a6(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
	USER -> A: a6(a6_p1)
		activate A
		A -> B: b2(b2_p1)
			activate B
			B -> C: c1(c1_p1)
				activate C
				B <-- C: return Cc1Return
				deactivate C
			A <-- B: return Bb2Return
			deactivate B
		A -> B: b2(b2_p1)
			activate B
			B -> C: c1(c1_p1)
				activate C
				B <-- C: return Cc1Return
				deactivate C
			A <-- B: return Bb2Return
			deactivate B
		USER <-- A: return Aa6Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnFiveLevelCallingSecondLevelMethodTwice(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a11')  # activate sequence diagram building
        entryPoint.a11(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
participant DSub
	USER -> A: a11(a11_p1)
		activate A
		A -> B: b6(b6_p1)
			activate B
			B -> C: c2(c2_p1)
				activate C
				C -> DSub: d1(d1_p1)
					activate DSub
					C <-- DSub: return Dd1Return
					deactivate DSub
				B <-- C: return Cc2Return
				deactivate C
			A <-- B: return Bb6Return
			deactivate B
		A -> B: b6(b6_p1)
			activate B
			B -> C: c2(c2_p1)
				activate C
				C -> DSub: d1(d1_p1)
					activate DSub
					C <-- DSub: return Dd1Return
					deactivate DSub
				B <-- C: return Cc2Return
				deactivate C
			A <-- B: return Bb6Return
			deactivate B
		USER <-- A: return Aa11Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnFiveLevelCallingSecondLevelMethodTwiceProjectPathUnixLike(self):
            entryPoint = A()

            SeqDiagBuilder.activate(self.projectPath.replace('\\','/'), 'A', 'a11')  # activate sequence diagram building
            entryPoint.a11(1)

            commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

            self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

            with open("c:\\temp\\ess.txt", "w") as f:
                f.write(commands)

            self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
participant DSub
	USER -> A: a11(a11_p1)
		activate A
		A -> B: b6(b6_p1)
			activate B
			B -> C: c2(c2_p1)
				activate C
				C -> DSub: d1(d1_p1)
					activate DSub
					C <-- DSub: return Dd1Return
					deactivate DSub
				B <-- C: return Cc2Return
				deactivate C
			A <-- B: return Bb6Return
			deactivate B
		A -> B: b6(b6_p1)
			activate B
			B -> C: c2(c2_p1)
				activate C
				C -> DSub: d1(d1_p1)
					activate DSub
					C <-- DSub: return Dd1Return
					deactivate DSub
				B <-- C: return Cc2Return
				deactivate C
			A <-- B: return Bb6Return
			deactivate B
		USER <-- A: return Aa11Return
		deactivate A
@enduml''', commands)

            SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnFiveLevelCallingSecondLevelMethodTwiceWithRecordFlowInEveryMethod(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a12')  # activate sequence diagram building
        entryPoint.a12(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
participant DSub
	USER -> A: a12(a12_p1)
		activate A
		A -> B: b7(b7_p1)
			activate B
			B -> C: c3(c3_p1)
				activate C
				C -> DSub: d2(d2_p1)
					activate DSub
					C <-- DSub: return Dd2Return
					deactivate DSub
				C -> C: c4(c4_p1)
					activate C
					C -> DSub: d2(d2_p1)
						activate DSub
						C <-- DSub: return Dd2Return
						deactivate DSub
					C <-- C: return Cc4Return
					deactivate C
				B <-- C: return Cc3Return
				deactivate C
			B -> DSub: d2(d2_p1)
				activate DSub
				B <-- DSub: return Dd2Return
				deactivate DSub
			A <-- B: return Bb7Return
			deactivate B
		A -> B: b7(b7_p1)
			activate B
			B -> C: c3(c3_p1)
				activate C
				C -> DSub: d2(d2_p1)
					activate DSub
					C <-- DSub: return Dd2Return
					deactivate DSub
				C -> C: c4(c4_p1)
					activate C
					C -> DSub: d2(d2_p1)
						activate DSub
						C <-- DSub: return Dd2Return
						deactivate DSub
					C <-- C: return Cc4Return
					deactivate C
				B <-- C: return Cc3Return
				deactivate C
			B -> DSub: d2(d2_p1)
				activate DSub
				B <-- DSub: return Dd2Return
				deactivate DSub
			A <-- B: return Bb7Return
			deactivate B
		USER <-- A: return Aa12Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testCreateSeqDiagCommandsOnFiveLevelCallingSecondLevelMethodTwiceWithRecordFlowInOnePlaceOnly(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a13')  # activate sequence diagram building
        entryPoint.a13(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant DSub
	USER -> A: a13(a13_p1)
		activate A
		A -> B: b8(b8_p1)
			activate B
			B -> DSub: d2(d2_p1)
				activate DSub
				B <-- DSub: return Dd2Return
				deactivate DSub
			A <-- B: return Bb8Return
			deactivate B
		A -> B: b8(b8_p1)
			activate B
			B -> DSub: d2(d2_p1)
				activate DSub
				B <-- DSub: return Dd2Return
				deactivate DSub
			A <-- B: return Bb8Return
			deactivate B
		USER <-- A: return Aa13Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnThreeLevelCallingLastLevelMethodTwice(self):
        '''
        Calling two level deep method which calls last Level method twice
        :return:
        '''
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a7')  # activate sequence diagram building
        entryPoint.a7(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
	USER -> A: a7(a7_p1)
		activate A
		A -> B: b3(b3_p1)
			activate B
			B -> C: c1(c1_p1)
				activate C
				B <-- C: return Cc1Return
				deactivate C
			B -> C: c1(c1_p1)
				activate C
				B <-- C: return Cc1Return
				deactivate C
			A <-- B: return Bb3Return
			deactivate B
		USER <-- A: return Aa6Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnTwoLevelCallCallingMethodTwice(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a4')  # activate sequence diagram building
        entryPoint.a4(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
	USER -> A: a4(a4_p1)
		activate A
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		USER <-- A: return Aa4Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnTwoLevelCallCallingMethodThreeTimes(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a5')  # activate sequence diagram building
        entryPoint.a5(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
	USER -> A: a5(a5_p1)
		activate A
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		A -> B: b1(b1_p1)
			activate B
			A <-- B: return Bb1Return
			deactivate B
		USER <-- A: return Aa5Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnThreeLevelCall(self):
        entryPoint = A()

        SeqDiagBuilder.activate(self.projectPath, 'A', 'a3')  # activate sequence diagram building
        entryPoint.a3(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant A
participant B
participant C
	USER -> A: a3(a3_p1)
		activate A
		A -> B: b2(b2_p1)
			activate B
			B -> C: c1(c1_p1)
				activate C
				B <-- C: return Cc1Return
				deactivate C
			A <-- B: return Bb2Return
			deactivate B
		USER <-- A: return Aa3Return
		deactivate A
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def test_instanciateClassInitTwoArgs(self):
        className = 'IsolatedClassWithInstanceVariables'
        packageSpec = 'testclasses.'
        moduleName = 'isolatedclasswithinstancevariables'

        instance = SeqDiagBuilder._instanciateClass(className, packageSpec, moduleName)

        self.assertIsInstance(instance, IsolatedClassWithInstanceVariables)


    def test_instanciateClassInitNoArgs(self):
        className = 'IsolatedClass'
        packageSpec = 'testclasses.'
        moduleName = 'isolatedclass'

        instance = SeqDiagBuilder._instanciateClass(className, packageSpec, moduleName)

        self.assertIsInstance(instance, IsolatedClass)


    def test_instanciateClassInitNoArgsSubPackageSpec(self):
        className = 'IsolatedClassSub'
        packageSpec = 'testclasses.subtestpackage.'
        moduleName = 'isolatedclasssub'

        instance = SeqDiagBuilder._instanciateClass(className, packageSpec, moduleName)

        self.assertIsInstance(instance, IsolatedClassSub)


    def test_instanciateClassInitNoArgsEmptyPackageSpec(self):
        className = 'Client'
        packageSpec = ''
        moduleName = 'testseqdiagbuilder'

        instance = SeqDiagBuilder._instanciateClass(className, packageSpec, moduleName)

        self.assertIsInstance(instance, Client)


    def test_instanciateClassInitNoArgsEmptyPackageSpecClassInProjectRoot(self):
        className = 'SeqDiagBuilder'
        packageSpec = ''
        moduleName = 'seqdiagbuilder'

        instance = SeqDiagBuilder._instanciateClass(className, packageSpec, moduleName)

        self.assertIsInstance(instance, SeqDiagBuilder)


    def testRecordFlowWhereMulitpleClassesSupportSameMethodAndOneIsSelected(self):
        entryPoint = ChildThree()

        SeqDiagBuilder.activate(self.projectPath, 'ChildThree', 'getCoordinate')  # activate sequence diagram building
        entryPoint.getCoordinate()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant ChildThree
	USER -> ChildThree: getCoordinate(location='')
		activate ChildThree
		USER <-- ChildThree: return CoordSel
		deactivate ChildThree
@enduml''', commands)

        SeqDiagBuilder.deactivate()


    def testRecordFlowWhereMulitpleClassesSupportSameMethodAndOneIsSelectedInOtherClass(self):
        entryPoint = ChildTwo()

        SeqDiagBuilder.activate(self.projectPath, 'ChildTwo', 'getCoordinate')  # activate sequence diagram building
        entryPoint.getCoordinate()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  No control flow recorded.</font></b>
<b><font color=red size=14>  Method activate() called: True.</font></b>
<b><font color=red size=14>  Method recordFlow() called: True.</font></b>
<b><font color=red size=14>  Specified entry point: ChildTwo.getCoordinate reached: False.</font></b>
endheader

actor USER

@enduml''', commands)

        SeqDiagBuilder.deactivate()


    def testRecordFlowWhereMulitpleClassesSupportSameMethodAndNoneIsSelected(self):
        entryPoint = ChildTwo()

        SeqDiagBuilder.activate(self.projectPath, 'ChildTwo', 'getCoordinateNoneSelected')  # activate sequence diagram building
        entryPoint.getCoordinateNoneSelected()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=20> 1</font></b>
<b><font color=red size=14>  More than one class ['Parent', 'ChildOne', 'ChildTwo', 'ChildThree', 'ChildOfChildTwo'] found in module testseqdiagbuilder do support method getCoordinateNoneSelected(location='').</font></b>
<b><font color=red size=14>  Since Python provides no way to determine the exact target class, class Parent was chosen by default for building the sequence diagram.</font></b>
<b><font color=red size=14>  To override this selection, put tag :seqdiag_select_method somewhere in the target method documentation or define every class of the hierarchy in its own file.</font></b>
<b><font color=red size=14>  See help for more information.</font></b>
<b><font color=red size=20> 2</font></b>
<b><font color=red size=14>  No control flow recorded.</font></b>
<b><font color=red size=14>  Method activate() called: True.</font></b>
<b><font color=red size=14>  Method recordFlow() called: True.</font></b>
<b><font color=red size=14>  Specified entry point: ChildTwo.getCoordinateNoneSelected reached: False.</font></b>
endheader

actor USER

@enduml''', commands)

        SeqDiagBuilder.deactivate()

    def testRecordFlowWhereMulitpleClassesSupportInheritedMethodAndNoneIsSelected(self):
        entryPoint = ClassA()

        SeqDiagBuilder.activate(self.projectPath, 'ClassA', 'aMethod')  # activate sequence diagram building
        entryPoint.aMethod(1)

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  More than one class ['Parent', 'ChildOne', 'ChildTwo', 'ChildThree', 'ChildOfChildTwo'] found in module testseqdiagbuilder do support method inheritedMethod(inhArg).</font></b>
<b><font color=red size=14>  Since Python provides no way to determine the exact target class, class Parent was chosen by default for building the sequence diagram.</font></b>
<b><font color=red size=14>  To override this selection, put tag :seqdiag_select_method somewhere in the target method documentation or define every class of the hierarchy in its own file.</font></b>
<b><font color=red size=14>  See help for more information.</font></b>
endheader


actor USER
participant TestSeqDiagBuilder
participant ClassA
participant Parent
	USER -> ClassA: aMethod(aMarg)
		activate ClassA
		ClassA -> Parent: inheritedMethod(inhArg)
			activate Parent
			ClassA <-- Parent: return inhMethResult
			deactivate Parent
		USER <-- ClassA: return ResultAmeth
		deactivate ClassA
@enduml''', commands)

        SeqDiagBuilder.deactivate()


    def testCreateSeqDiagCommandsOnFullRequestHistoDayPrice(self):
        if not 'CryptoPricer' in self.projectPath:
            return

        from datetimeutil import DateTimeUtil
        from utilityfortest import UtilityForTest
        from configurationmanager import ConfigurationManager
        from guioutputformater import GuiOutputFormater
        from controller import Controller

        SeqDiagBuilder.activate(self.projectPath, 'Controller', 'getPrintableResultForInput')  # activate sequence diagram building

        if os.name == 'posix':
            FILE_PATH = '/sdcard/cryptopricer.ini'
        else:
            FILE_PATH = 'c:\\temp\\cryptopricer.ini'

        configMgr = ConfigurationManager(FILE_PATH)
        self.controller = Controller(GuiOutputFormater(configMgr), configMgr)

        timezoneStr = 'Europe/Zurich'
        now = DateTimeUtil.localNow(timezoneStr)
        eightDaysBeforeArrowDate = now.shift(days=-8)

        eightDaysBeforeYearStr, eightDaysBeforeMonthStr, eightDaysBeforeDayStr, eightDaysBeforeHourStr, eightDaysBeforeMinuteStr = UtilityForTest.getFormattedDateTimeComponentsForArrowDateTimeObj(eightDaysBeforeArrowDate)

        requestYearStr = eightDaysBeforeYearStr
        requestDayStr = eightDaysBeforeDayStr
        requestMonthStr = eightDaysBeforeMonthStr
        inputStr = 'eth btc {}/{} all'.format(requestDayStr, requestMonthStr)
        printResult, fullCommandStr, fullCommandStrWithOptions, fullCommandStrWithSaveModeOptions = self.controller.getPrintableResultForInput(
            inputStr)

        if DateTimeUtil.isDateOlderThan(eightDaysBeforeArrowDate, 7):
            hourStr = '00'
            minuteStr = '00'
            priceType = 'C'
        else:
            hourStr = eightDaysBeforeHourStr
            minuteStr = eightDaysBeforeMinuteStr
            priceType = 'M'

        self.assertEqual(
            'ETH/BTC on CCCAGG: ' + '{}/{}/{} {}:{}{}'.format(requestDayStr, requestMonthStr, requestYearStr, hourStr, minuteStr, priceType),
                                                        UtilityForTest.removePriceFromResult(printResult))
        self.assertEqual('eth btc {}/{}/{} {}:{} all'.format(requestDayStr, requestMonthStr, requestYearStr, hourStr, minuteStr), fullCommandStr)
        self.assertEqual(None, fullCommandStrWithSaveModeOptions)
        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        commands = SeqDiagBuilder.createSeqDiaqCommands('GUI')

        with open("c:\\temp\\ess.txt","w") as f:
            f.write(commands)

        SeqDiagBuilder.deactivate()

#        print(commands)
        self.assertEqual(
'''@startuml

actor GUI
participant Controller
	note over of Controller
		Entry point of the business layer
	end note
participant Requester
	note over of Requester
		Parses the user commands
	end note
participant CommandPrice
participant Processor
participant PriceRequester
	note over of PriceRequester
		Obtains the RT or historical rates from the Cryptocompare web site
	end note
participant GuiOutputFormater
GUI -> Controller: getPrintableResultForInput(inputStr)
	activate Controller
	Controller -> Requester: getCommand(inputStr)
		activate Requester
		Requester -> Requester: _parseAndFillCommandPrice(inputStr)
			activate Requester
			Requester -> Requester: _buildFullCommandPriceOptionalParmsDic(optionalParmList)
				activate Requester
				Requester <-- Requester: return optionalParsedParmDataDic
				deactivate Requester
			Requester <-- Requester: return CommandPrice or CommandError
			deactivate Requester
		Controller <-- Requester: return AbstractCommand
		deactivate Requester
		note right
			May return a CommandError in case of parsing problem.
		end note
	Controller -> CommandPrice: execute()
		activate CommandPrice
		CommandPrice -> Processor: getCryptoPrice(crypto, fiat, exchange, day, month, year, hour, minute, priceValueSymbol=None, ...)
			activate Processor
			Processor -> PriceRequester: getHistoricalPriceAtUTCTimeStamp(crypto, fiat, timeStampLocalForHistoMinute, timeStampUTCNoHHMMForHistoDay, exchange)
				activate PriceRequester
				note right
					Obtainins a minute price if request date < 7 days from now, else a day close price.
				end note
				PriceRequester -> PriceRequester: _getHistoDayPriceAtUTCTimeStamp(crypto, fiat, timeStampUTC, exchange, resultData)
					activate PriceRequester
					PriceRequester <-- PriceRequester: return ResultData
					deactivate PriceRequester
				Processor <-- PriceRequester: return ResultData
				deactivate PriceRequester
			CommandPrice <-- Processor: return ResultData
			deactivate Processor
		Controller <-- CommandPrice: return ResultData or False
		deactivate CommandPrice
	Controller -> GuiOutputFormater: getFullCommandString(resultData)
		activate GuiOutputFormater
		GuiOutputFormater -> GuiOutputFormater: _buildFullDateAndTimeStrings(commandDic, timezoneStr)
			activate GuiOutputFormater
			GuiOutputFormater <-- GuiOutputFormater: return requestDateDMY, requestDateHM
			deactivate GuiOutputFormater
		Controller <-- GuiOutputFormater: return printResult, fullCommandStr, fullCommandStrWithOptions, fullCommandStrWithSaveModeOptions
		deactivate GuiOutputFormater
	GUI <-- Controller: return printResult, fullCommandStr, fullCommandStrWithOptions, fullCommandStrWithSaveModeOptions
	deactivate Controller
@enduml''', commands)


    def testCreateSeqDiagCommandsOnFullRequestHistoDayPriceWithSignatureLimitation(self):
        if not 'CryptoPricer' in self.projectPath:
            return

        from datetimeutil import DateTimeUtil
        from utilityfortest import UtilityForTest
        from configurationmanager import ConfigurationManager
        from guioutputformater import GuiOutputFormater
        from controller import Controller

        SeqDiagBuilder.activate(self.projectPath, 'Controller', 'getPrintableResultForInput')  # activate sequence diagram building

        if os.name == 'posix':
            FILE_PATH = '/sdcard/cryptopricer.ini'
        else:
            FILE_PATH = 'c:\\temp\\cryptopricer.ini'

        configMgr = ConfigurationManager(FILE_PATH)
        self.controller = Controller(GuiOutputFormater(configMgr), configMgr)

        timezoneStr = 'Europe/Zurich'
        now = DateTimeUtil.localNow(timezoneStr)
        eightDaysBeforeArrowDate = now.shift(days=-8)

        eightDaysBeforeYearStr, eightDaysBeforeMonthStr, eightDaysBeforeDayStr, eightDaysBeforeHourStr, eightDaysBeforeMinuteStr = UtilityForTest.getFormattedDateTimeComponentsForArrowDateTimeObj(
            eightDaysBeforeArrowDate)

        requestYearStr = eightDaysBeforeYearStr
        requestDayStr = eightDaysBeforeDayStr
        requestMonthStr = eightDaysBeforeMonthStr
        inputStr = 'mcap btc {}/{} all'.format(requestDayStr, requestMonthStr)
        printResult, fullCommandStr, fullCommandStrWithOptions, fullCommandStrWithSaveModeOptions = self.controller.getPrintableResultForInput(
            inputStr)

        commands = SeqDiagBuilder.createSeqDiaqCommands('GUI', None, 20)

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        try:
            self.assertEqual(
'''@startuml

actor GUI
participant Controller
	note over of Controller
		Entry point of the business
		layer
	end note
participant Requester
	note over of Requester
		Parses the user commands
	end note
participant CommandPrice
participant Processor
participant PriceRequester
	note over of PriceRequester
		Obtains the RT or historical
		rates from the Cryptocompare
		web site
	end note
participant GuiOutputFormater
GUI -> Controller: getPrintableResultForInput(inputStr)
	activate Controller
	Controller -> Requester: getCommand(inputStr)
		activate Requester
		Requester -> Requester: _parseAndFillCommandPrice(inputStr)
			activate Requester
			Requester -> Requester: _buildFullCommandPriceOptionalParmsDic(optionalParmList)
				activate Requester
				Requester <-- Requester: return ...
				deactivate Requester
			Requester <-- Requester: return ...
			deactivate Requester
		Controller <-- Requester: return AbstractCommand
		deactivate Requester
		note right
			May return a CommandError in
			case of parsing problem.
		end note
	Controller -> CommandPrice: execute()
		activate CommandPrice
		CommandPrice -> Processor: getCryptoPrice(crypto, fiat, ...)
			activate Processor
			Processor -> PriceRequester: getHistoricalPriceAtUTCTimeStamp(crypto, fiat, ...)
				activate PriceRequester
				note right
					Obtainins a minute price if
					request date < 7 days from
					now, else a day close price.
				end note
				PriceRequester -> PriceRequester: _getHistoDayPriceAtUTCTimeStamp(crypto, fiat, ...)
					activate PriceRequester
					PriceRequester <-- PriceRequester: return ResultData
					deactivate PriceRequester
				Processor <-- PriceRequester: return ResultData
				deactivate PriceRequester
			CommandPrice <-- Processor: return ResultData
			deactivate Processor
		Controller <-- CommandPrice: return ResultData or False
		deactivate CommandPrice
	Controller -> GuiOutputFormater: getFullCommandString(resultData)
		activate GuiOutputFormater
		GuiOutputFormater -> GuiOutputFormater: _buildFullDateAndTimeStrings(commandDic, ...)
			activate GuiOutputFormater
			GuiOutputFormater <-- GuiOutputFormater: return requestDateDMY, ...
			deactivate GuiOutputFormater
		Controller <-- GuiOutputFormater: return printResult, ...
		deactivate GuiOutputFormater
	GUI <-- Controller: return printResult, ...
	deactivate Controller
@enduml''' \
                , commands)
        except TypeError as e:
            print(e)
            pass

        SeqDiagBuilder.deactivate()


    def testCreateSeqDiagCommandsOnClassesWithEmbededSelfCalls(self):
        entryPoint = ClassA()

        SeqDiagBuilder.activate(self.projectPath,'ClassA', 'doWork')  # activate sequence diagram building
        entryPoint.doWork()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt","w") as f:
            f.write(commands)

        self.assertEqual(
'''@startuml

actor USER
participant TestSeqDiagBuilder
participant ClassA
participant ClassB
	USER -> ClassA: doWork()
		activate ClassA
		ClassA -> ClassA: internalCall()
			activate ClassA
			ClassA -> ClassA: internalInnerCall()
				activate ClassA
				ClassA -> ClassB: createInnerRequest(parm1)
					activate ClassB
					ClassA <-- ClassB: return Bool
					deactivate ClassB
				ClassA <-- ClassA: return ResultPrice
				deactivate ClassA
			ClassA -> ClassB: createRequest(parm1, parm2)
				activate ClassB
				ClassA <-- ClassB: return Bool
				deactivate ClassB
			ClassA <-- ClassA: return ResultPrice
			deactivate ClassA
		USER <-- ClassA: return ClassAdoWorkRes
		deactivate ClassA
@enduml''', commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsWithoutActivatingSeqDiagBuilder(self):
        entryPoint = ClassA()

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building
        entryPoint.doWork()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)
        self.assertEqual('No control flow recorded. Method activate() called: False. Method recordFlow() called: True. Specified entry point: None.None reached: False', SeqDiagBuilder.getWarningList()[0])


    def testCreateSeqDiagCommandsOnClassLocatedInPackage(self):
        entryPoint = IsolatedClass()

        SeqDiagBuilder.activate(self.projectPath, 'IsolatedClass', 'analyse')  # activate sequence diagram building
        entryPoint.analyse()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        self.assertEqual(
'''@startuml

actor USER
participant IsolatedClass
USER -> IsolatedClass: analyse()
	activate IsolatedClass
	USER <-- IsolatedClass: return Analysis
	deactivate IsolatedClass
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCreateSeqDiagCommandsOnClassLocatedInSubPackage(self):
        entryPoint = IsolatedClassSub()

        SeqDiagBuilder.activate(self.projectPath, 'IsolatedClassSub', 'analyse')  # activate sequence diagram building
        entryPoint.analyse()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)
        self.assertEqual(
'''@startuml

actor USER
participant IsolatedClassSub
USER -> IsolatedClassSub: analyse()
	activate IsolatedClassSub
	USER <-- IsolatedClassSub: return Analysis
	deactivate IsolatedClassSub
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCallingMethodOnClassRequiringNonNoneConstructotParmWithoutPassingClassArgsDic(self):
        entryPoint = Caller()

        SeqDiagBuilder.activate(self.projectPath, 'Caller', 'call')  # activate sequence diagram building
        entryPoint.call()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - constructor for class FileReader in module testclasses.subtestpackage.filereader failed due to invalid argument(s).</font></b>
<b><font color=red size=14>  To solve the problem, pass a class argument dictionary to the SeqDiagBuilder.activate() method.</font></b>
endheader


actor USER
participant Caller
USER -> Caller: call()
	activate Caller
	USER <-- Caller: 
	deactivate Caller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


    def testCallingMethodOnClassRequiringNonNoneConstructotParmWithPassingClassArgsDic(self):
        entryPoint = Caller()
        classArgDic = {'FileReader': ['testfile.txt']}

        SeqDiagBuilder.activate(self.projectPath, 'Caller', 'call', classArgDic)  # activate sequence diagram building
        entryPoint.call()

        commands = SeqDiagBuilder.createSeqDiaqCommands('USER')

        with open("c:\\temp\\ess.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor USER
participant Caller
participant FileReader
USER -> Caller: call()
	activate Caller
	Caller -> FileReader: getContentAsList()
		activate FileReader
		Caller <-- FileReader: 
		deactivate FileReader
	USER <-- Caller: 
	deactivate Caller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


if __name__ == '__main__':
    unittest.main()

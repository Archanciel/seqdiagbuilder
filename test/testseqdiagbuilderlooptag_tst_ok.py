import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone

from testclasses.foobarclasses import *
from testclasses.classlooponemethodcallcaller import ClassLoopOneMethodCallCaller
from testclasses.classlooptwomethodcallcaller import ClassLoopTwoMethodCallCaller
from testclasses.classloopnestedinneronecaller import ClassLoopNestedInnerOneCaller
from testclasses.classloopnestedinnertwotwocallstwoloopstarttagsonsamelinecaller import ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller
from testclasses.classloopnestedinnertwocallscaller import ClassLoopNestedInnerTwoCallsCaller
from testclasses.classtwoloopscaller import ClassTwoLoopsCaller
from testclasses.classloopmultinestedloopcaller import ClassLoopMultiNestedLoopCaller
from testclasses.classloopnestedinnerwosamelooptagononelinecaller import ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller
from testclasses.classlooptagonmethodnotinrecordflowcaller import ClassLoopTagOnMethodNotInRecordFlowCaller
from testclasses.classloopmultinestedloopstartendendonsamelinecaller import ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller


class TestSeqDiagBuilderLoopTag(unittest.TestCase):
    def setUp(self):
        SeqDiagBuilder.deactivate()

    def testLoopTagWhereOneMethodCalled(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        where only one method is called within the loop.
        '''
        entryPoint = ClassLoopOneMethodCallCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopOneMethodCallCaller', 'call', None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagWhereOneMethodCalled.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopOneMethodCallCaller
participant ClassLoopOneMethodCall
participant ClassLeaf
User -> ClassLoopOneMethodCallCaller: call(p1)
	activate ClassLoopOneMethodCallCaller
	ClassLoopOneMethodCallCaller -> ClassLoopOneMethodCall: doB(p1)
		activate ClassLoopOneMethodCall
		loop 3 times
			ClassLoopOneMethodCall -> ClassLeaf: doC1(p1)
				activate ClassLeaf
				ClassLoopOneMethodCall <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassLoopOneMethodCall -> ClassLeaf: doC2(p1)
			activate ClassLeaf
			ClassLoopOneMethodCall <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopOneMethodCallCaller <-- ClassLoopOneMethodCall: 
		deactivate ClassLoopOneMethodCall
	User <-- ClassLoopOneMethodCallCaller: 
	deactivate ClassLoopOneMethodCallCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagWhereTwoMethodCalled(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        where two methods are called within the loop.
        '''
        entryPoint = ClassLoopTwoMethodCallCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTwoMethodCallCaller', 'call', None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagWhereTwoMethodCalled.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopTwoMethodCallCaller
participant ClassLoopTwoMethodCall
participant ClassLeaf
User -> ClassLoopTwoMethodCallCaller: call(p1)
	activate ClassLoopTwoMethodCallCaller
	ClassLoopTwoMethodCallCaller -> ClassLoopTwoMethodCall: doB(p1)
		activate ClassLoopTwoMethodCall
		loop 3 times
			ClassLoopTwoMethodCall -> ClassLeaf: doC1(p1)
				activate ClassLeaf
				ClassLoopTwoMethodCall <-- ClassLeaf: 
				deactivate ClassLeaf
			ClassLoopTwoMethodCall -> ClassLeaf: doC2(p1)
				activate ClassLeaf
				ClassLoopTwoMethodCall <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassLoopTwoMethodCallCaller <-- ClassLoopTwoMethodCall: 
		deactivate ClassLoopTwoMethodCall
	User <-- ClassLoopTwoMethodCallCaller: 
	deactivate ClassLoopTwoMethodCallCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagNestedLoopsWithTwoCallsInnerLoop(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        containing a nested loop. The nested loop (inner loop) itself
        contains two calls to a leaf function.
        '''
        entryPoint = ClassLoopNestedInnerTwoCallsCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopNestedInnerTwoCallsCaller',
                                'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagNestedLoopsWithTwoCallsInnerLoop.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopNestedInnerTwoCallsCaller
participant ClassLoopNestedInnerTwoCalls
participant ClassLeaf
User -> ClassLoopNestedInnerTwoCallsCaller: call(p1)
	activate ClassLoopNestedInnerTwoCallsCaller
	ClassLoopNestedInnerTwoCallsCaller -> ClassLoopNestedInnerTwoCalls: doB(p1)
		activate ClassLoopNestedInnerTwoCalls
		note right
			method doB note
		end note
		loop 3 times
			ClassLoopNestedInnerTwoCalls -> ClassLeaf: doC3(p1)
				activate ClassLeaf
				note right
					doC3 method note
				end note
				ClassLoopNestedInnerTwoCalls <-- ClassLeaf: 
				deactivate ClassLeaf
			loop 5 times
				ClassLoopNestedInnerTwoCalls -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassLoopNestedInnerTwoCalls <-- ClassLeaf: 
					deactivate ClassLeaf
				ClassLoopNestedInnerTwoCalls -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassLoopNestedInnerTwoCalls <-- ClassLeaf: 
					deactivate ClassLeaf
			end
			ClassLoopNestedInnerTwoCalls -> ClassLeaf: doC2(p1)
				activate ClassLeaf
				ClassLoopNestedInnerTwoCalls <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassLoopNestedInnerTwoCalls -> ClassLeaf: doC1(p1)
			activate ClassLeaf
			ClassLoopNestedInnerTwoCalls <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopNestedInnerTwoCallsCaller <-- ClassLoopNestedInnerTwoCalls: 
		deactivate ClassLoopNestedInnerTwoCalls
	User <-- ClassLoopNestedInnerTwoCallsCaller: 
	deactivate ClassLoopNestedInnerTwoCallsCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagWhereTwoLoops(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        where two non nested loops are defined.
        '''
        entryPoint = ClassTwoLoopsCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassTwoLoopsCaller', 'call', None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagWhereTwoLoops.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassTwoLoopsCaller
participant ClassTwoLoops
participant ClassLeaf
User -> ClassTwoLoopsCaller: call(p1)
	activate ClassTwoLoopsCaller
	ClassTwoLoopsCaller -> ClassTwoLoops: doB(p1)
		activate ClassTwoLoops
		loop 3 times
			ClassTwoLoops -> ClassLeaf: doC1(p1)
				activate ClassLeaf
				ClassTwoLoops <-- ClassLeaf: 
				deactivate ClassLeaf
			ClassTwoLoops -> ClassLeaf: doC2(p1)
				activate ClassLeaf
				ClassTwoLoops <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		loop 6 times
			ClassTwoLoops -> ClassLeaf: doC1(p1)
				activate ClassLeaf
				ClassTwoLoops <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassTwoLoops -> ClassLeaf: doC2(p1)
			activate ClassLeaf
			ClassTwoLoops <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassTwoLoopsCaller <-- ClassTwoLoops: 
		deactivate ClassTwoLoops
	User <-- ClassTwoLoopsCaller: 
	deactivate ClassTwoLoopsCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopStartAndLoopEndOnNotRecordedMethodCall(self):
        '''
        This test case tests the the correct handling of a :seqdiag_loop
        start tag located on a call to a method  which is not monitored
        by the SeqDiagBuilder.recordFlow() static method.
        '''
        entryPoint = ClassLoopTagOnMethodNotInRecordFlowCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTagOnMethodNotInRecordFlowCaller', 'callLoopStartAndLoopEndOnNotRecordedMethodCall', None)  # activate sequence diagram building
        entryPoint.callLoopStartAndLoopEndOnNotRecordedMethodCall('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopStartAndLoopEndOnNotRecordedMethodCall.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
User -> ClassLoopTagOnMethodNotInRecordFlowCaller: callLoopStartAndLoopEndOnNotRecordedMethodCall(p1)
	activate ClassLoopTagOnMethodNotInRecordFlowCaller
	ClassLoopTagOnMethodNotInRecordFlowCaller -> ClassLoopTagOnMethodNotInRecordFlow: doLoopStartAndLoopEndOnNotRecordedMethodCall(p1)
		activate ClassLoopTagOnMethodNotInRecordFlow
		ClassLoopTagOnMethodNotInRecordFlow -> ClassLeaf: doC2(p1)
			activate ClassLeaf
			ClassLoopTagOnMethodNotInRecordFlow <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopTagOnMethodNotInRecordFlowCaller <-- ClassLoopTagOnMethodNotInRecordFlow: 
		deactivate ClassLoopTagOnMethodNotInRecordFlow
	User <-- ClassLoopTagOnMethodNotInRecordFlowCaller: 
	deactivate ClassLoopTagOnMethodNotInRecordFlowCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopStartEndOnNotRecordedMethodCall(self):
        '''
        This test case tests the the correct handling of a :seqdiag_loop
        start end tag located on a call to a method  which is not monitored
        by the SeqDiagBuilder.recordFlow() static method.
        '''
        entryPoint = ClassLoopTagOnMethodNotInRecordFlowCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTagOnMethodNotInRecordFlowCaller', 'callLoopStartEndOnNotRecordedMethodCall', None)  # activate sequence diagram building
        entryPoint.callLoopStartEndOnNotRecordedMethodCall('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopStartEndOnNotRecordedMethodCall.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
User -> ClassLoopTagOnMethodNotInRecordFlowCaller: callLoopStartEndOnNotRecordedMethodCall(p1)
	activate ClassLoopTagOnMethodNotInRecordFlowCaller
	ClassLoopTagOnMethodNotInRecordFlowCaller -> ClassLoopTagOnMethodNotInRecordFlow: doLoopStartEndOnNotRecordedMethodCall(p1)
		activate ClassLoopTagOnMethodNotInRecordFlow
		ClassLoopTagOnMethodNotInRecordFlow -> ClassLeaf: doC2(p1)
			activate ClassLeaf
			ClassLoopTagOnMethodNotInRecordFlow <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopTagOnMethodNotInRecordFlowCaller <-- ClassLoopTagOnMethodNotInRecordFlow: 
		deactivate ClassLoopTagOnMethodNotInRecordFlow
	User <-- ClassLoopTagOnMethodNotInRecordFlowCaller: 
	deactivate ClassLoopTagOnMethodNotInRecordFlowCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building


if __name__ == '__main__':
    unittest.main()

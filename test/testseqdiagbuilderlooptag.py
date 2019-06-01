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
from testclasses.classloopnestedinnertwotwocallscaller import ClassLoopNestedInnerTwoTwoCallsCaller
from testclasses.classtwoloopscaller import ClassTwoLoopsCaller
from testclasses.classloopmultinestedloopcaller import ClassLoopMultiNestedLoopCaller

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


    def testLoopTagNestedLoopsWithOneCallInnerLoop(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        containing a nested loop. The nested loop (inner loop) itself
        contains only one call to a leaf function. This means that the
        :seqdiag loop start end tag is used there.
        '''
        entryPoint = ClassLoopNestedInnerOneCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopNestedInnerOneCaller', 'call', None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagNestedLoopsWithOneCallInnerLoop.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopNestedInnerOneCaller
participant ClassLoopNestedInnerOne
participant ClassLeaf
User -> ClassLoopNestedInnerOneCaller: call(p1)
	activate ClassLoopNestedInnerOneCaller
	ClassLoopNestedInnerOneCaller -> ClassLoopNestedInnerOne: doB(p1)
		activate ClassLoopNestedInnerOne
		loop 3 times
			loop 5 times
				ClassLoopNestedInnerOne -> ClassLeaf: doCWithNote(p1)
					activate ClassLeaf
					note right
						doCWithNote method note
					end note
					ClassLoopNestedInnerOne <-- ClassLeaf: 
					deactivate ClassLeaf
			end
			ClassLoopNestedInnerOne -> ClassLeaf: doC2(p1)
				activate ClassLeaf
				ClassLoopNestedInnerOne <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassLoopNestedInnerOne -> ClassLeaf: doC1(p1)
			activate ClassLeaf
			ClassLoopNestedInnerOne <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopNestedInnerOneCaller <-- ClassLoopNestedInnerOne: 
		deactivate ClassLoopNestedInnerOne
	User <-- ClassLoopNestedInnerOneCaller: 
	deactivate ClassLoopNestedInnerOneCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagMultiNestedLoops(self):
        '''
        This test case tests the correct generation of multi nested
        PlantUml loop.
        '''
        entryPoint = ClassLoopMultiNestedLoopCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoops.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopMultiNestedLoopCaller
participant ClassLoopMultiNestedLoop
participant ClassMidLoop
participant ClassLeaf
User -> ClassLoopMultiNestedLoopCaller: call(p1)
	activate ClassLoopMultiNestedLoopCaller
	ClassLoopMultiNestedLoopCaller -> ClassLoopMultiNestedLoop: doB(p1)
		activate ClassLoopMultiNestedLoop
		loop 2 times
			loop 3 times
				ClassLoopMultiNestedLoop -> ClassMidLoop: doMidLoopLeafLoop(p1)
					activate ClassMidLoop
					loop 2 times
						ClassMidLoop -> ClassLeaf: doCLoop(p1)
							activate ClassLeaf
							note right
								doCLoop method note
							end note
							loop 2 times
								ClassLeaf -> ClassLeaf: doC1(p1)
									activate ClassLeaf
									ClassLeaf <-- ClassLeaf: 
									deactivate ClassLeaf
								ClassLeaf -> ClassLeaf: doC2(p1)
									activate ClassLeaf
									ClassLeaf <-- ClassLeaf: 
									deactivate ClassLeaf
							end
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
						ClassMidLoop -> ClassLeaf: doCLoopStartEnd(p1)
							activate ClassLeaf
							note right
								doCLoopStartEnd method note
							end note
							loop 3 times
								ClassLeaf -> ClassLeaf: doC1(p1)
									activate ClassLeaf
									ClassLeaf <-- ClassLeaf: 
									deactivate ClassLeaf
								ClassMidLoop <-- ClassLeaf: 
								deactivate ClassLeaf
							end
					end
					ClassLoopMultiNestedLoop <-- ClassMidLoop: 
					deactivate ClassMidLoop
			end
			ClassLoopMultiNestedLoop -> ClassMidLoop: doMidLoopSimple(p1)
				activate ClassMidLoop
				loop 3 times
					ClassMidLoop -> ClassLeaf: doC1(p1)
						activate ClassLeaf
						ClassMidLoop <-- ClassLeaf: 
						deactivate ClassLeaf
					ClassMidLoop -> ClassLeaf: doC2(p1)
						activate ClassLeaf
						ClassMidLoop <-- ClassLeaf: 
						deactivate ClassLeaf
				end
				ClassLoopMultiNestedLoop <-- ClassMidLoop: 
				deactivate ClassMidLoop
		end
		ClassLoopMultiNestedLoop -> ClassMidLoop: doMidLoop1(p1)
			activate ClassMidLoop
			loop 2 times
				ClassMidLoop -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassMidLoop <-- ClassLeaf: 
					deactivate ClassLeaf
				ClassMidLoop -> ClassLeaf: doC2(p1)
					activate ClassLeaf
					ClassMidLoop <-- ClassLeaf: 
					deactivate ClassLeaf
			end
			ClassLoopMultiNestedLoop <-- ClassMidLoop: 
			deactivate ClassMidLoop
		ClassLoopMultiNestedLoopCaller <-- ClassLoopMultiNestedLoop: 
		deactivate ClassLoopMultiNestedLoop
	User <-- ClassLoopMultiNestedLoopCaller: 
	deactivate ClassLoopMultiNestedLoopCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagNestedLoopsWithTwoCallsInnerLoopTwoLoopStartTagsOnSameLine(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        containing a nested loop. The nested loop (inner loop) itself
        contains two calls to a leaf function with the two seqdiag start
        loop tags located on the same line.
        '''
        entryPoint = ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagNestedLoopsWithTwoCallsInnerLoopTwoLoopStartTagsOnSameLine.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller
participant ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine
participant ClassLeaf
User -> ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller: call(p1)
	activate ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller
	ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller -> ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine: doB(p1)
		activate ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine
		loop 3 times
			loop 5 times
				ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine <-- ClassLeaf: 
					deactivate ClassLeaf
				ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine <-- ClassLeaf: 
					deactivate ClassLeaf
			end
			ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine -> ClassLeaf: doC2(p1)
				activate ClassLeaf
				ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine <-- ClassLeaf: 
				deactivate ClassLeaf
		end
		ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine -> ClassLeaf: doC1(p1)
			activate ClassLeaf
			ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller <-- ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine: 
		deactivate ClassLoopNestedInnerTwoCallsTwoLoopStartTagsOnSameLine
	User <-- ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller: 
	deactivate ClassLoopNestedInnerTwoTwoCallsTwoLoopStartTagsOnSameLineCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagNestedLoopsWithTwoCallsInnerLoop(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        containing a nested loop. The nested loop (inner loop) itself
        contains two calls to a leaf function.
        '''
        entryPoint = ClassLoopNestedInnerTwoTwoCallsCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopNestedInnerTwoTwoCallsCaller',
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
participant ClassLoopNestedInnerTwoTwoCallsCaller
participant ClassLoopNestedInnerTwoCalls
participant ClassLeaf
User -> ClassLoopNestedInnerTwoTwoCallsCaller: call(p1)
	activate ClassLoopNestedInnerTwoTwoCallsCaller
	ClassLoopNestedInnerTwoTwoCallsCaller -> ClassLoopNestedInnerTwoCalls: doB(p1)
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
		ClassLoopNestedInnerTwoTwoCallsCaller <-- ClassLoopNestedInnerTwoCalls: 
		deactivate ClassLoopNestedInnerTwoCalls
	User <-- ClassLoopNestedInnerTwoTwoCallsCaller: 
	deactivate ClassLoopNestedInnerTwoTwoCallsCaller
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
		end
		deactivate ClassLeaf
		loop 6 times
			ClassTwoLoops -> ClassLeaf: doC1(p1)
				activate ClassLeaf
				ClassTwoLoops <-- ClassLeaf: 
		end
		deactivate ClassLeaf
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

if __name__ == '__main__':
    unittest.main()

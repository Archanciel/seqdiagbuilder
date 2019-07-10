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
from testclasses.classloopmultinestedloopsimplercaller import ClassLoopMultiNestedLoopSimplerCaller
from testclasses.classloopmultinestedloopsimpler2caller import ClassLoopMultiNestedLoopSimpler2Caller
from testclasses.classloopthreenestedloopcaller import ClassLoopThreeNestedLoopCaller
from testclasses.classloopmultinestedloopsimpler2missingloopendtagcaller import ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller
from testclasses.classloopmultinestedloopsimpler2missingloopstarttagcaller import ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller

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

    def testLoopTagNestedInnerTwoSameLoopTagOnOneLine(self):
        '''
        This test case tests the correct generation of a PlantUml loop
        command using the :seqdiag_loop tags added in the body of a method
        containing a nested loop. The outer loop does not contain any call.
        The nested loop (inner loop) itself
        contains only one call to a leaf function. This means that the
        :seqdiag loop start end tag is used twice on the same line there.
        '''
        entryPoint = ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagNestedInnerTwoSameLoopTagOnOneLine.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller
participant ClassLoopNestedInnerTwoSameLoopTagOnOneLine
participant ClassLeaf
User -> ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller: call(p1)
	activate ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller
	ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller -> ClassLoopNestedInnerTwoSameLoopTagOnOneLine: doB(p1)
		activate ClassLoopNestedInnerTwoSameLoopTagOnOneLine
		loop 3 times
			loop 5 times
				ClassLoopNestedInnerTwoSameLoopTagOnOneLine -> ClassLeaf: doCWithNote(p1)
					activate ClassLeaf
					note right
						doCWithNote method note
					end note
					ClassLoopNestedInnerTwoSameLoopTagOnOneLine <-- ClassLeaf: 
					deactivate ClassLeaf
			end
		end
		ClassLoopNestedInnerTwoSameLoopTagOnOneLine -> ClassLeaf: doC1(p1)
			activate ClassLeaf
			ClassLoopNestedInnerTwoSameLoopTagOnOneLine <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller <-- ClassLoopNestedInnerTwoSameLoopTagOnOneLine: 
		deactivate ClassLoopNestedInnerTwoSameLoopTagOnOneLine
	User <-- ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller: 
	deactivate ClassLoopNestedInnerTwoSameLoopTagOnOneLineCaller
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
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
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

    def testLoopTagMultiNestedLoopsSimpler(self):
        '''
        This test case tests the correct generation of multi nested
        PlantUml loop.
        '''
        entryPoint = ClassLoopMultiNestedLoopSimplerCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopSimplerCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoopsSimpler.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopMultiNestedLoopSimplerCaller
participant ClassLoopMultiNestedLoopSimpler
participant ClassMidLoop
participant ClassLeaf
User -> ClassLoopMultiNestedLoopSimplerCaller: call(p1)
	activate ClassLoopMultiNestedLoopSimplerCaller
	ClassLoopMultiNestedLoopSimplerCaller -> ClassLoopMultiNestedLoopSimpler: doB(p1)
		activate ClassLoopMultiNestedLoopSimpler
		loop 2 times
			loop 3 times
				ClassLoopMultiNestedLoopSimpler -> ClassMidLoop: doMidLoopLeafLoop(p1)
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
							end
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
					end
					ClassLoopMultiNestedLoopSimpler <-- ClassMidLoop: 
					deactivate ClassMidLoop
			end
			ClassLoopMultiNestedLoopSimpler -> ClassMidLoop: doMidLoopSimple(p1)
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
				ClassLoopMultiNestedLoopSimpler <-- ClassMidLoop: 
				deactivate ClassMidLoop
		end
		ClassLoopMultiNestedLoopSimplerCaller <-- ClassLoopMultiNestedLoopSimpler: 
		deactivate ClassLoopMultiNestedLoopSimpler
	User <-- ClassLoopMultiNestedLoopSimplerCaller: 
	deactivate ClassLoopMultiNestedLoopSimplerCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagMultiNestedLoopsSimpler2(self):
        '''
        This test case tests the correct generation of multi nested
        PlantUml loop.
        '''
        entryPoint = ClassLoopMultiNestedLoopSimpler2Caller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopSimpler2Caller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoopsSimpler2.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopMultiNestedLoopSimpler2Caller
participant ClassLoopMultiNestedLoopSimpler2
participant ClassMidLoop
participant ClassLeaf
User -> ClassLoopMultiNestedLoopSimpler2Caller: call(p1)
	activate ClassLoopMultiNestedLoopSimpler2Caller
	ClassLoopMultiNestedLoopSimpler2Caller -> ClassLoopMultiNestedLoopSimpler2: doB(p1)
		activate ClassLoopMultiNestedLoopSimpler2
		loop 2 times
			loop 3 times
				ClassLoopMultiNestedLoopSimpler2 -> ClassMidLoop: doMidLoopLeafLoop(p1)
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
							end
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
					end
					ClassLoopMultiNestedLoopSimpler2 <-- ClassMidLoop: 
					deactivate ClassMidLoop
			end
		end
		ClassLoopMultiNestedLoopSimpler2Caller <-- ClassLoopMultiNestedLoopSimpler2: 
		deactivate ClassLoopMultiNestedLoopSimpler2
	User <-- ClassLoopMultiNestedLoopSimpler2Caller: 
	deactivate ClassLoopMultiNestedLoopSimpler2Caller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagMultiNestedLoopsSimpler2MissingLoopEndTag(self):
        '''
        This test case tests the generation of an error warning in the Plant
        Uml command file in case a seqdiag loop start tag has no corresponding
        seqdiag loop end tag.
        '''
        entryPoint = ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoopsSimpler2MissingLoopEndTag.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_start' tag number (1) greater than :seqdiag_loop_end tag number (0) in method doB of class</font></b>
<b><font color=red size=14>  ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag. As a consequence, the loop part of the sequence diagram is not correct !</font></b>
<b><font color=red size=14>  </font></b>
endheader


actor User
participant ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller
participant ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag
participant ClassMidLoop
participant ClassLeaf
User -> ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller: call(p1)
	activate ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller
	ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller -> ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag: doB(p1)
		activate ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag
		loop 2 times
			loop 3 times
				ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag -> ClassMidLoop: doMidLoopLeafLoop(p1)
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
							end
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
					end
					ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag <-- ClassMidLoop: 
					deactivate ClassMidLoop
			end
			ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller <-- ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag: 
			deactivate ClassLoopMultiNestedLoopSimpler2MissingLoopEndTag
		User <-- ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller: 
		deactivate ClassLoopMultiNestedLoopSimpler2MissingLoopEndTagCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagMultiNestedLoopsSimpler2MissingLoopStartTag(self):
        '''
        This test case tests the generation of an error warning in the Plant
        Uml command file in case a seqdiag loop end tag has no corresponding
        seqdiag loop start tag.
        '''
        entryPoint = ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoopsSimpler2MissingLoopStartTag.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_end' tag number (1) greater than :seqdiag_loop_start tag number (0) in method doB of class</font></b>
<b><font color=red size=14>  ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag. As a consequence, the whole sequence diagram is wrong or incomplete !</font></b>
<b><font color=red size=14>  </font></b>
endheader


actor User
participant ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller
participant ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag
participant ClassMidLoop
participant ClassLeaf
User -> ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller: call(p1)
	activate ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller
	ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller -> ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag: doB(p1)
		activate ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag
		loop 2 times
			loop 3 times
				ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag -> ClassMidLoop: doMidLoopLeafLoop(p1)
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
							end
							ClassMidLoop <-- ClassLeaf: 
							deactivate ClassLeaf
						ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag <-- ClassMidLoop: 
						deactivate ClassMidLoop
					ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag -> ClassMidLoop: doMidLoopSimple(p1)
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
						ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag <-- ClassMidLoop: 
						deactivate ClassMidLoop
				end
				ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller <-- ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag: 
				deactivate ClassLoopMultiNestedLoopSimpler2MissingLoopStartTag
			User <-- ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller: 
			deactivate ClassLoopMultiNestedLoopSimpler2MissingLoopStartTagCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagThreeNestedLoops(self):
        '''
        This test case tests the correct generation of multi nested
        PlantUml loop.
        '''
        entryPoint = ClassLoopThreeNestedLoopCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopThreeNestedLoopCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagThreeNestedLoops.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopThreeNestedLoopCaller
participant ClassLoopThreeNestedLoop
participant ClassLeaf
User -> ClassLoopThreeNestedLoopCaller: call(p1)
	activate ClassLoopThreeNestedLoopCaller
	ClassLoopThreeNestedLoopCaller -> ClassLoopThreeNestedLoop: doB(p1)
		activate ClassLoopThreeNestedLoop
		loop 2 times
			loop 3 times
				loop 4 times
					ClassLoopThreeNestedLoop -> ClassLeaf: doC3(p1)
						activate ClassLeaf
						note right
							doC3 method note
						end note
						ClassLoopThreeNestedLoop <-- ClassLeaf: 
						deactivate ClassLeaf
				end
			end
		end
		ClassLoopThreeNestedLoopCaller <-- ClassLoopThreeNestedLoop: 
		deactivate ClassLoopThreeNestedLoop
	User <-- ClassLoopThreeNestedLoopCaller: 
	deactivate ClassLoopThreeNestedLoopCaller
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopTagMultiNestedLoopsStartEndEndOnSameLine(self):
        '''
        This test case tests the correct generation of multi nested
        PlantUml loop in a special situation where there's a seqdiag loop
        start end and a seqdiag loop end on the same line.
        '''
        entryPoint = ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller', 'call',
                                None)  # activate sequence diagram building
        entryPoint.call('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopTagMultiNestedLoopsStartEndEndOnSameLine.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 0)

        self.assertEqual(
'''@startuml

actor User
participant ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller
participant ClassLoopMultiNestedLoopStartEndEndOnSameLine
participant ClassLeaf
User -> ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller: call(p1)
	activate ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller
	ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller -> ClassLoopMultiNestedLoopStartEndEndOnSameLine: doB(p1)
		activate ClassLoopMultiNestedLoopStartEndEndOnSameLine
		loop 3 times
			loop 2 times
				ClassLoopMultiNestedLoopStartEndEndOnSameLine -> ClassLeaf: doC1(p1)
					activate ClassLeaf
					ClassLoopMultiNestedLoopStartEndEndOnSameLine <-- ClassLeaf: 
					deactivate ClassLeaf
			end
			loop 2 times
				ClassLoopMultiNestedLoopStartEndEndOnSameLine -> ClassLeaf: doC2(p1)
					activate ClassLeaf
					ClassLoopMultiNestedLoopStartEndEndOnSameLine <-- ClassLeaf: 
					deactivate ClassLeaf
			end
		end
		ClassLoopMultiNestedLoopStartEndEndOnSameLine -> ClassLeaf: doC3(p1)
			activate ClassLeaf
			note right
				doC3 method note
			end note
			ClassLoopMultiNestedLoopStartEndEndOnSameLine <-- ClassLeaf: 
			deactivate ClassLeaf
		ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller <-- ClassLoopMultiNestedLoopStartEndEndOnSameLine: 
		deactivate ClassLoopMultiNestedLoopStartEndEndOnSameLine
	User <-- ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller: 
	deactivate ClassLoopMultiNestedLoopStartEndEndOnSameLineCaller
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
        This test case tests the the correct handling of both :seqdiag_loop
        start and :seqdiag_loop end tags located on a call to a method  which is not monitored
        by the SeqDiagBuilder.recordFlow() static method.
        '''
        entryPoint = ClassLoopTagOnMethodNotInRecordFlowCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTagOnMethodNotInRecordFlowCaller', 'callLoopStartAndLoopEndOnNotRecordedMethodCall', None)  # activate sequence diagram building
        entryPoint.callLoopStartAndLoopEndOnNotRecordedMethodCall('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopStartAndLoopEndOnNotRecordedMethodCall.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 2)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=20> 1</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_start' tag located on line 16 of file containing class ClassLoopTagOnMethodNotInRecordFlow is placed on an instruction calling</font></b>
<b><font color=red size=14>  method doC4NotRecordedInFlow() which IS NOT part of the execution flow recorded by SeqDiagBuilder.</font></b>
<b><font color=red size=14>  To solve the problem, ensure the ':seqdiag_loop_start' tag is placed on a line calling a method whose execution is recorded by</font></b>
<b><font color=red size=14>  SeqDiagBuilder.recordFlow().</font></b>
<b><font color=red size=20> 2</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_end' tag located on line 18 of file containing class ClassLoopTagOnMethodNotInRecordFlow is placed on an instruction calling</font></b>
<b><font color=red size=14>  method doC4NotRecordedInFlow() which IS NOT part of the execution flow recorded by SeqDiagBuilder.</font></b>
<b><font color=red size=14>  To solve the problem, ensure the ':seqdiag_loop_end' tag is placed on a line calling a method whose execution is recorded by</font></b>
<b><font color=red size=14>  SeqDiagBuilder.recordFlow().</font></b>
endheader

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
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

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_start_end' tag located on line 34 of file containing class ClassLoopTagOnMethodNotInRecordFlow is placed on an instruction</font></b>
<b><font color=red size=14>  calling method doC4NotRecordedInFlow() which IS NOT part of the execution flow recorded by SeqDiagBuilder.</font></b>
<b><font color=red size=14>  To solve the problem, ensure the ':seqdiag_loop_start_end' tag is placed on a line calling a method whose execution is recorded by</font></b>
<b><font color=red size=14>  SeqDiagBuilder.recordFlow().</font></b>
endheader

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall(self):
        '''
        This test case tests the the correct handling of a :seqdiag_loop
        start tag located on a call to a method  which is monitored
        by the SeqDiagBuilder.recordFlow() static method and a :seqdiag_loop
        end tag located on a call to a method which is not monitored
        by the SeqDiagBuilder.recordFlow() static method..
        '''
        entryPoint = ClassLoopTagOnMethodNotInRecordFlowCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTagOnMethodNotInRecordFlowCaller', 'callLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall', None)  # activate sequence diagram building
        entryPoint.callLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopStartOnRecordedMethodCallAndLoopEndOnNotRecordedMethodCall.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        # since the loop start command has no corresponding end command, PlantUML
        # will ignore the loop start command
        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_end' tag located on line 75 of file containing class ClassLoopTagOnMethodNotInRecordFlow is placed on an instruction calling</font></b>
<b><font color=red size=14>  method doC4NotRecordedInFlow() which IS NOT part of the execution flow recorded by SeqDiagBuilder.</font></b>
<b><font color=red size=14>  To solve the problem, ensure the ':seqdiag_loop_end' tag is placed on a line calling a method whose execution is recorded by</font></b>
<b><font color=red size=14>  SeqDiagBuilder.recordFlow().</font></b>
endheader

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

    def testLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall(self):
        '''
        This test case tests the the correct handling of a :seqdiag_loop
        start tag located on a call to a method  which is not monitored
        by the SeqDiagBuilder.recordFlow() static method and a :seqdiag_loop
        end tag located on a call to a method which is monitored
        by the SeqDiagBuilder.recordFlow() static method..
        '''
        entryPoint = ClassLoopTagOnMethodNotInRecordFlowCaller()

        SeqDiagBuilder.activate(parentdir, 'ClassLoopTagOnMethodNotInRecordFlowCaller', 'callLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall', None)  # activate sequence diagram building
        entryPoint.callLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall('str')

        commands = SeqDiagBuilder.createSeqDiaqCommands('User')

        with open("c:\\temp\\testLoopStartOnNotRecordedMethodCallAndLoopEndOnRecordedMethodCall.txt", "w") as f:
            f.write(commands)

        self.assertEqual(len(SeqDiagBuilder.getWarningList()), 1)

        # since the loop end command has no corresponding start command,
        # we do not write an end command in the PlantUML command file since
        # it would cause an error at seq diagram generation time by PlantUML.
        self.assertEqual(
'''@startuml
center header
<b><font color=red size=20> Warnings</font></b>
<b><font color=red size=14>  ERROR - ':seqdiag_loop_start' tag located on line 53 of file containing class ClassLoopTagOnMethodNotInRecordFlow is placed on an instruction calling</font></b>
<b><font color=red size=14>  method doC4NotRecordedInFlow() which IS NOT part of the execution flow recorded by SeqDiagBuilder.</font></b>
<b><font color=red size=14>  To solve the problem, ensure the ':seqdiag_loop_start' tag is placed on a line calling a method whose execution is recorded by</font></b>
<b><font color=red size=14>  SeqDiagBuilder.recordFlow().</font></b>
endheader

actor User
participant ClassLoopTagOnMethodNotInRecordFlowCaller
participant ClassLoopTagOnMethodNotInRecordFlow
participant ClassLeaf
@enduml''', commands)

        SeqDiagBuilder.deactivate()  # deactivate sequence diagram building

if __name__ == '__main__':
    unittest.main()

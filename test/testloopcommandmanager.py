import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone

from seqdiagbuilder import LoopCommandManager
from seqdiagbuilder import SEQDIAG_LOOP_START_TAG, SEQDIAG_LOOP_START_END_TAG, SEQDIAG_LOOP_END_TAG

class TestLoopCommandManager(unittest.TestCase):
    def test_buildKey(self):
        '''
        Test that the LoopCommandManager key is correctly built.
        :return:
        '''
        loopCommandMgr = LoopCommandManager()
        fromClassName = 'ClassLoopNestedInnerOne'
        fromMethodName = 'doB'
        toMethodName = 'doCWithNote'
        key = loopCommandMgr._buildKey(fromClassName, fromMethodName, toMethodName, 17)

        self.assertIsNotNone(key)
        self.assertEqual(key, 'ClassLoopNestedInnerOne.doB->doCWithNote: 17')

    def testStoreLoopCommandsClassLoopNestedInnerOne(self):
        '''
        Test the correct working of the LoopCommandManager on a source file containing loop
        commands.
        :return:
        '''
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinnerone.py"
        fromClassName = 'ClassLoopNestedInnerOne'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', False], [':seqdiag_loop_start_end', '5 times', False])

        value_20 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', '', False])

    def testGetLoopCommandList(self):
        '''
        Test the correct working of the LoopCommandManager for loop tags
        with and without time info.
        :return:
        '''
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', False], [':seqdiag_loop_start_end', '5 times', False])

        value_20 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', '', False])

    def testConsumeLoopCommand(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', True], [':seqdiag_loop_start_end', '5 times', False])
        loopCommandMgr.consumeLoopCommand(1, fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', True], [':seqdiag_loop_start_end', '5 times', True])

        value_20 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', '', True])

    def testConsumeLoopCommand(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', True], [':seqdiag_loop_start_end', '5 times', False])
        loopCommandMgr.consumeLoopCommand(1, fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times', True], [':seqdiag_loop_start_end', '5 times', True])

        value_20 = loopCommandMgr.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', '', True])

    def testGetUnconsumedLoopCommandListNoUnconsumedCommands(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doCWithNote', 17)
        loopCommandMgr.consumeLoopCommand(1, fromClassName, fromMethodName, 'doCWithNote', 17)

        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doC2', 20)
        self.assertIsNone(loopCommandMgr.getUnconsumedLoopCommandList())

    def testGetUnconsumedLoopCommandListOneUnconsumedCommands(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doCWithNote', 17)
        loopCommandMgr.consumeLoopCommand(1, fromClassName, fromMethodName, 'doCWithNote', 17)

        unconsumedLoopCommandList = loopCommandMgr.getUnconsumedLoopCommandList()
        self.assertEqual(unconsumedLoopCommandList, ['ClassLoopNestedInnerOneForTestLoopIdxDic.doB->doC2: 20'])

    def testGetUnconsumedLoopCommandListTwoUnconsumedCommandsOnDifferentLines(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doCWithNote', 17)

        unconsumedLoopCommandList = loopCommandMgr.getUnconsumedLoopCommandList()
        self.assertEqual(unconsumedLoopCommandList, ['ClassLoopNestedInnerOneForTestLoopIdxDic.doB->doCWithNote: 17', 'ClassLoopNestedInnerOneForTestLoopIdxDic.doB->doC2: 20'])

    def testGetUnconsumedLoopCommandListTwoUnconsumedCommandsOnSameLines(self):
        loopCommandMgr = LoopCommandManager()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopCommandMgr.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        loopCommandMgr.consumeLoopCommand(0, fromClassName, fromMethodName, 'doC2', 20)

        unconsumedLoopCommandList = loopCommandMgr.getUnconsumedLoopCommandList()
        self.assertEqual(unconsumedLoopCommandList, ['ClassLoopNestedInnerOneForTestLoopIdxDic.doB->doCWithNote: 17', 'ClassLoopNestedInnerOneForTestLoopIdxDic.doB->doCWithNote: 17'])

    def testExtractLoopCommandsFromLine(self):
        '''
        Testing seqdiag loop commands extraction from a string line.
        :return:
        '''
        loopCommandMgr = LoopCommandManager()

        # instruction line containing 1 seqdiag loop start command
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', '3 times']], loopCommandList)

        # instruction line containing 1 seqdiag loop start end command
        instructionLine = SEQDIAG_LOOP_START_END_TAG + ' 3 times'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start_end', '3 times']], loopCommandList)

        # instruction line containing 1 seqdiag loop end command
        instructionLine = SEQDIAG_LOOP_END_TAG
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_end', '']], loopCommandList)

        # instruction line containing 2 seqdiag loop start commands
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times ' + SEQDIAG_LOOP_START_TAG + ' 5 times'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start',  '5 times']], loopCommandList)

        # instruction line containing 2 seqdiag loop start end commands
        instructionLine = SEQDIAG_LOOP_START_END_TAG + ' 3 times ' + SEQDIAG_LOOP_START_END_TAG + ' 5 times'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start_end', '3 times'], [':seqdiag_loop_start_end',  '5 times']], loopCommandList)

        # instruction line containing 2 seqdiag loop end command
        instructionLine = SEQDIAG_LOOP_END_TAG + ' ' + SEQDIAG_LOOP_END_TAG
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_end', ''], [':seqdiag_loop_end', '']], loopCommandList)

        # instruction line containing several seqdiag loop commands, some
        # specifying time with no 's'
        instructionLine = SEQDIAG_LOOP_START_TAG + ' three time ' + SEQDIAG_LOOP_START_END_TAG + ' 5 times ' + SEQDIAG_LOOP_START_END_TAG + '     at least fifty time ' + SEQDIAG_LOOP_START_TAG + ' 30 times'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', 'three time'], [':seqdiag_loop_start_end', '5 times'], [':seqdiag_loop_start_end', 'at least fifty time'], [':seqdiag_loop_start', '30 times']], loopCommandList)

        # instruction line containing no seqdiag loop command
        instructionLine = 'if a > 45'
        loopCommandList = loopCommandMgr.extractLoopCommandsFromLine(instructionLine)
        self.assertIsNone(loopCommandList)

if __name__ == '__main__':
    unittest.main()

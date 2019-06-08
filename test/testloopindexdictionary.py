import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone

from seqdiagbuilder import LoopIndexDictionary
from seqdiagbuilder import SEQDIAG_LOOP_START_TAG, SEQDIAG_LOOP_START_END_TAG, SEQDIAG_LOOP_END_TAG

class TestLoopIndexDictionary(unittest.TestCase):
    def test_buildKey(self):
        '''
        Test that the LoopIndexDictionary key is correctly built.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()
        fromClassName = 'ClassLoopNestedInnerOne'
        fromMethodName = 'doB'
        toMethodName = 'doCWithNote'
        key = loopIdxDic._buildKey(fromClassName, fromMethodName, toMethodName, 17)

        self.assertIsNotNone(key)
        self.assertEqual(key, 'ClassLoopNestedInnerOne.doB->doCWithNote: 17')

    def testStoreLoopCommandsClassLoopNestedInnerOne(self):
        '''
        Test the correct working of the LoopIndexDictionary on a source file containing loop
        commands.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinnerone.py"
        fromClassName = 'ClassLoopNestedInnerOne'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopIdxDic.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopIdxDic.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start_end', '5 times'])

        value_20 = loopIdxDic.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', ''])

    def testLoopIndexDictionaryClassLoopNestedInnerOneNoTimeInfo(self):
        '''
        Test the correct working of the LoopIndexDictionary for loop tags
        with no time info.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        fromClassName = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        fromMethodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if fromMethodName in entry][0]
            loopIdxDic.storeLoopCommands(fromClassName, fromMethodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        value_17 = loopIdxDic.getLoopCommandList(fromClassName, fromMethodName, 'doCWithNote', 17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start_end', '5 times'])

        value_20 = loopIdxDic.getLoopCommandList(fromClassName, fromMethodName, 'doC2', 20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', ''])

    def testExtractLoopCommandsFromLine(self):
        '''
        Testing seqdiag loop commands extraction from a string line.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        # instruction line containing 1 seqdiag loop start command
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', '3 times']], loopCommandList)

        # instruction line containing 1 seqdiag loop end ommand
        instructionLine = SEQDIAG_LOOP_END_TAG
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_end', '']], loopCommandList)

        # instruction line containing 2 seqdiag loop commands
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times ' + SEQDIAG_LOOP_START_END_TAG + ' 5 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start_end',  '5 times']], loopCommandList)

        # instruction line containing 2 seqdiag loop end ommand
        instructionLine = SEQDIAG_LOOP_END_TAG + ' ' + SEQDIAG_LOOP_END_TAG
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_end', ''], [':seqdiag_loop_end', '']], loopCommandList)

        # instruction line containing several seqdiag loop commands, some
        # specifying time with no 's'
        instructionLine = SEQDIAG_LOOP_START_TAG + ' three time ' + SEQDIAG_LOOP_START_END_TAG + ' 5 times ' + SEQDIAG_LOOP_START_END_TAG + '     at least fifty time ' + SEQDIAG_LOOP_START_TAG + ' 30 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([[':seqdiag_loop_start', 'three time'], [':seqdiag_loop_start_end', '5 times'], [':seqdiag_loop_start_end', 'at least fifty time'], [':seqdiag_loop_start', '30 times']], loopCommandList)

        # instruction line containing no seqdiag loop command
        instructionLine = 'if a > 45'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertIsNone(loopCommandList)

if __name__ == '__main__':
    unittest.main()

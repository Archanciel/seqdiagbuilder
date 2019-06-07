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

    def testLoopIndexDictionaryClassLoopNestedInnerOne(self):
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
        self.assertEqual(value_20[0], [':seqdiag_loop_end', None])

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
        self.assertEqual(value_20[0], [':seqdiag_loop_end', None])

    def testExtractLoopTimeNumberOneLoopTagOnInstructionLine(self):
        '''
        Tests the extractLoopTimeNumber() on instruction line with only one seqdiag loop tag.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        # using 1 space to separate time from loop start tag
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        # using 1 tab to separate time from loop start tag, time with no 's' !
        instructionLine = SEQDIAG_LOOP_START_TAG + '\t3 time'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 time')

        # using 2 spaces to separate time from loop start end tag
        instructionLine = SEQDIAG_LOOP_START_END_TAG + '  3 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_END_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        # not using 'times' word
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 '
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3')

    def testExtractLoopTimeNumberTwoLoopTagOnInstructionLine(self):
        '''
        Tests the extractLoopTimeNumber() on instruction line with two seqdiag loop tags.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        # adding space before times info
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times' + SEQDIAG_LOOP_START_END_TAG + ' 5 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_END_TAG, instructionLine)
        self.assertEqual(loopTime, '5 times')

        # adding tab before times info
        instructionLine = SEQDIAG_LOOP_START_TAG + '\t3 times' + SEQDIAG_LOOP_START_END_TAG + '   5 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_END_TAG, instructionLine)
        self.assertEqual(loopTime, '5 times')

        # adding tab before seqdiag loop command
        instructionLine = SEQDIAG_LOOP_START_TAG + '\t3 times' + "\t" + SEQDIAG_LOOP_START_END_TAG + '   5 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_END_TAG, instructionLine)
        self.assertEqual(loopTime, '5 times')

        # adding spaces before seqdiag loop command
        instructionLine = "   " + SEQDIAG_LOOP_START_TAG + '\t3 times' + "\t" + SEQDIAG_LOOP_START_END_TAG + '   5 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_END_TAG, instructionLine)
        self.assertEqual(loopTime, '5 times')

    def testExtractLoopCommandsFromLine(self):
        '''
        Testing legal seqdiag loop commands with loop time specification
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        # instruction line containing 1 seqdiag loop command
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([':seqdiag_loop_start 3 times'], loopCommandList)

        # instruction line containing 2 seqdiag loop commands
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times' + SEQDIAG_LOOP_START_END_TAG + ' 5 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([':seqdiag_loop_start 3 times', ':seqdiag_loop_start_end 5 times'], loopCommandList)

        # instruction line containing several seqdiag loop commands, some
        # specifying time with no 's'
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 time' + SEQDIAG_LOOP_START_END_TAG + ' 5 times' + SEQDIAG_LOOP_START_END_TAG + ' 50 time' + SEQDIAG_LOOP_START_TAG + ' 30 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([':seqdiag_loop_start 3 time', ':seqdiag_loop_start_end 5 times', ':seqdiag_loop_start_end 50 time', ':seqdiag_loop_start 30 times'], loopCommandList)


    def testExtractLoopCommandsFromLineWithNoTimeSpecification(self):
        '''
        Testing illegal seqdiag loop commands with no loop time specification.
        The illegal loop comm-nds are ignored !
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        # instruction line containing 1 seqdiag loop command
        instructionLine = SEQDIAG_LOOP_START_TAG
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([], loopCommandList)

        # instruction line containing 2 seqdiag loop commands
        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times' + SEQDIAG_LOOP_START_END_TAG
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual([':seqdiag_loop_start 3 times'], loopCommandList)

        # instruction line containing several seqdiag loop commands
        instructionLine = SEQDIAG_LOOP_START_TAG + ' ' + SEQDIAG_LOOP_START_END_TAG + ' 5 times' + SEQDIAG_LOOP_START_END_TAG + ' ' + SEQDIAG_LOOP_START_TAG + ' 30 times'
        loopCommandList = loopIdxDic.extractLoopCommandsFromLine(instructionLine)
        self.assertEqual(
            [':seqdiag_loop_start_end 5 times',
             ':seqdiag_loop_start 30 times'], loopCommandList)


if __name__ == '__main__':
    unittest.main()

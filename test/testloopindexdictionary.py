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
    def testLoopIndexDictionaryClassLoopNestedInnerOne(self):
        '''
        Test the correct working of the LoopIndexDictionary.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinnerone.py"
        className = 'ClassLoopNestedInnerOne'
        methodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if methodName in entry][0]
            loopIdxDic.storeLoopCommands(className, methodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        key_17 = loopIdxDic.buildKey(className, methodName, 'doCWithNote', 17)

        self.assertIsNotNone(key_17)
        value_17 = loopIdxDic.getLoopCommandListForKey(key_17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start_end', '5 times'])

        key_20 = loopIdxDic.buildKey(className, methodName, 'doC2', 20)
        self.assertIsNotNone(key_20)
        value_20 = loopIdxDic.getLoopCommandListForKey(key_20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', None])

    def testLoopIndexDictionaryClassLoopNestedInnerOneNoTimeInfo(self):
        '''
        Test the correct working of the LoopIndexDictionary for loop tags
        with no time info.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()
        sourcePathFileName = parentdir + "\\testclasses\\classloopnestedinneronefortestloopidxdic.py"
        className = 'ClassLoopNestedInnerOneForTestLoopIdxDic'
        methodName = 'doB'

        with open(sourcePathFileName, "r") as f:
            contentList = f.readlines()
            methodDefLineIndex = [i for (i, entry) in enumerate(contentList) if methodName in entry][0]
            loopIdxDic.storeLoopCommands(className, methodName, methodDefLineIndex + 1, [contentList[methodDefLineIndex:]])

        key_17 = loopIdxDic.buildKey(className, methodName, 'doCWithNote', 17)

        self.assertIsNotNone(key_17)
        value_17 = loopIdxDic.getLoopCommandListForKey(key_17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', None], [':seqdiag_loop_start_end', None])

        key_20 = loopIdxDic.buildKey(className, methodName, 'doC2', 20)
        self.assertIsNotNone(key_20)
        value_20 = loopIdxDic.getLoopCommandListForKey(key_20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', None])

    def testExtractLoopTimeNumberOneLoopTagOnInstructionLine(self):
        '''
        Tests instruction line with only one seqdiag loop tag.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        instructionLine = SEQDIAG_LOOP_START_TAG + '\t3 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        instructionLine = SEQDIAG_LOOP_START_TAG + '  3 times'
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3 times')

        instructionLine = SEQDIAG_LOOP_START_TAG + ' 3 '
        loopTime = loopIdxDic.extractLoopTimeNumber(SEQDIAG_LOOP_START_TAG, instructionLine)
        self.assertEqual(loopTime, '3')

    def testExtractLoopTimeNumberTwoLoopTagOnInstructionLine(self):
        '''
        Tests instruction line with two seqdiag loop tags.
        :return:
        '''
        loopIdxDic = LoopIndexDictionary()

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


if __name__ == '__main__':
    unittest.main()

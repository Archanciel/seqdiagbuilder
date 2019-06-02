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
        value_17 = loopIdxDic.get(key_17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', '3 times'], [':seqdiag_loop_start_end', '5 times'])

        key_20 = loopIdxDic.buildKey(className, methodName, 'doC2', 20)
        self.assertIsNotNone(key_20)
        value_20 = loopIdxDic.get(key_20)
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
        value_17 = loopIdxDic.get(key_17)
        self.assertEqual(len(value_17), 2)
        self.assertEqual(value_17[0], [':seqdiag_loop_start', None], [':seqdiag_loop_start_end', None])

        key_20 = loopIdxDic.buildKey(className, methodName, 'doC2', 20)
        self.assertIsNotNone(key_20)
        value_20 = loopIdxDic.get(key_20)
        self.assertEqual(value_20[0], [':seqdiag_loop_end', None])

if __name__ == '__main__':
    unittest.main()

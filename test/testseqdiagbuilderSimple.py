import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone

from seqdiagbuilder import SeqDiagBuilder
from seqdiagbuilder import FlowEntry
from seqdiagbuilder import RecordedFlowPath
import collections


class TestSeqDiagBuilderSimple(unittest.TestCase):


    def testFlowEntryEq(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe2 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'f', '(a, b)', 'RetClass')
        fe5 = FlowEntry('A', 'e', 'g', '(a, b)', 'RetClass')
        fe6 = FlowEntry('A', 'e', 'f', '(a, w)', 'RetClass')
        fe7 = FlowEntry('A', 'e', 'f', '(a, b)', '')

        self.assertTrue(fe1 == fe2)
        self.assertTrue(fe1 == fe3)
        self.assertFalse(fe1 == fe4)
        self.assertFalse(fe1 == fe5)
        self.assertFalse(fe1 == fe6)
        self.assertFalse(fe1 == fe7)


    @unittest.skip
    def testFlowEntryToString(self):
        fe1 = FlowEntry('A', 'e', 'B', 'f', '95', '(a, b)', 'f_RetType')
        self.assertEqual('A.e, B.f, 95, (a, b), f_RetType', str(fe1))


    @unittest.skip
    def testFlowEntryCreateReturnTypeVaryingMaxArgNum(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'a, b, c, d')
        self.assertEqual(fe.createReturnType(None, None), 'a, b, c, d')
        self.assertEqual(fe.createReturnType(4, None), 'a, b, c, d')
        self.assertEqual(fe.createReturnType(5, None), 'a, b, c, d')
        self.assertEqual(fe.createReturnType(3, None), 'a, b, c, ...')
        self.assertEqual(fe.createReturnType(1, None), 'a, ...')
        self.assertEqual(fe.createReturnType(0, None), '...')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', '')
        self.assertEqual(fe.createReturnType(None, None), '')
        self.assertEqual(fe.createReturnType(0, None), '')
        self.assertEqual(fe.createReturnType(1, None), '')
        self.assertEqual(fe.createReturnType(2, None), '')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'a')
        self.assertEqual(fe.createReturnType(None, None), 'a')
        self.assertEqual(fe.createReturnType(0, None), '...')
        self.assertEqual(fe.createReturnType(1, None), 'a')
        self.assertEqual(fe.createReturnType(2, None), 'a')


    def testFlowEntryCreateSignatureVaryingMaxSigArgNum(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '(a, b, c, d)', 'f_RetType')
        self.assertEqual(fe.createSignature(None, None), '(a, b, c, d)')
        self.assertEqual(fe.createSignature(4, None), '(a, b, c, d)')
        self.assertEqual(fe.createSignature(5, None), '(a, b, c, d)')
        self.assertEqual(fe.createSignature(3, None), '(a, b, c, ...)')
        self.assertEqual(fe.createSignature(1, None), '(a, ...)')
        self.assertEqual(fe.createSignature(0, None), '(...)')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'f_RetType')
        self.assertEqual(fe.createSignature(None, None), '()')
        self.assertEqual(fe.createSignature(0, None), '()')
        self.assertEqual(fe.createSignature(1, None), '()')
        self.assertEqual(fe.createSignature(2, None), '()')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '(a)', 'f_RetType')
        self.assertEqual(fe.createSignature(None, None), '(a)')
        self.assertEqual(fe.createSignature(0, None), '(...)')
        self.assertEqual(fe.createSignature(1, None), '(a)')
        self.assertEqual(fe.createSignature(2, None), '(a)')


    @unittest.skip
    def testFlowEntryCreateReturnTypeVaryingMaxReturnTypeCharLen(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'aaa, bbb, ccc, ddd')
        self.assertEqual(fe.createReturnType(None, None), 'aaa, bbb, ccc, ddd')
        self.assertEqual(fe.createReturnType(None, 100), 'aaa, bbb, ccc, ddd')
        self.assertEqual(fe.createReturnType(None, 0), '...')
        self.assertEqual(fe.createReturnType(None, 8), 'aaa, ...')
        self.assertEqual(fe.createReturnType(None, 7), '...')
        self.assertEqual(fe.createReturnType(None, 13), 'aaa, bbb, ...')
        self.assertEqual(fe.createReturnType(None, 12), 'aaa, ...')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '', '')
        self.assertEqual(fe.createReturnType(None, None), '')
        self.assertEqual(fe.createReturnType(None, 100), '')
        self.assertEqual(fe.createReturnType(None, 0), '')


    def testFlowEntryCreateSignatureVaryingMaxSigCharLen(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '(aaa, bbb, ccc, ddd)', 'f_RetType')
        self.assertEqual(fe.createSignature(None, None), '(aaa, bbb, ccc, ddd)')
        self.assertEqual(fe.createSignature(None, 100), '(aaa, bbb, ccc, ddd)')
        self.assertEqual(fe.createSignature(None, 0), '(...)')
        self.assertEqual(fe.createSignature(None, 10), '(aaa, ...)')
        self.assertEqual(fe.createSignature(None, 9), '(...)')
        self.assertEqual(fe.createSignature(None, 15), '(aaa, bbb, ...)')
        self.assertEqual(fe.createSignature(None, 14), '(aaa, ...)')

        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'f_RetType')
        self.assertEqual(fe.createSignature(None, None), '()')
        self.assertEqual(fe.createSignature(None, 100), '()')
        self.assertEqual(fe.createSignature(None, 0), '()')


    @unittest.skip
    def testFlowEntryReturnTypeVaryingMaxArgNumAndMaxReturnTypeCharLen(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '()', 'aaaa, bbbb, cccc')
        self.assertEqual(fe.createReturnType(2, 14), 'aaaa, ...')
        self.assertEqual(fe.createReturnType(2, 15), 'aaaa, bbbb, ...')
        self.assertEqual(fe.createReturnType(2, 16), 'aaaa, bbbb, ...')
        self.assertEqual(fe.createReturnType(3, 15), 'aaaa, bbbb, ...')
        self.assertEqual(fe.createReturnType(3, 16), 'aaaa, bbbb, cccc')
        self.assertEqual(fe.createReturnType(3, 17), 'aaaa, bbbb, cccc')
        self.assertEqual(fe.createReturnType(4, 15), 'aaaa, bbbb, ...')
        self.assertEqual(fe.createReturnType(4, 16), 'aaaa, bbbb, cccc')
        self.assertEqual(fe.createReturnType(4, 17), 'aaaa, bbbb, cccc')


    def testFlowEntryCreateSignatureVaryingMaxSigArgNumAndMaxSigCharLen(self):
        fe = FlowEntry('A', 'e', 'B', 'f', '95', '(aaaa, bbbb, cccc)', 'f_RetType')
        self.assertEqual(fe.createSignature(2, 16), '(aaaa, ...)')
        self.assertEqual(fe.createSignature(2, 17), '(aaaa, bbbb, ...)')
        self.assertEqual(fe.createSignature(2, 18), '(aaaa, bbbb, ...)')
        self.assertEqual(fe.createSignature(3, 17), '(aaaa, bbbb, ...)')
        self.assertEqual(fe.createSignature(3, 18), '(aaaa, bbbb, cccc)')
        self.assertEqual(fe.createSignature(3, 19), '(aaaa, bbbb, cccc)')
        self.assertEqual(fe.createSignature(4, 17), '(aaaa, bbbb, ...)')
        self.assertEqual(fe.createSignature(4, 18), '(aaaa, bbbb, cccc)')
        self.assertEqual(fe.createSignature(4, 19), '(aaaa, bbbb, cccc)')


    @unittest.skip
    def testAddIfNotInNoCallBeforeEntryPoint(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'f', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('B', 'f')
        rfp.addIfNotIn(fe1)
        rfp.addIfNotIn(fe3)
        rfp.addIfNotIn(fe4)
        self.assertEqual('A.e, B.f, (a, b), RetClass\nA.e, C.f, (a, b), RetClass\nC.f, B.f, (a, b), RetClass\n',str(rfp))


    @unittest.skip
    def testAddIfNotInOneCallBeforeEntryPoint(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'f', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('C', 'f')
        rfp.addIfNotIn(fe1)
        rfp.addIfNotIn(fe3)
        rfp.addIfNotIn(fe4)
        self.assertEqual('A.e, C.f, (a, b), RetClass\nC.f, B.f, (a, b), RetClass\n',str(rfp))


    @unittest.skip
    def testAddIfNotInNCallsBeforeEntryPoint(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('B', 'j')
        rfp.addIfNotIn(fe1)
        rfp.addIfNotIn(fe3)
        rfp.addIfNotIn(fe4)
        self.assertEqual('C.f, B.j, (a, b), RetClass\n',str(rfp))


    @unittest.skip
    def testAddIfNotInNCallsBeforeEntryPointEntryPointAddedTwice(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')
        fe5 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('B', 'j')
        rfp.addIfNotIn(fe1)
        rfp.addIfNotIn(fe3)
        rfp.addIfNotIn(fe4)
        rfp.addIfNotIn(fe5)
        self.assertEqual('C.f, B.j, (a, b), RetClass\n',str(rfp))


    @unittest.skip
    def testAddIfNotInNCallsBeforeEntryPointEntryPointAddedTwiceWithSubsequentEntries(self):
        fe4 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')
        fe5 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('B', 'j')
        rfp.addIfNotIn(fe1) # before entry point: will not be added
        rfp.addIfNotIn(fe3) # before entry point: will not be added
        rfp.addIfNotIn(fe4)
        rfp.addIfNotIn(fe5)
        rfp.addIfNotIn(fe1) # after entry point: will  be added
        rfp.addIfNotIn(fe3) # after entry point: will  be added
        self.assertEqual('C.f, B.j, (a, b), RetClass\nA.e, B.f, (a, b), RetClass\nA.e, C.f, (a, b), RetClass\n',str(rfp))


    @unittest.skip
    def testAddIfNotInEntryPointNeverReached(self):
        fe1 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe3 = FlowEntry('A', 'e', 'f', '(a, b)', 'RetClass')
        fe4 = FlowEntry('C', 'f', 'j', '(a, b)', 'RetClass')

        rfp = RecordedFlowPath('A', 'a')
        rfp.addIfNotIn(fe1)
        rfp.addIfNotIn(fe3)
        rfp.addIfNotIn(fe4)
        self.assertEqual('',str(rfp))


    @unittest.skip
    def testWithBackSlash(self):
        from configurationmanager import ConfigurationManager
        from guioutputformater import GuiOutputFormater
        from controller import Controller
        import os

        SeqDiagBuilder.activate('Controller', 'getPrintableResultForInput')  # activate sequence diagram building

        if os.name == 'posix':
            FILE_PATH = '/sdcard/cryptopricer.ini'
        else:
            FILE_PATH = 'c:\\temp\\cryptopricer.ini'

        configMgr = ConfigurationManager(FILE_PATH)
        controller = Controller(GuiOutputFormater(configMgr), configMgr)

        inputStr = 'mcap btc 0 all'
        _, _, _, _ = controller.getPrintableResultForInput(
            inputStr)

        SeqDiagBuilder.createDiagram('c:\\temp\\', 'GUI', None, 20)


    @unittest.skip
    def testWithSlash(self):
        from configurationmanager import ConfigurationManager
        from guioutputformater import GuiOutputFormater
        from controller import Controller
        import os

        SeqDiagBuilder.activate('Controller', 'getPrintableResultForInput')  # activate sequence diagram building

        if os.name == 'posix':
            FILE_PATH = '/sdcard/cryptopricer.ini'
        else:
            FILE_PATH = 'c:\\temp\\cryptopricer.ini'

        configMgr = ConfigurationManager(FILE_PATH)
        controller = Controller(GuiOutputFormater(configMgr), configMgr)

        inputStr = 'mcap btc 0 all'
        _, _, _, _ = controller.getPrintableResultForInput(
            inputStr)

        SeqDiagBuilder.createDiagram('c:/temp', 'GUI', None, 20)


    def test_splitNoteToLines(self):
        note = 'a long class description. Which occupies several lines.'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], 'a long class description.')
        self.assertEqual(multilineNote[1], 'Which occupies several lines.')


    def test_splitNoteToLinesEmptyNote(self):
        note = ''
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 0)


    def test_splitNoteToLinesOneWordNoteLenEqualsMaxNoteLineLenMinusOne(self):
        note = '12345678911234567892123456789'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 1)
        self.assertEqual(multilineNote[0], '12345678911234567892123456789')


    def test_splitNoteToLinesOneWordNoteLenEqualsMaxNoteLineLen(self):
        note = '123456789112345678921234567893'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 1)
        self.assertEqual(multilineNote[0], '123456789112345678921234567893')


    def test_splitNoteToLinesOneWordNoteLenEqualsMaxNoteLineLenPlusOne(self):
        note = '1234567891123456789212345678931'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 1)
        self.assertEqual(multilineNote[0], '1234567891123456789212345678931')


    def test_splitNoteToLinesTwoWordsNoteLenEqualsMaxNoteLineLen(self):
        note = '12345678911234 567892123456789'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 1)
        self.assertEqual(multilineNote[0], '12345678911234 567892123456789')


    def test_splitNoteToLinesTwoWordsNoteLenEqualsMaxNoteLineLenPlusOne(self):
        note = '123456789112345 678921234567893'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '123456789112345')
        self.assertEqual(multilineNote[1], '678921234567893')


    def test_splitNoteToLinesTwoWordsNoteLenEqualsMaxNoteLineLenPlusTwo(self):
        note = '123456789112345 6789212345678931'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '123456789112345')
        self.assertEqual(multilineNote[1], '6789212345678931')


    def test_splitNoteToLinesTwoWordsFirstEqualsMaxLen(self):
        note = '123456789112345678921234567893 2'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '123456789112345678921234567893')
        self.assertEqual(multilineNote[1], '2')


    def test_splitNoteToLinesTwoWordsFirstEqualsMaxLenPlusOne(self):
        note = '1234567891123456789212345678931 3'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '1234567891123456789212345678931')
        self.assertEqual(multilineNote[1], '3')


    def test_splitNoteToLinesTwoWordsFirstAndSecondEqualsMaxLen(self):
        note = '123456789112345678921234567893 123456789112345678921234567893'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '123456789112345678921234567893')
        self.assertEqual(multilineNote[1], '123456789112345678921234567893')


    def test_splitNoteToLinesTwoWordsFirstAndSecondEqualsMaxLenPlusOne(self):
        note = '1234567891123456789212345678931 1234567891123456789212345678931'
        maxNoteLineLen = 30

        multilineNote = SeqDiagBuilder._splitNoteToLines(note, maxNoteLineLen)

        self.assertEqual(len(multilineNote), 2)
        self.assertEqual(multilineNote[0], '1234567891123456789212345678931')
        self.assertEqual(multilineNote[1], '1234567891123456789212345678931')


    def test__buildClassNoteSection(self):
        participantDocOrderedDic = collections.OrderedDict()
        participantDocOrderedDic['Controller'] = 'Entry point of the business layer'
        participantDocOrderedDic['Requester'] = 'Parses the user commands'
        participantDocOrderedDic['CommandPrice'] = ''
        participantDocOrderedDic['Processor'] = ''
        participantDocOrderedDic['PriceRequester'] = 'Obtains the RT or historical rates from the Cryptocompare web site'
        maxNoteLineLen = 30

        participantSection = SeqDiagBuilder._buildClassNoteSection(participantDocOrderedDic, maxNoteLineLen)
        self.assertEqual(
'''participant Controller
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
		Obtains the RT or historical rates from the
		Cryptocompare web site
	end note
''', participantSection)


if __name__ == '__main__':
    unittest.main()

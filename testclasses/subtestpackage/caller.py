from testclasses.subtestpackage.filereader import FileReader
from testclasses.subtestpackage.filereadersupportingverbosemode import FileReaderSupportingVerboseMode

class Caller:
    def call(self):
        fr = FileReader('testfile.txt')
        print(fr.getContentAsList())

    def callUsingTwoFileReaders(self):
        fr1 = FileReader('testfile.txt')
        print(fr1.getContentAsList())
        fr2 = FileReader('testfile2.txt')
        print(fr2.getContentAsList())

    def callUsingVerboseFileReader(self):
        fr = FileReaderSupportingVerboseMode('testfile.txt', False)
        print(fr.getContentAsList())

    def callUsingVerboseFileReaderWithCallToSuper(self):
        fr = FileReaderSupportingVerboseMode('testfile.txt', False)
        print(fr.getContentAsListFromSuper())

if __name__ == '__main__':
    c = Caller()
    c.call()
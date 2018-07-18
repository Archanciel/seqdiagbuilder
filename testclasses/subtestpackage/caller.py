from testclasses.subtestpackage.filereader import FileReader

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
        fr = FileReader('testfile.txt')

if __name__ == '__main__':
    c = Caller()
    c.call()
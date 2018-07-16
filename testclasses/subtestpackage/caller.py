from testclasses.subtestpackage.filereader import FileReader

class Caller:
    def call(self):
        fr = FileReader('testfile.txt')
        print(fr.getContentAsList())


if __name__ == '__main__':
    c = Caller()
    c.call()
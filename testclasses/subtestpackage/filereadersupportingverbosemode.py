from testclasses.subtestpackage.filereader import FileReader
from seqdiagbuilder import SeqDiagBuilder

class FileReaderSupportingVerboseMode(FileReader):
    def __init__(self, fileName, isVerbose):
        super().__init__(fileName)

        self.isVerbose = isVerbose

        if self.isVerbose:
            print(self.content)

    def getContentAsList(self):
        SeqDiagBuilder.recordFlow()

        return self.content

    def getContentAsListFromSuper(self):
        SeqDiagBuilder.recordFlow()

        return super().getContentAsList()

if __name__ == '__main__':
    pass
from seqdiagbuilder import SeqDiagBuilder

class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.content = ''

        with open(self.fileName, 'r') as f:
            self.content = f.readlines()

    def getContentAsList(self):
        SeqDiagBuilder.recordFlow()

        return self.content

if __name__ == '__main__':
    pass
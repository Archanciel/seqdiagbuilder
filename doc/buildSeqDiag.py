from doc.classa import ClassA
from seqdiagbuilder import SeqDiagBuilder
import os, inspect

def createSeqDiagram():
    a = ClassA()
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    SeqDiagBuilder.activate(projectPath=currentdir, entryClass='ClassA', entryMethod='doA')

    a.doA(1)

    SeqDiagBuilder.createDiagram(targetDriveDirName='c:/temp', actorName='User')

    SeqDiagBuilder.deactivate()

if __name__ == '__main__':
    createSeqDiagram()

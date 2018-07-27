import os, inspect, sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from seqdiagbuilder import SeqDiagBuilder
from doc.classa import ClassA

def createSeqDiagram():
    a = ClassA()
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    SeqDiagBuilder.activate(projectPath=currentdir, entryClass='ClassA', entryMethod='doWork')

    a.doWork(1)

    SeqDiagBuilder.createDiagram(targetDriveDirName='c:/temp', actorName='User')
    SeqDiagBuilder.deactivate()

if __name__ == '__main__':
    createSeqDiagram()
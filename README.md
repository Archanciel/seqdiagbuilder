
# SeqDiagBuilder

This utility generates a UML sequence diagram on Python code using data collected at execution time.

## Principle

SeqDiagBuilder does its job in two steps:
1. It first collects control flow data during Python code execution.
2. Using the collected control flow data, it generates a PlantUML sequence diagram command file.

Then, PlantUML can be launched on the generated command file to draw the sequence diagram, storing it in an svg or png file. The svg file can be opened in a web browser to display the diagram.

Step 1 requires the insertion of a single line of code in the leaf or lowest level methods which are to be displayed in the sequence diagram.

The code to insert in the leaf method is
...

    from seqdiagbuilder import SeqDiagBuilder
    ...
    <your method code here>
    ...
    SeqDiagBuilder.recordFlow()


## Example
Here's a very basic usage of SeqDiagBuilder followed by the
generated PlantUML command file and the sequence diagram 
drawned from it. 

The example draws a sequence diagram of the collaboration of two classes: ClassA, which calls a method of ClassB.

In order to build a sequence diagram in your Python code, simply
copy seqdiagbuilder.py in your project.

Here's the code of the two classes:

#### ClassA
```
from classb import ClassB

class ClassA:
    '''
    ClassA is the entry point of our sequence diagram.
    '''
    def doWork(self, p1):
        '''
        doWork() is the entry method of our sequence diagram.
        
        :param p1:
        :return:
        '''
        b = ClassB()
        b.do(p1)
```
#### ClassB
```
from seqdiagbuilder import SeqDiagBuilder

class ClassB:
    def do(self, p1):
        '''
        This the leaf method of our sequence diagram.
        
        :param p1:
        :return:
        '''
        
        # The next instruction causes SeqDiagBuilder to record the
        # whole control flow which conducted to call the present method.
        seqdiagbuilder.SeqDiagBuilder.recordFlow()
```
#### Code using SeqDiagBuilder
The code below does three things: it first instanciates ClassA. Then it activates 
SeqDiagBuilder so that the utility will record the control flow information during 
the execution of ClassA.
```
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
```
#### Generated PlantUML command file
```
@startuml

actor User
participant ClassA
participant ClassB
User -> ClassA: doWork(p1)
	activate ClassA
	ClassA -> ClassB: do(p1)
		activate ClassB
		ClassA <-- ClassB:
		deactivate ClassB
	User <-- ClassA:
	deactivate ClassA
@enduml
```
#### Corresponding sequence diagram
![](doc/basic_usage_seq_diagr.jpg)

Later in this document, more detailed and complete informations on
SeqDiagBuilder usage is provided. In the end, a section is devoted to
the inner working and implementation of SeqDiagBuilder in order to
facilitate its extension / improvement by any motivated developer.

## Usage

### SeqDiagBuilder tags
* **:seqdiag_return** This tag can be added anywhere in the method doc to specify the return type to attach in the sequence diagram to the call of this method
* **:seqdiag_select_method** Used in the context where a method is defined at different levels in a class hierarchy. This tag is useful only if the classes of the hierarchy are defined in the same file ! In this case, SeqDiagBuilder selects by default the parent class method (the one at the highest level in the hierchy. Use this tag anywhere in the method doc to override the default.
* **:seqdiag_note** Used either in class or in method doc. Use \r to force a line break. But a better solution is to specify maxSigArgNum=None, maxSigCharLen=30 for example when calling SeqDiagBuilder.createSeqDiaqCommands() or SeqDiagBuilder.createDiagram().
## Installing PlantUML

Download plantuml.jar from http://plantuml.com/starting
* To be executed, plantUML requires Java to be installed !

Running PlantUML on a command file

java -jar plantuml.jar -tsvg plantUML_commands_file

### Warning
If your plantUML command file name contains spaces, you may have to surround it with quotation marks ("):

java -jar plantuml.jar -tsvg "plantUML commands file.txt"
## Required libraries

## Note
I am currently involved in studying Machine Learning. But if asked, I could consider devoting some time completing this documentation.


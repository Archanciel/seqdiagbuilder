# SeqDiagBuilder

Generates a UML sequence diagram on Python code using data collected at execution time.

## Principle
SeqDiagBuilder does its job in two steps:
1. It first collects control flow data during program execution.
2. Using the collected control flow data, it generates a PlantUML sequence diagram command file.

Then, PlantUML can be launched on the generated command file to draw the sequence diagram, storing it in an svg file. The svg file can be opened in a web browser to display the diagram.

Step 1 requires the insertion of a single line of code in the leaf or lowest level methods which are to be displayed in the sequence diagram.

The code to insert is
```
from seqdiagbuilder import SeqDiagBuilder
...
    SeqDiagBuilder.recordFlow()
```

## Usage

### SeqDiagBuilder tags
* **:seqdiag_return** This tag can be added anywhere in the method documentation to specify the return type to attach in the sequence diagram to the call of this method
* **:seqdiag_select_method** Used in the context where a method is defined at different levels in a class hierarchy. This tag is useful only if the classes of the hierarchy are defined in the same file ! In this case, SeqDiagBuilder selects by default the parent class method (the one at the highest level in the hierchy. Use this tag anywhere in the method documentation to override the default.
* **:seqdiag_note** Used either in class or in method documentation. Use \r to force a line break. But a better solution is to specify maxSigArgNum=None, maxSigCharLen=30 for example when calling SeqDiagBuilder.createSeqDiaqCommands() or SeqDiagBuilder.createDiagram().
## Installing PlantUML

Download plantuml.jar from http://plantuml.com/starting
* To be executed, plantUML requires Java to be installed !

## Running PlantUML on a command file

java -jar plantuml.jar -tsvg plantUML_commands_file

## Required libraries

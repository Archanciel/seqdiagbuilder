# SeqDiagBuilder

Generates a UML sequence diagram on Python code using data collected at execution time.

## Principle
SeqDiagBuilder does its job in four steps:
1. record control flow data during program execution
2. generate a PlantUML sequence diagram command file
3. launch PlantUML on the generated command file to draw a sequence diagram in an svg file
4. open the svg file in a browser to display the sequence diagram

Step 1 requires the insertion of a single line of code in the leaf methods which are to be displayed in the sequence diagram.

The code to insert is
```
from seqdiagbuilder import SeqDiagBuilder
...
    SeqDiagBuilder.recordFlow()
```

## Usage

### SeqDiagBuilder tags
* **:seqdiag_return** This tag can be added anywhere in the method documentation to specify the return type to attach in the sequence diagram to the call of this method
* **:seqdiag_select_method** Used in the context where a method is defined at different levels in a class hierarchy. In this case, SeqDiagBuilder selects by default the parent class method (the one at the highest level in the hierchy. Use this tag anywhere in the method documentation to override the default.
* **:seqdiag_note** Used either in class or in method documentation. Use \r to force a line break. But a better solution is to specify maxSigArgNum=None, maxSigCharLen=30 for example when calling SeqDiagBuilder.createSeqDiaqCommands() or SeqDiagBuilder.createDiagram().
## Installing PlantUML

Download plantuml.jar from http://plantuml.com/starting
* To be executed, plantUML requires Java to be installed !

## Running PlantUML on a command file

java -jar plantuml.jar -tsvg plantUML_commands_file

## Required libraries

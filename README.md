# SeqDiagBuilder

Generates a UML sequence diagram on Python code using data collected at execution time.

## Usage

### SeqDiagBuilder tags
* **:seqdiag_return** This tag can be added anywhere in the method documentation to specify the return type to attach in the sequence diagram to the call of this method
* **:seqdiag_select_method** Used in the context where a method is defined at different levels in a class hierarchy. In this case, SeqDiagBuilder selects by default the parent class method (the one at the highest level in the hierchy. Use this tag anywhere in the method documentation to override the default.
## Installing PlantUML

Download plantuml.jar from http://plantuml.com/starting
* To be executed, plantUML requires Java to be installed !

## Running PlantUML on a command file

java -jar plantuml.jar -tsvg plantUML_commands_file

## Required libraries

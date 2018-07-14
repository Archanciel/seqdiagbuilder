# SeqDiagBuilder

Generates a UML sequence diagram on Python code using data collected at execution time.

## Usage

### SeqDiagBuilder tags
* **:seqdiag_return** this tag can be added anywhere in the method documentation to specify the return type to attach in the sequence diagram to the call of this method

## Installing PlantUML

Download plantuml.jar from http://plantuml.com/starting
* To be executed, plantUML requires Java to be installed !

## Running PlantUML on a command file

java -jar plantuml.jar -tsvg plantUML_commands_file

## Required libraries

# Apitax

Pronounced: *ahhp-ehh-tax*

## Builds

### Packaging Instructions
* Use either Powershell or Bash
* Building the package: `python setup.py sdist bdist_wheel`
* Upload the package to Pypi: `twine upload dist/* -r pypi`
* More information can be found here: https://gist.github.com/ShawnClake/759e9d09af868ef18f8c7b39d1684ad4

### Readme Conversion Instructions
* Install `pandoc` if it is not already installed: `sudo apt-get install pandoc`
* Run the command: `pandoc -o readme.docx -f markdown -t docx README.md`

### Compile Antlr Grammar from another directory
This is sometimes nessecary due to a bug in the antlr compiler with regards to paths
* Download the antlr compiler .jar file and save it somewhere.
* Inside of the directory where the .jar was saved, create the following folder heirarchy
    * build
    * src
    * scripts
    * logs
* Create a .bat or .sh file (dependent on OS) and add the following script:
``` bash
java -jar ~/grammar/antlr-4.7.1-complete.jar -Dlanguage=Python3 ~/grammar/src/AhLex210.g4
java -jar ~/grammar/antlr-4.7.1-complete.jar -lib ~/grammar/src -o ~/grammar/build -listener -visitor -Dlanguage=Python3 ~/grammar/src/Ah210.g4
cp -r ~/grammar/build/* ~/Apitax/apitax/grammar/build
cp ~/grammar/src/AhLex210.g4 ~/Apitax/apitax/grammar/src
cp ~/grammar/src/Ah210.g4 ~/Apitax/apitax/grammar/src
```
* Anytime you want to make changes to the grammar, do it from the new ~/grammar/src directory and run the script

## Documentation and Usage

### Scriptax - Control Flow, Scoping, and Automation

#### Existing keys
* ct("\<someCommand\>") 
    * Commandtax execution
    * A command is executed during the parsing of the line and its response is returned
* set \<someVar\> = \<someValue\>
    * Sets a variable
    * Supports expressions, strings, numbers, booleans, dictionaries, lists, and commandtax responses
* "this is a string {{ someVar }}"
    * Injects the contents of a variable
    * Fancy stuff is possible such as: set newVar = ct("{{someVar}}")
* {{ r: someResponse }}
    * Injects the response of some request
* import ct("some commandtax")
    * Executes a command and imports the response to the current scope
* export ct("some commandtax"), export someVar 
    * Imports the values to the current scope and exports them to allow a parent scope to access these values 
* name \<someName\>
    * Sets the reference name of the script.
    * Supports strings and expressions
* log("log some output to the console & log file")
    * Supports expressions
* cast(\<someVar\>, type)
    * Casts a variable to a type
    * Valid types are: str, num, dict, list 
* // some comment
    * Inline comment
* /* some comment spanning multiple lines */
    * Block comment

#### Coming Soon
* {% if \<someCondition\> %}   \<someExecution\>
* {% if \<someCondition\> %}: \<someSetOfExecutionSpanningMultipleLines\> {% endif %}
* return \<someDataOrOptionallyNoData\>
    * Stops the processing of the current script and gives control back to the parent script
    * The parent script, if importing this subscript, will have access to any data returned by this subscript. The returned data will be directly under the subscripts namespace in the dataStore
        * For example: {"vars": {"someSubScript":{"return": "{"this is": "the returned data"}"}}}
* \<someVariable\> to \<type\>
    * Cast a variable to a type
    * Types: boolean, string, int, float, double, json, object
    * Type checking is not preformed and is expected of the user to know what they are trying to do
* {% for \<someNewVariable\> to range(\<someStart\>,\<someEnd\>) %} \<someExecution\>
* {% for \<someNewVariable\> to \<someEnd\> %} \<someExecution\>
* {% for \<someNewVariable\> in \<someExistingVariableObject\> %} \<someExecution\>
* {% for oneOfTheCasesListedAbove %}: \<someSetOfExecutionSpanningMultipleLines\> {% endfor %}
* require <someData>
    * Provide a means for a parent script to gather all of the data it will need to run from the executing user

#### Tidbits
* You can use arrays via dot notation
    * set someVar.1 = num1
    * set someVar.2 = num2
    * set someVar.{{counter}} = num3
    * When doing this, the first usage of a variable must either be someVar = "{}" or an index as part of that object. Failure to do this will result in errors being thrown.


### Commandtax - Data Gathering, Manipulating, Usage

#### Existing
* script \<pathToSomeScript\>
    * Executes the script file specified
* custom \<someCustomCommand\>
    * Execute some custom command
		

#### Coming Soon
* shell \<someCommand\>
    * Runs the command in the shell and returns the response from the shell		

Tidbits


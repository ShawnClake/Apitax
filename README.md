# Apitax

Pronounced: *ahhp-ehh-tax*

### Build Instructions
* Use either Powershell or Bash
* Building the package: `python setup.py sdist bdist_wheel`
* Upload the package to Pypi: `twine upload dist/* -r pypi`
* More information can be found here: https://gist.github.com/ShawnClake/759e9d09af868ef18f8c7b39d1684ad4


### Scriptax - Control Flow, Scoping, and Automation

#### Existing keys
* {% \<someCommand\> %} 
    * Inline execution
    * A command is executed during the parsing of the line and its response is returned
* \> \<someCommand\>
    * Command execution
    * The command is executed after line parsing and the response is ignored
* set \<someVar\> = \<someValue\>, set \<someVar\> = {% \<someCommand\> %}
    * Sets a variable
* {{ someVar }}
    * Injects the contents of a variable
    * Fancy stuff is possible such as: set newVar = {% {{someVar}} %}
* {{ r: someResponseVar }}
    * Injects the response of some variable
* import {% someCommand %}
    * Executes a command and imports the response to the current scope
* export {% someCommand %}, export someVar 
    * Imports the values to the current scope and exports them to allow a parent scope to access these values 
* name \<someName\>
    * Sets the reference name of the script. If this is not specified, it'll default to the file name

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


### Commandtax - Data Gathering, Manipulating, Usage

#### Existing
* script \<pathToSomeScript\>
    * Executes the script file specified
* custom \<someCustomCommand\>
    * Execute some custom command
		

#### Coming Soon
* shell \<someCommand\>
    * Runs the command in the shell and returns the response from the shell
* eval \<someExpression\>
    * Evaluate the provided expression and return the result
		

Tidbits


# MnemonicParserV2 Class Documentation

## Table of Contents

* [1. Introduction](#1-introduction)
* [2. Class Overview: `MnemonicParserV2`](#2-class-overview-mnemonicparserv2)
    * [2.1 Constructor: `__init__`](#21-constructor-__init__)
    * [2.2 Public Methods: `parse`](#22-public-methods-parse)
* [3. Private Methods](#3-private-methods)
    * [3.1 `__start`](#31-__start)
    * [3.2 `__cleanUp`](#32-__cleanup)
    * [3.3 `__assignMnemonic`](#33-__assignmnemonic)
    * [3.4 Helper Methods](#34-helper-methods)
        * [3.4.1 `__determineData`](#341-__determinedata)
        * [3.4.2 `__isComment`](#342-__iscomment)
        * [3.4.3 `__determineVariableAddress`](#343-__determinevariableaddress)


<a name="1-introduction"></a>
## 1. Introduction

This document provides internal code documentation for the `MnemonicParserV2` class, a parser designed to process assembly-like instructions from a text file.  It converts the raw instructions into a structured representation suitable for further processing.


<a name="2-class-overview-mnemonicparserv2"></a>
## 2. Class Overview: `MnemonicParserV2`

The `MnemonicParserV2` class implements the `IParser` interface (assumed to be defined elsewhere) and is responsible for parsing a file containing assembly-like instructions. It handles comments, labels, and variable addresses. The parser maintains a memory map to track variable addresses.

<a name="21-constructor-__init__"></a>
### 2.1 Constructor: `__init__`

```python
def __init__(self, memoryLimit: int, debug: bool = True):
    super().__init__(debug)
    self.AddressMemoryCounter = 0;
    self.AddressMemoryDict = dict();
    self.labelAddressMap = {};
    self.memoryLimit = memoryLimit
```

The constructor initializes the parser with a `memoryLimit` (integer) defining the maximum addressable memory and a boolean flag `debug` to enable/disable debugging output (defaults to `True`). It also initializes internal data structures:
* `AddressMemoryCounter`: Tracks the number of variables assigned memory addresses.
* `AddressMemoryDict`: A dictionary mapping variable names to their assigned memory addresses.
* `labelAddressMap`: A dictionary mapping labels to their corresponding instruction addresses.


<a name="22-public-methods-parse"></a>
### 2.2 Public Methods: `parse`

```python
def parse(self, fileAddress: str) -> list[Instruction]:
    return self.__start(fileAddress)
```

The `parse` method is the main entry point for parsing a file. It takes the file path (`fileAddress`) as input and returns a list of `Instruction` objects.  It simply delegates the actual parsing to the private `__start` method.


<a name="3-private-methods"></a>
## 3. Private Methods

<a name="31-__start"></a>
### 3.1 `__start`

```python
def __start(self, fileAddress: str) -> list[Instruction]:
    try:
        # ... (debug output) ...
        splittedWords = []
        with open(fileAddress, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                splittedWords.append(word)
                # ... (debug output) ...
        return self.__cleanUp(splittedWords)
    except Exception as e:
        raise e
```

This method reads the input file line by line, splits each line into words, and passes the resulting list of lists (`splittedWords`) to the `__cleanUp` method for further processing.  Error handling is included using a `try-except` block.


<a name="32-__cleanup"></a>
### 3.2 `__cleanUp`

```python
def __cleanUp(self, listOfCommands: list[list[str]])-> list[Instruction]:
    # ... (debug output) ...
    sanitizedCommands = []
    for lineCommand in listOfCommands:
        line = []
        for command in lineCommand:
            if(self.__isComment(command)):
                break
            else:
                line.append(command)
        if line:
            sanitizedCommands.append(line)
            # ... (debug output) ...
    return self.__assignMnemonic(sanitizedCommands)
```

This method removes comments (lines or parts of lines starting with ';') from the list of commands. It iterates through each line and filters out any commands that are comments using the helper method `__isComment`. The cleaned list is then passed to the `__assignMnemonic` method.


<a name="33-__assignmnemonic"></a>
### 3.3 `__assignMnemonic`

```python
def __assignMnemonic(self, sanitizedCommands: list[list[str]]) -> list[Instruction]:
    # ... (debug output) ...
    convertedCommands : list[Instruction]= [] 
    address: int = 0
    # First pass: identify labels and their addresses
    for lineCommand in sanitizedCommands:
        if Mnemonic.JumpMarkerExistsIn(lineCommand):
            label = lineCommand[-1]
            self.labelAddressMap[label] = address
        else: 
            address +=1

    address : int = 0
    # Second pass: create Instruction objects
    for lineCommand in sanitizedCommands:
        mnemonic = Mnemonic.ExtractFrom(lineCommand, address)
        if mnemonic.IsJumpMarker():
            continue
        data:int = self.__determineData(mnemonic, lineCommand, address)
        opcode = Opcode(mnemonic, data)
        instruction = Instruction(address, opcode)
        convertedCommands.append(instruction)
        address += 1
    return convertedCommands
```

This is the core of the parsing logic.  It performs two passes:
1. **Label identification:** The first pass identifies jump labels and stores their addresses in `self.labelAddressMap`.
2. **Instruction creation:** The second pass creates `Instruction` objects. For each line, it extracts the mnemonic using `Mnemonic.ExtractFrom`, determines the data using `__determineData`, creates an `Opcode` object, and finally constructs an `Instruction` object. Jump marker lines are skipped.

<a name="34-helper-methods"></a>
### 3.4 Helper Methods

<a name="341-__determinedata"></a>
#### 3.4.1 `__determineData`

```python
def __determineData(self, mnemonic: Mnemonic, lineCommand, address) -> int:
    if mnemonic.IsIndependent(address, len(lineCommand)):
        return 00
    variable: str = lineCommand[1]
    if mnemonic.IsJumpStatement():
        # ... (debug output) ...
        return self.labelAddressMap.get(variable, "??")
    else:
        return self.__determineVariableAddress(variable)
```

This helper method determines the data component of an instruction.  It checks if the mnemonic is independent (no data needed), a jump statement (data is a label address), or a variable assignment (data is a variable's address).

<a name="342-__iscomment"></a>
#### 3.4.2 `__isComment`

```python
def __isComment(self, command: str) -> bool:
    return command == ";" or command.startswith(";")
```

A simple helper function to check if a given command is a comment.

<a name="343-__determinevariableaddress"></a>
#### 3.4.3 `__determineVariableAddress`

```python
def __determineVariableAddress(self, data:str) -> int:
    if data.isalpha():
        if(data in self.AddressMemoryDict):
            return self.AddressMemoryDict[data]
        else:
            self.AddressMemoryDict[data] = self.memoryLimit - self.AddressMemoryCounter
            self.AddressMemoryCounter += 1
            return self.AddressMemoryDict[data]
    else:
        return data
```

This method assigns memory addresses to variables. If a variable is already in `AddressMemoryDict`, its address is returned. Otherwise, a new address is assigned from the top of memory downwards, and the address is returned.  Non-alphabetic data is returned as is (assuming it's already an address).


# MnemonicParserV1 Class Documentation

## Table of Contents

* [1. Overview](#1-overview)
* [2. Class `MnemonicParserV1`](#2-class-mnemonicparserv1)
    * [2.1 Constructor `__init__`](#21-constructor-__init__)
    * [2.2 Method `parse`](#22-method-parse)
    * [2.3 Method `__start`](#23-method-__start)
    * [2.4 Method `__cleanUp`](#24-method-__cleanup)
    * [2.5 Method `__assignMnemonic`](#25-method-__assignmnemonic)
    * [2.6 Helper Method `__isComment`](#26-helper-method-__iscomment)


## 1. Overview

This document details the `MnemonicParserV1` class, responsible for parsing assembly-like files and converting them into a list of `Instruction` objects.  The parser handles comments and assigns opcodes based on a provided mnemonic library.


## 2. Class `MnemonicParserV1`

This class implements the `IParser` interface and provides a basic assembly language parser.

### 2.1 Constructor `__init__`

```python
def __init__(self, mnemonicLibray = MnemonicLibrary, debug: bool = True):
    super().__init__(debug)
    self.mnemonicLibrary = mnemonicLibray.DEFAULT_MNEMONIC
```

The constructor initializes the `MnemonicParserV1` object. It takes an optional `mnemonicLibrary` (defaulting to `MnemonicLibrary.DEFAULT_MNEMONIC`) and a `debug` flag (defaulting to `True`). The `mnemonicLibrary` provides a mapping of mnemonics to opcodes. The `debug` flag controls the level of diagnostic output during parsing.


### 2.2 Method `parse`

```python
def parse(self, fileAddress: str) -> list[Instruction]:
    return self.__start(fileAddress)
```

The `parse` method is the main entry point for parsing a file. It takes the file address as input and returns a list of `Instruction` objects. It simply delegates the actual parsing work to the `__start` method.


### 2.3 Method `__start`

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
        print(f"Error occurred during file parsing: {e}")
        return []
```

This method reads the assembly file line by line. Each line is split into words using `line.split()`.  The list of words for each line is appended to `splittedWords`.  Error handling is included to catch potential `IOError` or other exceptions during file access.  The `__cleanUp` method is called to process the resulting list.


### 2.4 Method `__cleanUp`

```python
def __cleanUp(self, listOfCommands: list[list[str]])-> list[Instruction]:
    # ... (debug output) ...
    sanitizedCommands = []
    for lineCommand in listOfCommands:
        line = []
        for command in lineCommand:
            if(self.__isComment(command)):
                break  # Stop processing line if comment encountered
            else:
                line.append(command)
        if line: #Avoid adding empty lines
            sanitizedCommands.append(line)
            # ... (debug output) ...

    return self.__assignMnemonic(sanitizedCommands)
```

This method removes comments from each line. If a comment (identified by `__isComment`) is found within a line, processing for that line stops.  The cleaned lines are then passed to `__assignMnemonic`.


### 2.5 Method `__assignMnemonic`

```python
def __assignMnemonic(self, sanitizedCommands: list[list[str]])-> list[Instruction]:
    lineCount: int = 0
    # ... (debug output) ...
    convertedCommands: list[Instruction] = []
    for lineCommand in sanitizedCommands:
        address = lineCount
        mnemonic = lineCommand[0]
        data = lineCommand[1]    
        opcode = str(self.mnemonicLibrary[mnemonic]) + data
        instuction = Instruction(int(address), opcode)
        convertedCommands.append(instuction)
        lineCount += 1

    return convertedCommands
```

This method iterates through the sanitized commands. For each command, it extracts the mnemonic and data, looks up the opcode in `self.mnemonicLibrary`, constructs an `Instruction` object, and appends it to the `convertedCommands` list.  The line number serves as the instruction address.


### 2.6 Helper Method `__isComment`

```python
def __isComment(self, command: str) -> bool:
    return command == ";" or command.startswith(";")
```

This helper method checks if a given string represents a comment.  It returns `True` if the command is either ";" or starts with ";", and `False` otherwise.


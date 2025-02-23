# LowLevelParser Class Documentation

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Class Overview](#1-class-overview)
* [2. `__init__(self, debug: bool = False)`](#2-__init__self-debug-bool--false)
* [3. `parse(self, fileAddress: str) -> list[Instruction]`](#3-parse-self-fileaddress-str---listinstruction)
* [4. `__startParse(self, fileAddress: str) -> list[Instruction]`](#4-__startparse-self-fileaddress-str---listinstruction)
* [5. `__cleanUp(self, listOfCommands: list[list[str]]) -> list[Instruction]`](#5-__cleanup-self-listofcommands-listliststr---listinstruction)


## 1. Class Overview

The `LowLevelParser` class implements the `IParser` interface and is responsible for parsing a text file containing assembly-like instructions.  It reads the file, splits it into individual instructions, cleans up any extraneous characters, and returns a list of `Instruction` objects. The class utilizes a debug mode for enhanced troubleshooting.


## 2. `__init__(self, debug: bool = False)`

This is the constructor for the `LowLevelParser` class.

| Parameter | Type | Description |
|---|---|---|
| `debug` | `bool` |  A boolean flag to enable debug mode. Defaults to `False`. |

The constructor initializes the `debug` attribute inherited from the parent class (`IParser`).


## 3. `parse(self, fileAddress: str) -> list[Instruction]`

This method initiates the parsing process.

| Parameter | Type | Description |
|---|---|---|
| `fileAddress` | `str` | The path to the file to be parsed. |
| **Returns** | `list[Instruction]` | A list of `Instruction` objects representing the parsed instructions. |

This method simply calls the private method `__startParse` to perform the actual parsing and returns the result.


## 4. `__startParse(self, fileAddress: str) -> list[Instruction]`

This private method performs the core parsing logic.

| Parameter | Type | Description |
|---|---|---|
| `fileAddress` | `str` | The path to the file to be parsed. |
| **Returns** | `list[list[str]]` | A list of lists, where each inner list represents a line from the file, split into words. |

**Algorithm:**

1. **File Reading:** The method opens the specified file in read mode (`"r"`).
2. **Line-by-Line Processing:** It reads the file line by line using `readlines()`.
3. **Word Splitting:** Each line is split into a list of words using `line.split()`. Empty lines are skipped.
4. **Debug Output (if enabled):** If `self.debug` is `True`, each line's words are printed to the console.
5. **List Aggregation:**  The list of words for each line is appended to `splittedWords`.
6. **Cleanup:** The `__cleanUp` method is called to sanitize and convert the `splittedWords` list into a list of `Instruction` objects.


## 5. `__cleanUp(self, listOfCommands: list[list[str]]) -> list[Instruction]`

This private method cleans up the list of commands and converts it into a list of `Instruction` objects.

| Parameter | Type | Description |
|---|---|---|
| `listOfCommands` | `list[list[str]]` | A list of lists, where each inner list represents a line of commands. |
| **Returns** | `list[Instruction]` | A list of `Instruction` objects. |

**Algorithm:**

1. **Iteration:** The method iterates through each `lineCommand` in `listOfCommands`.
2. **Comment Handling:** It iterates through each `command` in `lineCommand`. If a semicolon (`;`) is encountered, the rest of the line is ignored (treating it as a comment).
3. **Instruction Creation:** If the line contains commands after removing comments, it creates an `Instruction` object.  It assumes the first element is an integer representing the instruction code and the second element is the instruction operand.
4. **Error Handling (Implicit):**  The code implicitly handles potential errors (e.g., lines with incorrect format) by simply skipping them and continuing to the next line.  More robust error handling might be beneficial in a production environment.
5. **List Appending:** The created `Instruction` object is added to `sanitizedCommands`.
6. **Return Value:** The function returns the `sanitizedCommands` list.



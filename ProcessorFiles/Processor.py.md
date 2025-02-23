# Processor Class Documentation

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Introduction](#1-introduction)
* [2. Class Overview: `Processor`](#2-class-overview-processor)
    * [2.1 Attributes](#21-attributes)
    * [2.2 Methods](#22-methods)
        * [2.2.1 Getter and Setter Methods](#221-getter-and-setter-methods)
        * [2.2.2 `incrementProgramCounter()` Method](#222-incrementprogramcounter-method)
        * [2.2.3 `dump()` Method](#223-dump-method)
        * [2.2.4 `__formatter()` Method](#224-formatter-method)
        * [2.2.5 `update_state()` Method](#225-update-state-method)


## 1. Introduction

This document provides internal code documentation for the `Processor` class. This class simulates a simplified processor with registers and instruction processing capabilities.  It interacts with the `Instruction` class (from `TextProcessors.entities`) to fetch and execute instructions.


## 2. Class Overview: `Processor`

The `Processor` class is designed to mimic the core functionality of a central processing unit (CPU). It maintains several registers to store data and program state, and provides methods to manage and update these registers.

### 2.1 Attributes

The `Processor` class uses private attributes to store its internal state, accessible through getter and setter methods.

| Attribute Name         | Data Type     | Description                                                                 |
|-------------------------|----------------|-----------------------------------------------------------------------------|
| `__accumulator`        | integer        | Stores the result of arithmetic and logical operations.                     |
| `__programCounter`     | integer        | Holds the address of the next instruction to be executed.                 |
| `__instructionRegister` | string         | Stores the currently fetched instruction.                                  |
| `__operationCode`      | integer        | Stores the operation code (opcode) extracted from the instruction.          |
| `__operand`            | string         | Stores the operand (data or address) part of the instruction.             |


### 2.2 Methods

#### 2.2.1 Getter and Setter Methods

The class includes standard getter and setter methods for each attribute, allowing controlled access and modification of the processor's internal state.  These follow a consistent naming pattern (e.g., `accumulator`, `programCounter`, `instructionRegister`, `operationCode`, `operand`).  These methods directly access and modify the respective private attributes.

#### 2.2.2 `incrementProgramCounter()` Method

```python
def incrementProgramCounter(self) -> None:
    self.programCounter += 1
```

This method increments the `programCounter` by 1, advancing to the next instruction in the program sequence.  This is a fundamental step in instruction execution.

#### 2.2.3 `dump()` Method

```python
def dump(self):
    print("REGISTERS: ")
    print(f"accumulator: +{self.__formatter(self.accumulator)}")
    print(f"programCounter: {self.__formatter(self.programCounter, zeroes=2)}")
    print(f"instructionRegister: +{self.__formatter(self.instructionRegister)}")
    print(f"operationCode: {self.__formatter(self.operationCode, zeroes=2)}")
    print(f"operand: {self.__formatter(self.operand, zeroes=2)}")
```

The `dump()` method provides a formatted output of the processor's register contents. It uses the `__formatter()` method (described below) to ensure consistent formatting. The output is designed for debugging purposes.

#### 2.2.4 `__formatter()` Method

```python
def __formatter(self, data, zeroes = 4):
    return str(data).zfill(zeroes)
```

This private helper method formats the data for display in the `dump()` method. It converts the input `data` to a string and pads it with leading zeros to a specified length (`zeroes`).  This ensures consistent formatting of register values, regardless of their magnitude.


#### 2.2.5 `update_state()` Method

```python
def update_state(self, instruction: Instruction):
    operation_code, address = instruction.decode()
    self.instructionRegister = instruction.data
    self.operationCode = operation_code
    self.operand = address
```

This method updates the processor's state based on the provided `Instruction` object.  It uses the `Instruction.decode()` method to extract the operation code and operand from the instruction. The extracted information is then used to update the `instructionRegister`, `operationCode`, and `operand` attributes of the `Processor` instance.  The algorithm involves directly assigning values obtained from the decoded instruction to the respective processor registers.  This method assumes that the `Instruction` class properly handles the decoding process.

# Mnemonic Library Internal Documentation

[Linked Table of Contents](#table-of-contents)

## Table of Contents <a name="table-of-contents"></a>

* [1. Overview](#overview)
* [2. Class `MnemonicLibrary`](#class-mnemoniclibrary)
    * [2.1. Class Attributes](#class-attributes)
    * [2.2.  `DEFAULT_MNEMONIC` Dictionary](#default_mnemonic-dictionary)
    * [2.3. `INDEPENDENT_MNEMONICS` List](#independent_mnemonics-list)
    * [2.4. `RESERVED_KEYWORDS` List](#reserved_keywords-list)


## 1. Overview <a name="overview"></a>

This document details the `MnemonicLibrary` class, which provides a mapping between mnemonic instruction names and their corresponding numerical opcode values.  This mapping is crucial for assembling and disassembling machine code. The library defines several key attributes to manage this mapping and identify reserved keywords.


## 2. Class `MnemonicLibrary` <a name="class-mnemoniclibrary"></a>

The `MnemonicLibrary` class is a simple structure to hold mnemonic definitions and reserved keywords.  No methods are defined in the provided code snippet; it serves solely as a container for mnemonic data.


### 2.1. Class Attributes <a name="class-attributes"></a>

The class defines several key attributes:

| Attribute Name             | Data Type | Description                                                                        |
|-----------------------------|------------|------------------------------------------------------------------------------------|
| `HALT_COMMAND`             | `str`      | Represents the mnemonic for the halt instruction. Used for both mnemonic lookup and in `INDEPENDENT_MNEMONICS` |
| `JUMP_LABEL`               | `str`      | Represents a reserved keyword used for jump labels in assembly code.                |


### 2.2. `DEFAULT_MNEMONIC` Dictionary <a name="default_mnemonic-dictionary"></a>

This dictionary is the core of the library. It maps mnemonic instruction names (keys) to their corresponding numerical opcode values (values).  The opcodes are represented as integers.

| Mnemonic | Opcode | Description                               |
|----------|---------|-------------------------------------------|
| Data      | 0       | Data operation                          |
| Read      | 10      | Read operation                           |
| Write     | 11      | Write operation                          |
| WriteA    | 12      | Write operation (special addressing mode) |
| ReadI     | 13      | Read operation (indirect addressing)     |
| Load      | 20      | Load operation                           |
| Store     | 21      | Store operation                          |
| LoadI     | 22      | Load operation (indirect addressing)     |
| Add       | 30      | Addition operation                       |
| Sub       | 31      | Subtraction operation                    |
| Div       | 32      | Division operation                      |
| Mod       | 33      | Modulo operation                        |
| Mul       | 34      | Multiplication operation                 |
| AddI      | 35      | Addition (indirect addressing)          |
| SubI      | 36      | Subtraction (indirect addressing)       |
| DivI      | 37      | Division (indirect addressing)          |
| ModI      | 38      | Modulo (indirect addressing)           |
| MulI      | 39      | Multiplication (indirect addressing)     |
| JMP       | 40      | Jump operation                          |
| JL        | 41      | Jump if less than                       |
| JZ        | 42      | Jump if zero                            |
| Halt      | 43      | Halt operation                          |
| clr       | 50      | Clear operation                         |


### 2.3. `INDEPENDENT_MNEMONICS` List <a name="independent_mnemonics-list"></a>

This list specifies mnemonics that operate independently and don't require additional operands or parameters beyond the opcode itself. Note that this list includes the `HALT_COMMAND` to explicitly indicate that the halt instruction is independent.

*   WriteA
*   ReadI
*   Halt


### 2.4. `RESERVED_KEYWORDS` List <a name="reserved_keywords-list"></a>

This list contains keywords that are reserved and cannot be used as mnemonic instruction names.

*   Section (JUMP_LABEL)


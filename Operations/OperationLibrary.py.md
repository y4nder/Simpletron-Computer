# OperationLibrary Class Documentation

[Linked Table of Contents](#table-of-contents)

## Table of Contents

<a name="table-of-contents"></a>

* [1. Overview](#overview)
* [2. Class `OperationLibrary`](#class-operationlibrary)
    * [2.1. `OPERATION_CODES_DEFAULT` Dictionary](#operation-codes-default-dictionary)


## 1. Overview

This document provides internal code documentation for the `OperationLibrary` class.  This class serves as a central registry for operations, mapping integer operation codes to their corresponding functions.  This design promotes code organization, maintainability, and extensibility.


## 2. Class `OperationLibrary`

The `OperationLibrary` class is designed to manage a dictionary mapping operation codes (integers) to functions defined in the `Operations` module. This allows for a flexible and easily expandable system for handling various operations.

### 2.1. `OPERATION_CODES_DEFAULT` Dictionary

The `OPERATION_CODES_DEFAULT` dictionary is the core of the `OperationLibrary` class.  It's a dictionary where:

* **Keys:** are integers representing operation codes.  These codes serve as identifiers for specific operations.
* **Values:** are callable functions (specifically, functions from the `op` module imported as `operations`). Each function corresponds to the operation indicated by its associated key.

The dictionary is initialized with the following key-value pairs:

| Operation Code | Function         | Description                                   |
|-----------------|-----------------|-----------------------------------------------|
| 10              | `op.read`       | Reads input.                                |
| 11              | `op.write`      | Writes output.                               |
| 12              | `op.write_acc`   | Writes the accumulator value.                |
| 13              | `op.readI`      | Reads immediate value.                         |
| 20              | `op.loadM`      | Loads value from memory.                     |
| 21              | `op.store`      | Stores value into memory.                     |
| 22              | `op.loadI`      | Loads immediate value.                         |
| 30              | `op.addM`       | Adds memory value to accumulator.            |
| 31              | `op.subM`       | Subtracts memory value from accumulator.       |
| 32              | `op.divM`       | Divides accumulator by memory value.          |
| 33              | `op.modM`       | Computes modulo of accumulator and memory value.|
| 34              | `op.mulM`       | Multiplies accumulator by memory value.       |
| 35              | `op.addI`       | Adds immediate value to accumulator.          |
| 36              | `op.subI`       | Subtracts immediate value from accumulator.     |
| 37              | `op.divI`       | Divides accumulator by immediate value.       |
| 38              | `op.modI`       | Computes modulo of accumulator and immediate value.|
| 39              | `op.mulI`       | Multiplies accumulator by immediate value.     |
| 40              | `op.jump`       | Unconditional jump.                          |
| 41              | `op.jump_if_negative` | Conditional jump if accumulator is negative. |
| 42              | `op.jump_if_zero`   | Conditional jump if accumulator is zero.     |
| 43              | `op.halt`       | Halts execution.                             |


This structure allows for easy lookup of operation functions based on their integer codes.  Adding new operations only requires adding a new key-value pair to the `OPERATION_CODES_DEFAULT` dictionary.  The use of a dictionary provides efficient O(1) lookup time on average.

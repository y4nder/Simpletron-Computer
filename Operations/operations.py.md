# Internal Code Documentation

## Table of Contents

* [1. Introduction](#1-introduction)
* [2. Function Descriptions](#2-function-descriptions)
    * [2.1 `read(controller, address, useDebug)`](#21-readcontroller-address-usedebug)
    * [2.2 `write(controller, address, useDebug)`](#22-writecontroller-address-usedebug)
    * [2.3 `write_acc(controller, _, useDebug)`](#23-write_accontroller---usedebug)
    * [2.4 `readI(controller, _, useDebug)`](#24-readicontroller---usedebug)
    * [2.5 `loadM(controller, address, useDebug)`](#25-loadmcontroller-address-usedebug)
    * [2.6 `store(controller, address, useDebug)`](#26-storecontroller-address-usedebug)
    * [2.7 `loadI(controller, operand, useDebug)`](#27-loadicontroller-operand-usedebug)
    * [2.8 `addM(controller, address, useDebug)`](#28-addmcontroller-address-usedebug)
    * [2.9 `subM(controller, address, useDebug)`](#29-submcontroller-address-usedebug)
    * [2.10 `divM(controller, address, useDebug)`](#210-divmcontroller-address-usedebug)
    * [2.11 `modM(controller, address, useDebug)`](#211-modmcontroller-address-usedebug)
    * [2.12 `mulM(controller, address, useDebug)`](#212-mulmcontroller-address-usedebug)
    * [2.13 `addI(controller, operand, useDebug)`](#213-addicontroller-operand-usedebug)
    * [2.14 `subI(controller, operand, useDebug)`](#214-subicontroller-operand-usedebug)
    * [2.15 `modI(controller, operand, useDebug)`](#215-modicontroller-operand-usedebug)
    * [2.16 `divI(controller, operand, useDebug)`](#216-divicontroller-operand-usedebug)
    * [2.17 `mulI(controller, operand, useDebug)`](#217-mulicontroller-operand-usedebug)
    * [2.18 `jump(controller, address, useDebug)`](#218-jumpcontroller-address-usedebug)
    * [2.19 `jump_if_negative(controller, address, useDebug)`](#219-jump_if_negativecontroller-address-usedebug)
    * [2.20 `jump_if_zero(controller, address, useDebug)`](#220-jump_if_zerocontroller-address-usedebug)
    * [2.21 `halt(controller, _, useDebug)`](#221-haltcontroller---usedebug)


<a name="1-introduction"></a>
## 1. Introduction

This document provides internal code documentation for a set of functions that interact with a simulated computer's memory and processor.  The functions are designed to perform various operations, including reading from and writing to memory, arithmetic operations on the accumulator, and control flow operations like jumps.  The `Controller` class (from `ControllerFiles.Controller`) is assumed to manage the memory and processor components.  The `useDebug` parameter provides optional debug output.


<a name="2-function-descriptions"></a>
## 2. Function Descriptions

<a name="21-readcontroller-address-usedebug"></a>
### 2.1 `read(controller: Controller, address: int, useDebug: bool = False)`

Reads integer input from the user and stores it into the specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) where the value will be stored.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Prompts the user to enter a number using `input()`.
    2. Converts the input to an integer using `int()`.
    3. Stores the integer value in memory using `controller.getMemory().store_data(address, value)`.
    4. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="22-writecontroller-address-usedebug"></a>
### 2.2 `write(controller: Controller, address, useDebug: bool = False)`

Writes the content of a specified memory address to the console output.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the data from the specified memory address using `controller.getMemory().read_data(address)`.
    2. Prints the address and its value to the console.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="23-write_accontroller---usedebug"></a>
### 2.3 `write_acc(controller: Controller, _, useDebug: bool = False)`

Writes the value of the accumulator to the console.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `_`: A placeholder parameter (not used).
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from the accumulator using `controller.getProcessor().accumulator`.
    2. Prints the accumulator's value to the console.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="24-readicontroller---usedebug"></a>
### 2.4 `readI(controller: Controller, _, useDebug: bool = False)`

Reads integer input from the user and stores it into the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `_`: A placeholder parameter (not used).
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Prompts the user for a number via `input()`.
    2. Converts the input to an integer using `int()`.
    3. Assigns the value to the accumulator: `controller.getProcessor().accumulator = value`.
    4. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="25-loadmcontroller-address-usedebug"></a>
### 2.5 `loadM(controller: Controller, address, useDebug: bool = False)`

Loads the value from a specified memory address into the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads data from memory using `controller.getMemory().read_data(address)`.
    2. Assigns the value to the accumulator: `controller.getProcessor().accumulator = value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="26-storecontroller-address-usedebug"></a>
### 2.6 `store(controller: Controller, address, useDebug: bool = False)`

Stores the accumulator's value into a specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to write to.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the accumulator's value using `controller.getProcessor().accumulator`.
    2. Stores the value in memory using `controller.getMemory().store_data(address, value)`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="27-loadicontroller-operand-usedebug"></a>
### 2.7 `loadI(controller: Controller, operand: int, useDebug: bool = False)`

Loads an immediate integer value into the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) to load.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Assigns the operand to the accumulator: `controller.getProcessor().accumulator = operand`.
    2. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="28-addmcontroller-address-usedebug"></a>
### 2.8 `addM(controller: Controller, address, useDebug: bool = False)`

Adds the value from a specified memory address to the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from memory using `controller.getMemory().read_data(address)`.
    2. Adds the value to the accumulator: `controller.getProcessor().accumulator += value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="29-submcontroller-address-usedebug"></a>
### 2.9 `subM(controller: Controller, address, useDebug: bool = False)`

Subtracts the value from a specified memory address from the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from memory using `controller.getMemory().read_data(address)`.
    2. Subtracts the value from the accumulator: `controller.getProcessor().accumulator -= value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="210-divmcontroller-address-usedebug"></a>
### 2.10 `divM(controller: Controller, address, useDebug: bool = False)`

Divides the accumulator by the value from a specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from memory using `controller.getMemory().read_data(address)`.
    2. Divides the accumulator by the value: `controller.getProcessor().accumulator /= value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="211-modmcontroller-address-usedebug"></a>
### 2.11 `modM(controller: Controller, address, useDebug: bool = False)`

Performs a modulo operation on the accumulator using the value from a specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from memory using `controller.getMemory().read_data(address)`.
    2. Performs the modulo operation: `controller.getProcessor().accumulator %= value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="212-mulmcontroller-address-usedebug"></a>
### 2.12 `mulM(controller: Controller, address, useDebug: bool = False)`

Multiplies the accumulator by the value from a specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to read from.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Reads the value from memory using `controller.getMemory().read_data(address)`.
    2. Multiplies the accumulator by the value: `controller.getProcessor().accumulator *= value`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="213-addicontroller-operand-usedebug"></a>
### 2.13 `addI(controller: Controller, operand: int, useDebug: bool = False)`

Adds an immediate integer value to the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) to add.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Adds the operand to the accumulator: `controller.getProcessor().accumulator += operand`.
    2. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="214-subicontroller-operand-usedebug"></a>
### 2.14 `subI(controller: Controller, operand: int, useDebug: bool = False)`

Subtracts an immediate integer value from the accumulator.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) to subtract.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Subtracts the operand from the accumulator: `controller.getProcessor().accumulator -= operand`.
    2. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="215-modicontroller-operand-usedebug"></a>
### 2.15 `modI(controller: Controller, operand: int, useDebug: bool = False)`

Performs a modulo operation on the accumulator using an immediate integer value.  Raises a `ZeroDivisionError` if the operand is zero.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) for the modulo operation.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Checks if the operand is zero. If so, raises a `ZeroDivisionError`.
    2. Performs the modulo operation: `controller.getProcessor().accumulator %= operand`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="216-divicontroller-operand-usedebug"></a>
### 2.16 `divI(controller: Controller, operand: int, useDebug: bool = False)`

Divides the accumulator by an immediate integer value. Raises a `ZeroDivisionError` if the operand is zero.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) to divide by.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Checks if the operand is zero. If so, raises a `ZeroDivisionError`.
    2. Performs integer division: `controller.getProcessor().accumulator //= operand`.
    3. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="217-mulicontroller-operand-usedebug"></a>
### 2.17 `mulI(controller: Controller, operand: int, useDebug: bool = False)`

Multiplies the accumulator by an immediate integer value.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `operand`: The immediate value (integer) to multiply by.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Multiplies the accumulator by the operand: `controller.getProcessor().accumulator *= operand`.
    2. Increments the program counter using `controller.getProcessor().incrementProgramCounter()`.


<a name="218-jumpcontroller-address-usedebug"></a>
### 2.18 `jump(controller: Controller, address, useDebug: bool = False)`

Unconditionally jumps to a specified memory address.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to jump to.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Sets the program counter to the specified address: `controller.getProcessor().programCounter = address`.


<a name="219-jump_if_negativecontroller-address-usedebug"></a>
### 2.19 `jump_if_negative(controller: Controller, address, useDebug: bool = False)`

Jumps to a specified memory address if the accumulator is less than zero.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to jump to.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Checks if the accumulator is less than zero.
    2. If true, sets the program counter to the specified address: `controller.getProcessor().programCounter = address`.
    3. If false, increments the program counter: `controller.getProcessor().incrementProgramCounter()`.


<a name="220-jump_if_zerocontroller-address-usedebug"></a>
### 2.20 `jump_if_zero(controller: Controller, address, useDebug: bool = False)`

Jumps to a specified memory address if the accumulator is zero.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `address`: The memory address (integer) to jump to.
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Checks if the accumulator is zero.
    2. If true, sets the program counter to the specified address: `controller.getProcessor().programCounter = address`.
    3. If false, increments the program counter: `controller.getProcessor().incrementProgramCounter()`.


<a name="221-haltcontroller---usedebug"></a>
### 2.21 `halt(controller: Controller, _, useDebug: bool = False)`

Halts the program execution and displays the processor and memory dumps.

* **Parameters:**
    * `controller`: An instance of the `Controller` class.
    * `_`: A placeholder parameter (not used).
    * `useDebug`: A boolean flag to enable debug output (default: `False`).
* **Algorithm:**
    1. Prints a newline character.
    2. Calls the `dump()` methods for the processor and memory to display their contents.
    3. Terminates the program using `exit()`.


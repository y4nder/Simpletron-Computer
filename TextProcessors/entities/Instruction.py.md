# Internal Code Documentation: Instruction Class

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Introduction](#1-introduction)
* [2. Class `Instruction`](#2-class-instruction)
    * [2.1 Constructor (`__init__`) ](#21-constructor-__init__)
    * [2.2 Properties (`address`, `data`)](#22-properties-address-data)
    * [2.3 String Representation (`__str__`)](#23-string-representation-__str__)
    * [2.4 `decode()` Method](#24-decode-method)
    * [2.5 `encode()` Method](#25-encode-method)


## 1. Introduction

This document details the implementation of the `Instruction` class,  designed to represent and manipulate instruction data.  The class encapsulates an instruction's address and data, providing methods for encoding and decoding the data.


## 2. Class `Instruction`

The `Instruction` class is defined to represent a single instruction. It stores the instruction's memory address and its data as a string.  The data string is assumed to contain an integer encoding operation and address information.

### 2.1 Constructor (`__init__`)

```python
def __init__(self, address:int, data:str):
    self.__address = address
    self.__data = data
```

The constructor initializes an `Instruction` object.

| Parameter | Type | Description |
|---|---|---|
| `address` | `int` | The memory address of the instruction. |
| `data` | `str` | The instruction data, represented as a string.  This string is expected to be an integer. |


The address and data are stored as private attributes (`self.__address`, `self.__data`) to enforce encapsulation.

### 2.2 Properties (`address`, `data`)

```python
@property
def address(self) -> int:
    return self.__address

@property
def data(self) -> str:
    return self.__data
```

These properties provide controlled access to the instruction's address and data, ensuring data integrity.  They return the address and data as integers and strings, respectively.

### 2.3 String Representation (`__str__`)

```python
def __str__(self) -> str:
    return f"address: {self.__address}  opcode: {self.__data}"
```

This method defines how an `Instruction` object is represented as a string. It returns a formatted string showing the address and data.

### 2.4 `decode()` Method

```python
def decode(self):
    data = int(self.data)
    operation_code = data // 100
    address = data % 100
    return operation_code, address
```

The `decode()` method extracts the operation code and address from the instruction's data.  It assumes that the data is an integer where the operation code is represented by the hundreds place and above, and the address is represented by the remainder after dividing by 100.


**Algorithm:**

1. The data string is converted to an integer.
2. Integer division (`//`) by 100 is used to extract the operation code (e.g., if data is 123, operation code will be 1).
3. The modulo operator (`%`) with 100 is used to extract the address (e.g., if data is 123, address will be 23).
4. The operation code and address are returned as a tuple.

### 2.5 `encode()` Method

```python
def encode(data: str, address: int):
    return Instruction(address, data)
```

The `encode()` method creates a new `Instruction` object from given data and address.  This method acts as a factory function for creating `Instruction` objects.  Note this is a static method and not bound to an instance of the class.

| Parameter | Type | Description |
|---|---|---|
| `data` | `str` | The instruction data (as a string). |
| `address` | `int` | The instruction address. |

The function simply creates and returns a new `Instruction` object using the provided parameters.  No encoding algorithm is implemented within this `encode` method; it assumes the data is already correctly formatted.

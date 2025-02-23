# Opcode Class Documentation

[Linked Table of Contents](#table-of-contents)

## Table of Contents <a name="table-of-contents"></a>

* [1. Class Overview](#class-overview)
* [2. `__new__` Method](#new-method)


## 1. Class Overview <a name="class-overview"></a>

The `Opcode` class extends the built-in `str` class to represent an opcode as a string.  It combines a mnemonic code (from the `Mnemonic` class) and numerical data into a single string representation.  This class ensures consistent formatting of opcodes.


## 2. `__new__` Method <a name="new-method"></a>

The `__new__` method is overridden to construct `Opcode` objects. This is necessary because we are inheriting from `str`, and we need to customize the object creation process.

| Parameter      | Type             | Description                                                              |
|-----------------|-------------------|--------------------------------------------------------------------------|
| `mnemonic`     | `Mnemonic`       | An instance of the `Mnemonic` class, providing the mnemonic code.       |
| `data`          | `int`             | An integer representing the numerical data associated with the opcode. |


**Algorithm:**

1. **Retrieve Mnemonic Code:** The mnemonic code is obtained by calling the `RetrieveCode()` method of the provided `Mnemonic` object. This method (not shown in the provided code snippet) presumably returns a string representation of the mnemonic.  The result is converted to a string using `str()`.

2. **Format Data:** The integer `data` is formatted using the `zfill(2)` method. This ensures that the data is always represented by two digits, padding with leading zeros if necessary. For example, the integer `5` becomes `"05"`. The result is converted to a string using `str()`.

3. **Concatenate and Create Object:** The mnemonic code string and the formatted data string are concatenated. This combined string is then used to create a new `Opcode` object using `super().__new__(cls, combinedString)`. The `super()` call invokes the `__new__` method of the parent class (`str`), creating a string object with the combined value.

4. **Return Object:** The newly created `Opcode` object is returned.


**Example:**

If `mnemonic.RetrieveCode()` returns `"ADD"` and `data` is `10`, the resulting `Opcode` object will be `"ADD10"`. If `data` was `5`, the resulting `Opcode` object would be `"ADD05"`.

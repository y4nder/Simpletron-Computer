# Internal Code Documentation: Mnemonic Class

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Class Overview](#1-class-overview)
* [2. `__new__` Method](#2-__new__-method)
* [3. `IsJumpStatement` Method](#3-isjumpstatement-method)
* [4. `IsIndependent` Method](#4-isindependent-method)
* [5. `IsJumpMarker` Method](#5-isjumpmarker-method)
* [6. `JumpMarkerExistsIn` Method](#6-jumpmarkerexistsin-method)
* [7. `ExtractFrom` Method](#7-extractfrom-method)
* [8. `RetrieveCode` Method](#8-retrievecode-method)


## 1. Class Overview

The `Mnemonic` class extends the built-in `str` class to represent assembly mnemonics. It leverages the `MnemonicLibrary` class (presumably defined elsewhere) to validate mnemonics and retrieve associated opcodes.  The class provides methods for checking mnemonic properties such as jump statements, independence, and jump markers.


## 2. `__new__` Method

```python
    def __new__(cls, value, address):
        if not MnemonicLibrary.DEFAULT_MNEMONIC.get(value) and value not in MnemonicLibrary.RESERVED_KEYWORDS:
            raise ValueError(f"Unknown mnemonic: '{value}' at address: {address}")
        obj = super().__new__(cls, value)
        return obj
```

This method overrides the standard `__new__` constructor for the `str` class. It performs input validation before creating a new `Mnemonic` object.

*   It checks if the input `value` (the mnemonic string) exists in `MnemonicLibrary.DEFAULT_MNEMONIC` (a dictionary mapping mnemonics to opcodes) or  `MnemonicLibrary.RESERVED_KEYWORDS` (a set of reserved words).
*   If the mnemonic is unknown and not a reserved keyword, a `ValueError` is raised, providing the invalid mnemonic and its address for debugging purposes.
*   Otherwise, a new `str` object is created using `super().__new__(cls, value)` and returned, ensuring the object inherits `str` functionalities.


## 3. `IsJumpStatement` Method

```python
    def IsJumpStatement(self):
        return self.upper().startswith("J")
```

This method checks if the mnemonic represents a jump statement. It converts the mnemonic to uppercase using `.upper()` and checks if it starts with the letter "J".  This is a simple heuristic; a more robust approach might involve a lookup table of jump instructions.


## 4. `IsIndependent` Method

```python
    def IsIndependent(self, address, length):
        if self in MnemonicLibrary.INDEPENDENT_MNEMONICS and length == 1:
            return True
        else:
            if(length == 1):
                raise ValueError(f"invalid independent mnemonic usage {self} at address {address} with length {length}")
            else:
                return False
```

This method determines whether a mnemonic is considered "independent".  Independence is defined based on two criteria:

1.  The mnemonic must be present in the `MnemonicLibrary.INDEPENDENT_MNEMONICS` set.
2.  The `length` parameter (presumably representing the number of bytes of the instruction) must be 1.

If both conditions are met, the method returns `True`. If `length` is 1 but the mnemonic isn't independent, a `ValueError` is raised, indicating an incorrect usage. Otherwise, it returns `False`.


## 5. `IsJumpMarker` Method

```python
    def IsJumpMarker(self):
        return self == MnemonicLibrary.JUMP_LABEL
```

This method simply checks if the mnemonic is equal to the `JUMP_LABEL` defined in `MnemonicLibrary`.


## 6. `JumpMarkerExistsIn` Method

```python
    def JumpMarkerExistsIn(lineCommand:list[str]):
        return MnemonicLibrary.JUMP_LABEL in lineCommand and len(lineCommand) > 2
```

This is a static method that checks if a `JUMP_LABEL` exists within a given `lineCommand` list (presumably representing a line of assembly code). It returns `True` if the label is present and the line contains more than 2 elements (implying more information beyond the label).


## 7. `ExtractFrom` Method

```python
    def ExtractFrom(lineCommand: list[str], address: int):
        return Mnemonic(lineCommand[0], address)
```

This static method extracts a mnemonic from a `lineCommand` list. It assumes the mnemonic is the first element (`lineCommand[0]`) and creates a new `Mnemonic` object using it and the provided `address`.


## 8. `RetrieveCode` Method

```python
    def RetrieveCode(self):
        return MnemonicLibrary.DEFAULT_MNEMONIC[self]
```

This method retrieves the opcode associated with the mnemonic. It accesses the `MnemonicLibrary.DEFAULT_MNEMONIC` dictionary using the mnemonic as the key and returns the corresponding opcode.  It assumes the mnemonic is a valid key in the dictionary;  no error handling is included.

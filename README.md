# Memory Component

This section defines a `Memory` class that manages memory operations using a `MainMemory` instance and a `Validator`. It provides methods to store and read data from memory cells and to visualize the memory state

## Example Usage

```python
memory = Memory()

# Store data in memory
success = memory.store_data(10, "1234")
print(success)  # Expected output: True if the address and data are valid, otherwise False

# Read data from memory
data = memory.read_data(10)
print(data)  # Expected output: "1234" if the address is valid and data is stored, otherwise "Address not found"

# Dump memory state
memory.dump()  # Expected output: Visual representation of the memory state
```

## Methods

### `_findCell`

-   Finds and returns the memory cell for a given address.

### `store_data(address: int, data: str) -> bool`

-   Validates the address and data, then stores the data in the appropriate memory cell.

### `read_data(address: int) -> str`

-   Validates the address and retrieves the data from the appropriate memory cell.

### `dump()`

-   Visualizes the current state of the memory using a CLI tool.

## Fields

### `_memoryInstance`

-   An instance of `MainMemory` that represents the memory structure

### `_validator`

-   An instance of `Validator` used to validate addresses and data

---

# MemoryLoader

The `MemoryLoader` class is responsible for loading instructions from a file into memory. It uses a parser to read and parse the instructions and then stores them in memory.

## Example Usage

```python
from MemoryFiles.MemoryLoader import MemoryLoader
from MemoryFiles.IMemory import IMemory
from TextProcessors.IParser import IParser

class Memory(IMemory):
    def store_data(self, address: int, data: str) -> bool:
        # Implementation here
        return True

    def read_data(self, address: int) -> str:
        # Implementation here
        return "data"

    def dump(self) -> bool:
        # Implementation here
        return True

class Parser(IParser):
    def parse(self, fileAddress: str) -> list[Instruction]:
        # Implementation here
        return [Instruction(0, "data")]

memory = Memory()
parser = Parser()
loader = MemoryLoader(memory, parser)
loader.load("path/to/file")
```

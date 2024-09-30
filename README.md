# Controller Component

### Summary

The `Controller` class orchestrates the interaction between a `Processor` and `IMemory` to execute instructions. It fetches, decodes, and executes instructions in a loop using provided operation codes.

#### Dependencies

<li>IMemory</li>
<li>Processor</li>
<li>OperationLibrary</li>

## Example Usage

```python
from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader
from ProcessorFiles.Processor import Processor
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary

#create instance of processor and memory
processor = Processor()
memory = MemoryFactory.MemorySingleList()

#load memory with sml program
file = "testCodes/Factorial.sml"
parser = ParserFactory.LowLevelParser()
memoryLoader = MemoryLoader(memory, parser)
memoryLoader.load(file)

#define the library
library = OperationLibrary.OPERATION_CODES_DEFAULT

#create controller instace and inject the processor, memory and library
controller = Controller(processor, memory, library)

print("-" * 10)
print("executing file")

#run the program
controller.run()
```

## Methods

-   **`__init__`**: Initializes the Controller with Processor, IMemory, and operation codes.
-   **`getProcessor`**: Returns the Processor instance.
-   **`getMemory`**: Returns the IMemory instance.
-   **`run`**: Main loop to fetch, decode, and execute instructions.
-   **`__fetch_instruction`**: Fetches the next instruction from memory.
-   **`__decodeInstructions`**: Decodes the fetched instruction into operation code and address.
-   **`__execute_instruction`**: Executes the instruction based on the operation code.

## Fields

-   **`__processor`**: Holds the Processor instance.
-   **`__memory`**: Holds the IMemory instance.
-   **`__operationCodes`**: Dictionary mapping operation codes to their corresponding functions.

---

# Processor

## Main functionalities

The main functionalities of the `Processor` class include managing and updating the state of a simulated CPU through properties such as the accumulator, program counter, instruction register, operation code, and operand.

## Methods

-   **`__init__`**: Initializes the Processor with default values for its properties.
-   **`accumulator`**: Getter and setter for the accumulator property.
-   **`programCounter`**: Getter and setter for the program counter property.
-   **`instructionRegister`**: Getter and setter for the instruction register property.
-   **`operationCode`**: Getter and setter for the operation code property.
-   **`operand`**: Getter and setter for the operand property.

## Fields

-   **`__accumulator`**: Stores the value of the accumulator.
-   **`__programCounter`**: Stores the value of the program counter.
-   **`__instructionRegister`**: Stores the current instruction.
-   **`__operationCode`**: Stores the operation code of the current instruction.
-   **`__operand`**: Stores the operand of the current instruction.

---

# Memory Component (di nako ani)

see MemorySingleList Component

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

# MemorySingeList

## Summary

The `MemorySingleList` class implements the `IMemory` interface, providing a memory storage system using a list. It includes methods to store and read data at specific addresses, and to dump the entire memory content.

## Example Usage

```python
memory = MemorySingleList(size=50)
success = memory.store_data(10, "+1234")
data = memory.read_data(10)
memory.dump()
```

## Code Analysis

### Main Functionalities

The main functionalities of the `MemorySingleList` class include:

-   Storing data at a specific address.
-   Reading data from a specific address.
-   Dumping the entire memory content for visualization.

### Methods

-   **`__init__(self, size: int = 100)`**: Initializes the memory list with a default size of 100 and sets up the validator.
-   **`store_data(self, address: int, data: str) -> bool`**: Stores data at the specified address if the address and data are valid.
-   **`read_data(self, address: int) -> str`**: Reads data from the specified address if the address is valid.
-   **`dump(self) -> bool`**: Dumps the entire memory content using the visualizer.

### Fields

-   **`__memory`**: A list representing the memory storage.
-   **`__validator`**: An instance of `MemoryValidatorSingleList` used to validate addresses and instructions.

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

# Memory Component

This repository contains a `Memory` class that provides an abstraction for storing and retrieving data at specific memory addresses, as well as dumping the contents of the memory for debugging purposes. The `Memory` class interacts with a `MainMemory` instance, handling the low-level details of memory management.

## Main Functionalities

-   **Store Data**: Store data at a specific memory address.
-   **Read Data**: Read and return the data from a specified memory address.
-   **Dump Memory**: Dump the entire memory content.

## Example Usage

```python
# Initialize memory
memory = Memory()

# Store data at address 10
success = memory.store_data(10, "1234")
if success:
    print("Data stored successfully.")
else:
    print("Failed to store data.")

# Read data from address 10
data = memory.read_data(10)
print(f"Data at address 10: {data}")

# Dump the entire memory content
memory.dump()
```

## Methods

### `__init__()`

-   Initializes a `Memory` instance by creating an instance of `MainMemory`.

### `store_data(address: int, data: str) -> bool`

-   Stores a string `data` at a specified memory `address`.
-   Returns `True` if the data is successfully stored, otherwise returns `False`.

### `read_data(address: int) -> str`

-   Reads and returns the data stored at the specified memory `address`.

### `dump()`

-   Dumps the entire memory content using the `memorydumper` function.

## Fields

### `_memoryInstance`

-   An instance of `MainMemory` that manages memory rows and cells.

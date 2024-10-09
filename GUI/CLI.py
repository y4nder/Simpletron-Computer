
from MemoryFiles.Memories.MemoryTypes import MasterMemory


def memorydumper(masterMemory: MasterMemory) -> None:
    print("Memory Dump:")
    __memoryDumpHeaderRenderer(masterMemory.getMemoryCellLimit())
    __memoryRowRenderer(masterMemory)

def __memoryDumpHeaderRenderer(memoryCellLimit: int) -> None:
    print("     ", end="")  
    for i in range(memoryCellLimit):
        print(f"{i:>7}", end="")  
    print("")  

def __memoryRowRenderer(masterMemory: MasterMemory) -> None:
    for memoryRow in masterMemory.getMemory():
        print(f"{memoryRow.getMemoryCells()[0].getAddress() // 10:5}0", end="  ")  
        for memoryCell in memoryRow.getMemoryCells():
            print(f"{memoryCell.getData()}", end="  ")  
        print("")  

def singleListMemoryDumper(memory: list, pointer_index: int = None) -> None:
    print("Memory Dump:")
    __newMemoryDumpHeaderRenderer()
    __newMemoryRowRenderer(memory, pointer_index)

def __newMemoryDumpHeaderRenderer() -> None:
    print("     ", end="")  
    for i in range(10):  # Always 10 columns
        print(f"{i:>9}", end="")  
    print("")  

def __newMemoryRowRenderer(memory: list, pointer_index: int = None) -> None:
    for i in range(0, len(memory), 10):  # Process in chunks of 10
        # Mimic address as memory row (multiples of 10)
        print(f"{i // 10:5}0", end="  ")
        for j in range(i, i + 10):
            if j < len(memory):  # Ensure we don’t go out of bounds
                if pointer_index is not None and j == pointer_index:
                    data = f"-> {memory[j]}"  # Add the ">" symbol for the pointed index
                else:
                    data = f"+{memory[j]}"
                print(f"{data:>7}", end="  ")  # Print memory cell data
        print("")  # Newline after each row
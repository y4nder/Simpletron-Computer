from MemoryFiles.MemoryTypes import MasterMemory

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

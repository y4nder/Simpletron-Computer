from MemoryFiles.MemoryTypes import MasterMemory

def memorydumper(masterMemory: MasterMemory) -> None:
    print("Memory Dump:")
    _memoryDumpHeaderRenderer(masterMemory.memoryCellLimit)
    _memoryRowRenderer(masterMemory)

def _memoryDumpHeaderRenderer(memoryCellLimit: int) -> None:
    # Print header with spaces for row number and memory cell headers aligned with cell width
    print("     ", end="")  # 5 spaces to align with row number
    for i in range(memoryCellLimit):
        print(f"{i:>7}", end="")  # Align headers with memory cells (6 characters wide)
    print("")  # Move to the next line after printing headers

def _memoryRowRenderer(masterMemory: MasterMemory) -> None:
    for memoryRow in masterMemory.memory:
        # Print the row number followed by '0' with proper spacing (4 for row number, 1 for 0)
        print(f"{memoryRow.memoryCells[0].getAddress() // 10:5}0", end="  ")  # Row number with 4 spaces width
        for memoryCell in memoryRow.memoryCells:
            # Print each memory cell value with a 6-character width to match headers
            print(f"{memoryCell.getData()}", end="  ")  # Two spaces between cells
        print("")  # Move to the next line after printing each row

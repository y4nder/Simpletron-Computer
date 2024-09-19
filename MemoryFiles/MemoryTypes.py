memoryRowLimit = 10
memoryCellLimit = 10

class MemoryCell(object):
    def __init__(self, address: int):
        self.address = address
        self.data: str = "+0000"
        
    def __str__(self) -> str:
        return self.data
    
    
class MemoryRow(object):
    def __init__(self, rowNumber: int):
        self.rowNumber = rowNumber
        self.memoryCells = [MemoryCell(rowNumber * memoryCellLimit + x) for x in range(memoryCellLimit)]
        

class MasterMemory(object):
    def __init__(self):
        self.memory = [MemoryRow(x) for x in range(0, memoryRowLimit)]
        self.memoryRowLimit = memoryRowLimit
        self.memoryCellLimit = memoryCellLimit
        
    def getMemory(self) -> list[MemoryRow]:
        return self.memory
memoryRowLimit = 10
memoryCellLimit = 10

class MemoryCell(object):
    def __init__(self, address: int):
        self._address = address
        self._data: str = "+0000"
        
    def getAddress(self) -> int:
        return self._address
                
    def __str__(self) -> str:
        return self._data
    
    def setData(self, data: str):
        self._data = "+" + data
        
    def getData(self):
        return self._data
    
    
class MemoryRow(object):
    def __init__(self, row_number: int):
        self.rowNumber = row_number
        self.memoryCells = [MemoryCell(row_number * memoryCellLimit + x) for x in range(memoryCellLimit)]
        

class MasterMemory(object):
    def __init__(self):
        self._memory = [MemoryRow(x) for x in range(0, memoryRowLimit)]
        self._memoryRowLimit = memoryRowLimit
        self._memoryCellLimit = memoryCellLimit
        
    def getMemoryRowLimit(self) -> int:
        return self._memoryRowLimit
    
    def getMemoryCellLimit(self) -> int:
        return self._memoryCellLimit
        
    def getMemory(self) -> list[MemoryRow]:
        return self._memory
memoryRowLimit = 10
memoryCellLimit = 10

class MemoryCell(object):
    def __init__(self, address: int):
        self._address = address
        self._data: str = "+0000"
        
    def getAddress(self) -> int:
        return self._address
        
    def setData(self, data: str) -> None:
        self._data = data
        
    def getData(self) -> str:
        return self._data
        
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
        self.memory = [MemoryRow(x) for x in range(0, memoryRowLimit)]
        self.memoryRowLimit = memoryRowLimit
        self.memoryCellLimit = memoryCellLimit
        
    def getMemory(self) -> list[MemoryRow]:
        return self.memory
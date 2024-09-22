memoryRowLimit = 10
memoryCellLimit = 10

class MemoryCell(object):
    def __init__(self, address: int):
        self.__address = address
        self.__data: str = "+0000"
        
    def getAddress(self) -> int:
        return self.__address
                
    def __str__(self) -> str:
        return self.__data
    
    def setData(self, data: str):
        self.__data = "+" + data
        
    def getData(self):
        return self.__data
    
    
class MemoryRow(object):
    def __init__(self, row_number: int):
        self.__rowNumber = row_number
        self.__memoryCells = [MemoryCell(row_number * memoryCellLimit + x) for x in range(memoryCellLimit)]
    
    def getRowNumber(self) -> int:
        return self.__rowNumber
    
    def getMemoryCells(self) -> list[MemoryCell]:
        return self.__memoryCells

class MasterMemory(object):
    def __init__(self):
        self.__memory = [MemoryRow(x) for x in range(0, memoryRowLimit)]
        self.__memoryRowLimit = memoryRowLimit
        self.__memoryCellLimit = memoryCellLimit
        
    def getMemoryRowLimit(self) -> int:
        return self.__memoryRowLimit
    
    def getMemoryCellLimit(self) -> int:
        return self.__memoryCellLimit
        
    def getMemory(self) -> list[MemoryRow]:
        return self.__memory
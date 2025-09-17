"""
    LUBGUBAN, Leander Lorenz B. BSCS3
	Simpletron Memory
"""

from MemoryFiles.Memories.MemoryTypes import MasterMemory as MainMemory
from MemoryFiles.Validator.MemoryValidator import MemoryValidator as Validator
from GUI.CLI import memorydumper as visualizeMemory_CLI
from Types.IMemory import IMemory

class Memory(IMemory):
    def __init__(self, memoryRows: int = 10, memoryCells: int = 10):
        self.__memoryInstance = MainMemory(memoryCells=memoryCells, memoryRows=memoryRows)
        self.__validator = Validator(self.__memoryInstance)
        
    # Helper Methods
    
    def __findCell(self, address: int):
        for mRow in self.__memoryInstance.getMemory():
            if self.__currentRowMatchesAddress(str(address), mRow):
                index_of_address = self.__findIndexOfAddress(str(address), mRow)
                if index_of_address != -1:
                    return mRow.getMemoryCells()[index_of_address]
                else:
                    return None
        return None

    def __findIndexOfAddress(self, address: str, mRow):
        return next((i for i, cell in enumerate(mRow.getMemoryCells()) if cell.getAddress() == address), -1)

    def __currentRowMatchesAddress(self, address: str, mRow) -> bool:
        return mRow.getMemoryCells()[0].getAddress() <= address < mRow.getMemoryCells()[-1].getAddress() + 1
    
    def __addressValidator(self, address: str) -> bool:
        return self.__validator.validateAddress(address)
    
    def __dataValidator(self, data: int) -> bool:
        return self.__validator.validateData(str(data))
    
    # Exposed APIs
    
    def store_data(self, address: int, data: str) -> bool:
        validAddress = self.__addressValidator(str(address))
        if not validAddress:
            return False
        
        validData = self.__dataValidator(int(data))
        if not validData:
            return False
        
        memoryCell = self.__findCell(address)
        if not memoryCell:
            print("Address not found")
            return False
        else:
            memoryCell.setData(data)
            return True

    def read_data(self, address: int) -> str:
        validAddress = self.__addressValidator(str(address))
        if not validAddress:
            return ""
        
        memoryCell = self.__findCell(address)
        if not memoryCell:
            return ""
        else:
            return str(memoryCell.getData())
        
    def dump(self)->bool:
        validMemoryStatus =  self.__validator.validateMemoryInstance()
        
        if not validMemoryStatus:
            return False
        
        visualizeMemory_CLI(self.__memoryInstance)
        return True
        
    
 
 
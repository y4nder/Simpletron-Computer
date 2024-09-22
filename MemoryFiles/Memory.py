"""
    LUBGUBAN, Leander Lorenz B. BSCS3
	Simpletron Memory
"""
from MemoryFiles.MemoryTypes import MasterMemory as MainMemory
from MemoryFiles.MemoryValidator import MemoryValidator as Validator
from GUI.CLI import memorydumper as visualizeMemory_CLI

class Memory(object):
    def __init__(self):
        self.__memoryInstance = MainMemory()
        self.__validator = Validator(self.__memoryInstance)
        
    # Helper Methods
    
    def __findCell(self, address: int):
        for mRow in self.__memoryInstance.getMemory():
            if self.__currentRowMatchesAddress(address, mRow):
                index_of_address = self.__findIndexOfAddress(address, mRow)
                if index_of_address != -1:
                    return mRow.getMemoryCells()[index_of_address]
                else:
                    return None
        return None

    def __findIndexOfAddress(self, address, mRow):
        return next((i for i, cell in enumerate(mRow.getMemoryCells()) if cell.getAddress() == address), -1)

    def __currentRowMatchesAddress(self, address, mRow) -> bool:
        return mRow.getMemoryCells()[0].getAddress() <= address < mRow.getMemoryCells()[-1].getAddress() + 1
    
    def __addressValidator(self, address: str) -> bool:
        return self.__validator.validateAddress(address)
    
    def __dataValidator(self, data: int) -> bool:
        return self.__validator.validateData(data)
    
    # Exposed APIs
    
    def store_data(self, address: int, data: str) -> bool:
        validAddress = self.__addressValidator(address)
        if not validAddress:
            return False
        
        validData = self.__dataValidator(data)
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
        validAddress = self.__addressValidator(address)
        if not validAddress:
            return False
        
        memoryCell = self.__findCell(address)
        if not memoryCell:
            return ""
        else:
            return memoryCell.getData()
        
    def dump(self)->bool:
        validMemoryStatus =  self.__validator.validateMemoryInstance()
        
        if not validMemoryStatus:
            return False
        
        visualizeMemory_CLI(self.__memoryInstance)
        return True
        
     
 
 
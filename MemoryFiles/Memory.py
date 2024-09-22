"""
    LUBGUBAN, Leander Lorenz B. BSCS3
	Simpletron Memory
"""
from MemoryFiles.MemoryTypes import MasterMemory as MainMemory
from MemoryFiles.MemoryValidator import MemoryValidator as Validator
from GUI.CLI import memorydumper as visualizeMemory_CLI

class Memory(object):
    def __init__(self):
        self._memoryInstance = MainMemory()
        self._validator = Validator(self._memoryInstance)
        
    def _findCell(self, address: int):
        for mRow in self._memoryInstance.getMemory():
            if mRow.memoryCells[0]._address <= address < mRow.memoryCells[-1]._address + 1:
                index_of_address = next((i for i, cell in enumerate(mRow.memoryCells) if cell._address == address), -1)
                if index_of_address != -1:
                    return mRow.memoryCells[index_of_address]
                    
            
    def store_data(self, address: int, data: str) -> bool:
        validAddress = self._validator.validateAddress(address)
        if not validAddress:
            return False
        
        validData = self._validator.validateData(data)
        if not validData:
            return False
        
        memoryCell = self._findCell(address)
        if not memoryCell:
            print("Address not found")
            return False
        else:
            memoryCell.setData(data)
            return True

            
    def read_data(self, address: int) -> str:
        validAddress = self._validator.validateAddress(address)
        if not validAddress:
            return False
        
        memoryCell = self._findCell(address)
        if not memoryCell:
            return "Address not found"
        else:
            return memoryCell.getData()
        

    def dump(self)->bool:
        visualizeMemory_CLI(self._memoryInstance)
        return True
        
     
 
 
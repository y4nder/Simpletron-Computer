'''
    LUBGUBAN, Leander Lorenz B. BSCS3
	Simpletron Memory
'''
from MemoryFiles.MemoryTypes import MasterMemory as MainMemory
from GUI.CLI import *

class Memory(object):
    def __init__(self):
        self._memoryInstance = MainMemory()
        
    def store_data(self, address: int, data: str) -> bool:
        indexOfAddress = -1

        for mRow in self._memoryInstance.getMemory():
            if mRow.memoryCells[0].address <= address < mRow.memoryCells[-1].address + 1:
                indexOfAddress = next((i for i, cell in enumerate(mRow.memoryCells) if cell.address == address), -1)
                if indexOfAddress != -1:
                    mRow.memoryCells[indexOfAddress].data = "+" + data  
                    print(f"storing value {data} to memory address: {mRow.rowNumber}{mRow.memoryCells[indexOfAddress].address}")
                    break

        if indexOfAddress == -1:
            print("Address not found")
            return False
        else:
            print("store success!")
            return True   
            
    def read_data(self, address: int) -> str:
        for mRow in self._memoryInstance.getMemory():
            if mRow.memoryCells[0].address <= address < mRow.memoryCells[-1].address + 1:
                indexOfAddress = next((i for i, cell in enumerate(mRow.memoryCells) if cell.address == address), -1)
                if indexOfAddress != -1:
                    return mRow.memoryCells[indexOfAddress].data

        return "Address not found"

    
    
    def dump(self)->bool:
        memorydumper(self._memoryInstance)
        
     
 
 
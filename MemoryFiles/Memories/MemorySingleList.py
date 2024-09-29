from MemoryFiles.Interface.IMemory import IMemory
from GUI.CLI import singleListMemoryDumper as visualizer
from MemoryFiles.Validator.MemomryValidatorSingleList import MemoryValidatorSingleList

class MemorySingleList(IMemory):
    def __init__(self, size: int = 100):
        self.__memory = ["+0000" for _ in range(size)]
        self.__validator = MemoryValidatorSingleList(self.__memory)
    
    def store_data(self, address: int, data: str) -> bool:
        if not self.__validator.validateAddress(address):
            return False
        
        if not self.__validator.validateInstruction(data):
            return False
        
        self.__memory[address] = data
        return True
    
    def read_data(self, address: int) -> str:
        if not self.__validator.validateAddress(address):
            return ""
        else:
            return self.__memory[address]
    
    def dump(self) -> bool:
        visualizer(self.__memory)
        
        
    

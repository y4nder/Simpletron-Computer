from MemoryFiles.Interface.IMemory import IMemory
from MemoryFiles.Interface.IMemoryValidator import IMemoryValidator


class MemoryValidatorSingleList(IMemoryValidator):
    def __init__(self, memory: IMemory):
        self.__memory = memory
    
    def validateAddress(self, address: int) -> bool:
        try:
            cell = self.__memory[address]
            return True
        except IndexError:
            print("invalid address")
            return False
    
    def validateInstruction(self, instruction: str) -> bool:
        # if(len(instruction) != 4):
        #     print("invalid instruction")
        #     return False
        return True
            
    
from Types import IMemory
from Types.IMemoryValidator import IMemoryValidator


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
        
        # if isinstance(instruction, int):
        #     instruction = str(instruction)
        
        # instruction = instruction.zfill(4)
        
        # if(len(instruction) != 4):
        #     print(f"invalid instruction {instruction}")
        #     print(f"{type(instruction)}")
        #     return False
        return True
            
    
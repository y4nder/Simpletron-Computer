from TextProcessors.entities.Instruction import Instruction
from Types.IMemory import IMemory
from Types.IParser import IParser

class MemoryLoader(object):
    def __init__(self, memory:IMemory, parser:IParser, debug: bool = False):
        self.__parser = parser
        self.__memory = memory
        self.debug = debug
    
    def load(self, fileAddress: str):
        if self.debug:
            print("\nloading instructions to memory\n")
        try:
            parsedInstructions: list[Instruction] = self.__parser.parse(fileAddress)   
        except Exception as e:
            raise e
        
        for parsedInstruction in parsedInstructions:
            if self.debug:
                print(parsedInstruction)
                
            if not isinstance(parsedInstruction, Instruction):
                raise TypeError("incorrect instruction type")            
        
            address: int = parsedInstruction.address
            instruction: str = parsedInstruction.data
            self.__memory.store_data(address, instruction)
from MemoryFiles.Interface.IMemory import IMemory
from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction

class MemoryLoader(object):
    def __init__(self, memory:IMemory, parser:IParser, debug: bool = False):
        self.__parser = parser
        self.__memory = memory
        self.debug = debug
    
    def load(self, fileAddress: str):
        if self.debug:
            print("\nloading instructions to memory\n")
        
        parsedInstructions = self.__parser.parse(fileAddress)   
        for instruction in parsedInstructions:
            if self.debug:
                print(instruction)
                
            if not isinstance(instruction, Instruction):
                raise TypeError("incorrect instruction type")            
        
            address: int = instruction.address
            instruction: str = instruction.data
            self.__memory.store_data(address, instruction)
        
        print("*** Welcome to Simpletron ***")
        print("*** Program Loaded Succesfully")

from MemoryFiles.Interface.IMemory import IMemory
from TextProcessors.IParser import IParser

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
        
            address: int = instruction.getAddress()
            instruction: str = instruction.getData()
            self.__memory.store_data(address, instruction)
        
        if self.debug:
            print("-"*50)
            print("\nload success\n")

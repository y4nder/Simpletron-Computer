from MemoryFiles.Interface.IMemory import IMemory
from TextProcessors.IParser import IParser

class MemoryLoader(object):
    def __init__(self, memory:IMemory, parser:IParser):
        self.__parser = parser
        self.__memory = memory
    
    def load(self, fileAddress: str):
        print("\nloading instructions to memory\n")
        parsedInstructions = self.__parser.parse(fileAddress)   
        for instruction in parsedInstructions:
            print(instruction)
            address: int = instruction.getAddress()
            instruction: str = instruction.getData()
            self.__memory.store_data(address, instruction)
        print("-"*50)
        print("load success\n")
        self.__memory.dump()
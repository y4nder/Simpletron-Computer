from MemoryFiles.IMemory import IMemory
from TextProcessors.IParser import IParser

class MemoryLoader(object):
    def __init__(self, memory: IMemory,parser: IParser):
        self.__parser = parser
        self.__memory = memory
    
    def load(self, fileAddress: str):
        print("\nloading instructions to memory\n")
        parsedData = self.__parser.parse(fileAddress)   
        for data in parsedData:
            print(data)
            address: int = int(data[0])
            instruction: str = data[1]
            self.__memory.store_data(address, instruction)
        print("-"*50)
        print("load success\n")
        self.__memory.dump()
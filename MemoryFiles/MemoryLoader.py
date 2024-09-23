from MemoryFiles.Memory import Memory as MemoryAPI
from TextProcessors.Parser import Parser

class MemoryLoader(object):
    def __init__(self):
        self.__parser = Parser()
    
    def load(self, fileAddress: str, memoryAPI: MemoryAPI):
        print("\nloading instructions to memory\n")
        parsedData = self.__parser.startParse(fileAddress)    
        for data in parsedData:
            print(data)
            address: int = int(data[0])
            instruction: str = data[1]
            memoryAPI.store_data(address, instruction)
        print("-"*50)
        print("load success\n")
        memoryAPI.dump()
from MemoryFiles.Interface.IMemory import IMemory
from ProcessorFiles.Processor import Processor


class Controller(object):
    def __init__(self, processor: Processor, memory: IMemory, operationCodes: dict[int, any]):
        self.__processor = processor
        self.__memory = memory
        self.__operationCodes = operationCodes
        
    def getProcessor(self) -> Processor:
        return self.__processor
    
    def getMemory(self) -> IMemory:
        return self.__memory
    
    def run(self):
        while True:
            instruction = self.__fetch_instruction()
            operation_code, address = self.__decodeInstructions(instruction)
            self.__execute_instruction(operation_code, address)
        
    def __fetch_instruction(self):
        instruction = self.__memory.read_data(self.__processor.programCounter)
        return instruction
        
    def __decodeInstructions(self, instruction: str):
        instruction = int(instruction)
        operation_code = instruction //100
        address = instruction % 100
        return operation_code, address
    
    def __execute_instruction(self, operation_code, address):
        if operation_code in self.__operationCodes:
            self.__operationCodes[operation_code](self, address)
        else:
            raise ValueError(f"Invalid operation code: {operation_code}")





from MemoryFiles.Interface.IMemory import IMemory
from ProcessorFiles.Processor import Processor
from typing import Callable


class Controller(object):
    '''
        The `Controller` class orchestrates the interaction between a `Processor` and `IMemory` to execute instructions. 
        It fetches, decodes, and executes instructions in a loop using provided operation codes.
    '''
    def __init__(self, processor: Processor, memory: IMemory, operationCodes: dict[int, Callable[[], None]], debug: bool = False):
        self.debug = debug
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
            
            if self.debug:
                print("-"*100)
                print(f"Executing {instruction} ...")
            
            operation_code, address = self.__decodeInstructions(instruction)
            self.__update_processor_state(instruction, operation_code, address)
            
            if self.debug:
                print() 
                self.__processor.dump()
                self.__memory.dump(self.__processor.programCounter)
                
            self.__execute_instruction(operation_code, address)
            
            if self.debug:
                input("\nPress any key to continue...")
                
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
            self.__operationCodes[operation_code](self, address, useDebug = self.debug)
        else:
            raise ValueError(f"Invalid operation code: {operation_code}")

    def __update_processor_state(self, instruction, operation_code, address):
        self.__processor.instructionRegister = instruction
        self.__processor.operationCode = operation_code
        self.__processor.operand = address 




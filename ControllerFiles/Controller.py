from ProcessorFiles.Processor import Processor
from typing import Callable
from TextProcessors.entities.Instruction import Instruction
from Types.IController import IController
from Types.IMemory import IMemory




class Controller(IController):
    '''
        The `Controller` class orchestrates the interaction between a `Processor` and `IMemory` to execute instructions. 
        It fetches, decodes, and executes instructions in a loop using provided operation codes.
    '''
    def __init__(self, processor: Processor, memory: IMemory, operationCodes: dict[int, Callable[[], None]], debug: bool = False):
        self.debug = debug
        self.__processor = processor
        self.__memory = memory
        self.__operationCodes = operationCodes
                        
    def get_processor_instance(self) -> Processor:
        return self.__processor
    
    def get_memory_instance(self) -> IMemory:
        return self.__memory
    
    def run(self):         
        print("*** Welcome to Simpletron ***")
        print("*** Program Loaded Succesfully ***\n")   
        while True:
            instruction = self.__fetch_instruction();
            
            if self.debug:
                print("-"*100)
                print(f"Executing {instruction} ...")
            
            self.__processor.update_state(instruction)
            
            if self.debug:
                print() 
                self.__processor.dump()
                self.__memory.dump(self.__processor.programCounter)
                
            self.__execute_instruction(instruction)
            
            if self.debug:
                input("\nPress any key to continue...")
                    
    def __fetch_instruction(self) -> Instruction:
        data = self.__memory.read_data(self.__processor.programCounter)
        instruction = Instruction.encode(data=data, address=self.__processor.programCounter)
        return instruction
                    
    def __execute_instruction(self, instruction: Instruction):
        operation_code, address = instruction.decode()
        if operation_code in self.__operationCodes:
            self.__operationCodes[operation_code](self, address, useDebug = self.debug)
        else:
            raise ValueError(f"Invalid operation code: {operation_code}")


    


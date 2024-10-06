from MemoryFiles.Interface.IMemory import IMemory
from GUI.CLI import singleListMemoryDumper as visualizer
from MemoryFiles.Validator.MemomryValidatorSingleList import MemoryValidatorSingleList

class MemorySingleList(IMemory):
    def __init__(self, size: int = 100):
        self.__memory = ["0000" for _ in range(size)]
        self.__validator = MemoryValidatorSingleList(self.__memory)
    
    def store_data(self, address: int, data) -> bool:
        # Validate address
        if not self.__validator.validateAddress(address):
            return False

        # Convert data to string if it is an integer
        if isinstance(data, int):
            data = str(data)
        
        # Check if the data is a valid instruction (string validation)
        if not self.__validator.validateInstruction(data):
            return False
        
        # Ensure the data is numeric and pad it with zeros to make it 4 characters long
        if data.isdigit():  # Ensure the string only contains digits
            formattedData = data.zfill(4)
        else:
            raise ValueError("input should be of type int")
            
        
        # Store the formatted data in memory
        self.__memory[address] = formattedData
        return True

    
    def read_data(self, address: int) -> int:
        if not self.__validator.validateAddress(address):
            return ""
        else:
            return int(self.__memory[address])
    
    def dump(self) -> bool:
        visualizer(self.__memory)
        
        
    

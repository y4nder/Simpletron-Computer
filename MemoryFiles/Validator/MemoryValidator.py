
from MemoryFiles.Memories.MemoryTypes import MasterMemory


class MemoryValidator:
    def __init__(self, memory: MasterMemory):
        self.__memory = memory
        self.__maxMemorySize = (self.__memory.getMemoryRowLimit() * self.__memory.getMemoryCellLimit())

    def validateAddress(self, address: str) -> bool:
        """
        Validate if the address is within the memory's valid range.
        
        The address should be in the format 'row:cell', where both row and cell are
        integers between 0 and memoryRowLimit-1 and memoryCellLimit-1 respectively.
        
        Args:
            memory (MasterMemory): The memory instance to validate against.
            address (str): The address in 'row:cell' format.
            
        Returns:
            bool: True if the address is valid, False otherwise.
        
        Raises:
            ValueError: If the address is not in the correct format.
        
        """
        try:
            # Convert address to integer
            addr_int = int(address)
            
            # Check if the address is between 0 and 99
            if 0 <= addr_int < (self.__maxMemorySize):
                return True
            else:
                print(f"Address {addr_int} is out of bounds. Must be between {0}0 and {self.__maxMemorySize - 1}.")
                return False
        except ValueError:
            print("Invalid address format. Please provide a numeric value between 0 and 99.")
            return False

    def validateData(self, data: str) -> bool:
        """
        Validate if the data is exactly 4 characters long.
        
        Args:
            memory (MasterMemory): The memory instance (not used but included for consistency).
            data (str): The data to be stored.
        
        Returns:
            bool: True if the data is exactly 4 characters long, False otherwise.
        
        """
        if len(data) == 4:
            return True
        else:
            print("Invalid data length. Data must be exactly 4 characters long.")
            return False

    def validateMemoryInstance(self) -> bool:
        if self.__memory is None:
            print("Error: Memory instance is not initialized")
            return False

        if not self.__memory:
            print("Error: Memory is empty")
            return False
        
        return True
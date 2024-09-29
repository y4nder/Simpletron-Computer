from abc import ABC, abstractmethod

class IMemoryValidator(ABC):    
    @abstractmethod
    def validateAddress(self, address:int) -> bool:
        pass
    
    @abstractmethod
    def validateInstruction(self, instruction: str) -> bool:
        pass
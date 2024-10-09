from abc import ABC, abstractmethod

class IMemory(ABC):
    
    @abstractmethod
    def store_data(self, address: int, data: str)-> bool:
        pass
    
    @abstractmethod
    def read_data(self, address: int) -> str:
        pass
    
    @abstractmethod
    def dump(self, pointer_index: int = None) -> bool:
        pass
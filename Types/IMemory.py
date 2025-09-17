from abc import ABC, abstractmethod


class IMemory(ABC):
    @abstractmethod
    def get_memory_length(self)-> int:
        pass
    
    @abstractmethod
    def store_data(self, address: int, data: str)-> bool:
        pass
    
    @abstractmethod
    def read_data(self, address: int) -> str:
        pass
    
    @abstractmethod
    def dump(self, pointer_index: int = -1) -> bool:
        pass
    
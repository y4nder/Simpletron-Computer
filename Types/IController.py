from abc import ABC, abstractmethod

from ProcessorFiles.Processor import Processor
from Types.IMemory import IMemory



class IController(ABC):
    
    @abstractmethod
    def get_processor_instance(self) -> Processor:
        pass

    @abstractmethod
    def get_memory_instance(self) -> IMemory:
        pass
    
    @abstractmethod
    def run(self) -> None:
        pass
    
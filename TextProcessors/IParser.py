from abc import ABC, abstractmethod

from TextProcessors.Instruction import Instruction

class IParser(ABC):
    def __init__(self, debug: bool):
        self.debug = debug
    
    @abstractmethod
    def parse(self, fileAddress: str) -> list[Instruction]: pass
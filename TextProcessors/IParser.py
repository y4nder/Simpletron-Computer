from abc import ABC, abstractmethod

from TextProcessors.Instruction import Instruction

class IParser(ABC):
    @abstractmethod
    def parse(self, fileAddress: str) -> list[Instruction]: pass
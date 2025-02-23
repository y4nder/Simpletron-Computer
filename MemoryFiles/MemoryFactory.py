from enum import Enum

from MemoryFiles.Memories.Memory import Memory
from MemoryFiles.Memories.MemorySingleList import MemorySingleList
from Types.IMemory import IMemory


class MemoryType(str, Enum):
    Object = "object"
    Array = "array"

class MemoryFactory(object):    
    @staticmethod
    def Use(memoryType: MemoryType) -> IMemory:
        if memoryType == MemoryType.Object:
            return Memory()
        elif memoryType == MemoryType.Array:
            return MemorySingleList()
        else:
            raise ValueError("Invalid Memory Type")

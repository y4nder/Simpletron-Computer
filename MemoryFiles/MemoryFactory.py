from MemoryFiles.Interface.IMemory import IMemory
from MemoryFiles.Memories.Memory import Memory
from MemoryFiles.Memories.MemorySingleList import MemorySingleList


class MemoryFactory(object):
    def Memory() -> IMemory:
        return Memory()
    
    def MemorySingleList() -> IMemory:
        return MemorySingleList()
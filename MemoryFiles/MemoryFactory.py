from MemoryFiles.Interface.IMemory import IMemory
from MemoryFiles.Memories.Memory import Memory
from MemoryFiles.Memories.MemorySingleList import MemorySingleList


class MemoryFactory(object):
    def Memory() -> IMemory:
        """ Creates an Object Based Memory Bati nani, but keeping it for the design pattern 🎇
        Returns:
            IMemory: Memory
        """
        return Memory()
    
    def MemorySingleList() -> IMemory:
        """ Creates a Memory That uses a single list simpler version, easy to debug 
        Returns:
            IMemory: MemorySingleList
        """
        return MemorySingleList()
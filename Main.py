
from MemoryFiles.Memory import Memory
from MemoryFiles.MemoryLoader import MemoryLoader 


if __name__ == "__main__":
    memory = Memory()
    memoryLoader = MemoryLoader()
    memoryLoader.load("TextProcessors/testFile.sml", memory)

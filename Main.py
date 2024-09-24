
from MemoryFiles.Memory import Memory
from MemoryFiles.MemoryLoader import MemoryLoader 
from os import system
from TextProcessors.LowLevelParser import LowLevelParser

if __name__ == "__main__":
    system("cls")
    memory = Memory()
    memoryLoader = MemoryLoader(memory = memory,parser = LowLevelParser())
    memoryLoader.load("TextProcessors/testFile.sml")

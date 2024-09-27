from CLI_Testers.MemoryCLI import memoryCLI
from MemoryFiles.Memory import Memory
from MemoryFiles.MemoryLoader import MemoryLoader 
from TextProcessors.ParserFactory import ParserFactory
from os import system


def testMemoryLoader():
    system("cls")
    file = "TextProcessors/testFile.sml"
    memory = Memory()
    memoryLoader = MemoryLoader(memory, ParserFactory.LowLevelParser())
    memoryLoader.load(file)
    
def testMemoryCLI():
    memoryCLI()
    
if __name__ == "__main__":
    testMemoryLoader()
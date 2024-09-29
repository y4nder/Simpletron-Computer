from CLI_Testers.MemoryCLI import memoryCLI
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from TextProcessors.ParserFactory import ParserFactory
from os import system


def testMemoryLoader():
    file = "TextProcessors/testFile.sml"
    memory = MemoryFactory.MemorySingleList()
    memoryLoader = MemoryLoader(memory, ParserFactory.LowLevelParser())
    memoryLoader.load(file)
    
def testMemoryCLI():
    memoryCLI()
    
if __name__ == "__main__":
    system("cls")
    testMemoryLoader()
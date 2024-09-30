from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.Processor import Processor
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from os import system

    
def testOperationCodes():
    #create instance of processor and memory
    processor = Processor()
    memory = MemoryFactory.MemorySingleList()
    
    #load memory with sml program
    file = "testCodes/Factorial.sml"
    parser = ParserFactory.LowLevelParser()
    memoryLoader = MemoryLoader(memory, parser)
    memoryLoader.load(file)
    
    #define the library
    library = OperationLibrary.OPERATION_CODES_DEFAULT
    
    #create controller instace and inject the processor, memory and library
    controller = Controller(processor, memory, library)
    
    print("-" * 10)
    print("executing file")
    
    #run the program
    controller.run()
    
if __name__ == "__main__":
    system("cls")
    testOperationCodes()
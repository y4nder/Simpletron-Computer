from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from os import system
import sys

    
def run(fileAddress: str):
    # change to True for debugging
    debug: bool = False
    
    #create instance of processor and memory
    processor = ProcessorFactory.Processor_DEFAULT()
    memory = MemoryFactory.MemorySingleList()
    
    #Create instance of a parser and a memoryloaoder 
    parser = ParserFactory.LowLevelParser(debug=debug)
    memoryLoader = MemoryLoader(memory, parser, debug=debug)
    
    # load memory with sml program
    memoryLoader.load(fileAddress)
    
    #define the library
    library = OperationLibrary.OPERATION_CODES_DEFAULT
    
    #create controller instace and inject the processor, memory and library
    controller = Controller(processor, memory, operationCodes=library, debug=debug)
    
    if(debug):
        print("-" * 50)
        print("executing file")
    
    #run the controller
    controller.run()
            
def main():
    if len(sys.argv) != 2:
        print("Usage: python Simpletron.py <filename>.sml")
    else:
        fileAddress = "codes/" + sys.argv[1]
        run(fileAddress)
        
if __name__ == "__main__":
    system("cls")
    main()
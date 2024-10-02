from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.Processor import Processor
from TextProcessors.MnemonicParser import MnemonicParser
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from os import system
import sys

    
def testOperationCodes(fileAddress: str):
    debug: bool = False
    #create instance of processor and memory
    processor = Processor()
    memory = MemoryFactory.MemorySingleList()
    
    #load memory with sml program
    file = fileAddress
    parser = ParserFactory.LowLevelParser(debug=debug)
    memoryLoader = MemoryLoader(memory, parser, debug=debug)
    memoryLoader.load(file)
    
    #define the library
    library = OperationLibrary.OPERATION_CODES_DEFAULT
    
    #create controller instace and inject the processor, memory and library
    controller = Controller(processor, memory, library, debug=debug)
    
    print("-" * 10)
    print("executing file")
    
    #run the program
    controller.run()
            
def startWithFileName():
    if len(sys.argv) != 2:
        print("Usage: python Main.py <filename>")
    else:
        header = "testCodes/" + sys.argv[1]
        testOperationCodes(header)
        
def testMnemonicParser():
    file = "testCodes/mnemonics.sml"
    mp = MnemonicParser()
    p = mp.parse(file)
    for x in p:
        print(x)
    
    
if __name__ == "__main__":
    system("cls")
    startWithFileName()
from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.Processor import Processor
from TextProcessors.MnemonicParser import MnemonicParser
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from os import system

    
def testOperationCodes():
    debug: bool = False
    #create instance of processor and memory
    processor = Processor()
    memory = MemoryFactory.MemorySingleList()
    
    #load memory with sml program
    file = "testCodes/FactorialM.sml"
    parser = ParserFactory.MnemonicParser(debug=True)
    memoryLoader = MemoryLoader(memory, parser, debug=True)
    memoryLoader.load(file)
    
    #define the library
    library = OperationLibrary.OPERATION_CODES_DEFAULT
    
    #create controller instace and inject the processor, memory and library
    controller = Controller(processor, memory, library, debug=debug)
    
    print("-" * 10)
    print("executing file")
    
    #run the program
    controller.run()
    
def testMnemonicParser():
    file = "testCodes/mnemonics.sml"
    mp = MnemonicParser()
    p = mp.parse(file)
    for x in p:
        print(x)
    
    
if __name__ == "__main__":
    system("cls")
    testOperationCodes()
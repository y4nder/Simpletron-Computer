from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.IParser import IParser
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from os import system
import sys
import argparse

    
def run(fileAddress: str, useMnemonic: bool, useDebug: bool):
    # change to True for debugging
    debug: bool = useDebug
    
    #create instance of processor and memory
    processor = ProcessorFactory.Processor_DEFAULT()
    memory = MemoryFactory.MemorySingleList()
    
    #Create instance of a parser and a memoryloaoder 
    parser = defineParser(useMnemonic, useDebug)
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
    
def defineParser(useMnemonic: bool, useDebug: bool) -> IParser:
    if useMnemonic:
        return ParserFactory.MnemonicParser(debug = useDebug)
    else:
        return ParserFactory.LowLevelParser(debug = useDebug)
            
def Main():
    argsParser = argparse.ArgumentParser(description="run simpletron script")
    argsParser.add_argument("fileAddress", type=str, help="name of the file ending with .sml")
    argsParser.add_argument("-mp", action="store_true", help="choose mnemonic parser" )
    argsParser.add_argument("-debug", action="store_true", help="Enable debug mode")
    
    args = argsParser.parse_args()
    fileAddress = "codes/" + args.fileAddress
    useMnemonic = args.mp
    useDebug = args.debug
    run(fileAddress, useMnemonic, useDebug)
    
        
if __name__ == "__main__":
    system("cls")
    Main()
from os import system, path
from Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader 
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.ParserFactory import ParserFactory
from Operations.OperationLibrary import OperationLibrary
from util.args_util import ArgumentFactory

    
def create_components(fileAddress: str, useMnemonic: bool, useDebug: bool, **kwargs) -> Controller:
    processor = ProcessorFactory.Processor_DEFAULT()
    memory = MemoryFactory.MemorySingleList()
    parser = ParserFactory.GetParser(useMnemonic, debug=False)
    memoryLoader = MemoryLoader(memory, parser, debug=False)
    
    try:
        memoryLoader.load(fileAddress)
    except Exception as e:
        print(f"Error loading memory: {e}")
    
    codes = OperationLibrary.OPERATION_CODES_DEFAULT
    controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)
    
    return controller

def run(fileAddress: str, useMnemonic: bool, useDebug: bool, **kwargs) -> None:
    controller = create_components(fileAddress, useMnemonic, useDebug, **kwargs)
    
    if(useDebug):
        print("-" * 50)
        print("executing file")
    
    controller.run()

def main() -> None:
    args = ArgumentFactory.DEFAULT_ARGUMENTS()
    
    if not args.filename.endswith('.sml'):
        raise ValueError("Invalid file extension. File must end with '.sml'")
    
    fileAddress: str = path.join("codes", args.filename)
    useMnemonic: bool = args.mp
    useDebug: bool = args.debug

    run(fileAddress, useMnemonic, useDebug)
        
if __name__ == "__main__":
    system("cls")
    main()
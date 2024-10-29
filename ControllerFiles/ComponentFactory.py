from ControllerFiles.Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader
from Operations.OperationLibrary import OperationLibrary
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.ParserFactory import ParserFactory


class ComponentFactory:
    '''Version 1 uses low level parsing'''
    def UseVersion1(fileAddress: str, useDebug: bool = False) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.LowLevelParser(debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        ComponentFactory.__runMemoryLoad(memoryLoader, fileAddress)

        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller
            
    '''Version 2 uses mnemonic parsing'''
    def UseVersion2(fileAddress: str, useDebug: bool) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.MnemonicParser(debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        ComponentFactory.__runMemoryLoad(memoryLoader,fileAddress)
        
        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller
    
    '''Version 3 uses mnemonic parsing but now without addressses'''
    def UseVersion3(fileAddress: str, useDebug: bool) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.MnemonicParserV2(debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        ComponentFactory.__runMemoryLoad(memoryLoader,fileAddress)
        
        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller
    
    def __runMemoryLoad(memoryLoader: MemoryLoader, fileAddress: str) -> None:
        try: 
            memoryLoader.load(fileAddress)
        except Exception as e:
            print(f"Erorr loading memory: {e}")
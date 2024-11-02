from ControllerFiles.Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory
from MemoryFiles.MemoryLoader import MemoryLoader
from Operations.OperationLibrary import OperationLibrary
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.ParserFactory import ParserFactory


class SimpletronFactory:
    '''
        `UseVersion1()` : uses low level parsing [For opcode usage]
        `UseVersion2()` : uses mnemonic parsing [depracated]
        `UseVersion3()` : uses mnemonic parsing [updated]
    '''
    def UseVersion1(fileAddress: str, useDebug: bool = False) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.LowLevelParser(debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        SimpletronFactory.__runMemoryLoad(memoryLoader, fileAddress)

        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller
            
    def UseVersion2(fileAddress: str, useDebug: bool) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.MnemonicParserV1(debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        SimpletronFactory.__runMemoryLoad(memoryLoader,fileAddress)
        
        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller

    def UseVersion3(fileAddress: str, useDebug: bool) -> Controller:
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.MemorySingleList()
        parser = ParserFactory.MnemonicParserV2(memoryLimit = memory.get_memory_length(),debug = useDebug)
        memoryLoader = MemoryLoader(memory, parser, debug=useDebug)
        
        SimpletronFactory.__runMemoryLoad(memoryLoader,fileAddress)
        
        codes = OperationLibrary.OPERATION_CODES_DEFAULT
        
        controller = Controller(processor, memory, operationCodes=codes, debug=useDebug)  
        return controller
    
    def __runMemoryLoad(memoryLoader: MemoryLoader, fileAddress: str) -> None:
        try: 
            memoryLoader.load(fileAddress)
        except Exception as e:
            raise e
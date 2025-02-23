from enum import Enum
from ControllerFiles.Controller import Controller
from MemoryFiles.MemoryFactory import MemoryFactory, MemoryType
from MemoryFiles.MemoryLoader import MemoryLoader
from Operations.OperationLibrary import OperationLibrary
from ProcessorFiles.ProcessorFactory import ProcessorFactory
from TextProcessors.ParserFactory import ParserFactory, ParserVer
from Types.IController import IController



class SmpVer(str, Enum):
    VERSION1 = "v1"
    VERSION2 = "v2"
    VERSION3 = "v3"


class SimpletronFactory:
    """
    `Use(version, fileAddress, useDebug)`: Creates a Simpletron instance based on version.

    - `VERSION1`: Uses low-level parsing [For opcode usage].
    - `VERSION2`: Uses mnemonic parsing [Deprecated].
    - `VERSION3`: Uses updated mnemonic parsing.
    """

    @staticmethod
    def Use(version: SmpVer, fileAddress: str, useDebug: bool = False) -> IController:
        version_map = {
            SmpVer.VERSION1: SimpletronFactory.__use_version1,
            SmpVer.VERSION2: SimpletronFactory.__use_version2,
            SmpVer.VERSION3: SimpletronFactory.__use_version3,
        }

        if version in version_map:
            return version_map[version](fileAddress, useDebug)

        raise ValueError(f"Invalid version: {version}")

    @staticmethod
    def __initialize_components(memory_type: MemoryType, parserVer: ParserVer, useDebug: bool):
        """Initializes processor, memory, and memory loader."""
        processor = ProcessorFactory.Processor_DEFAULT()
        memory = MemoryFactory.Use(memory_type)
        memory_limit = memory.get_memory_length() if memory is not None else 99
        parser = ParserFactory.Use(parserVer, memoryLimit=memory_limit, debug=useDebug)
        memory_loader = MemoryLoader(memory, parser, debug=useDebug)
        return processor, memory, parser, memory_loader

    @staticmethod
    def __use_version1(fileAddress: str, useDebug: bool) -> IController:
        processor, memory, _, memory_loader = SimpletronFactory.__initialize_components(
            MemoryType.Object, ParserVer.LOW_LEVEL, useDebug
        )
        SimpletronFactory.__run_memory_load(memory_loader, fileAddress)
        return Controller(processor, memory, OperationLibrary.OPERATION_CODES_DEFAULT, debug=useDebug)

    @staticmethod
    def __use_version2(fileAddress: str, useDebug: bool) -> IController:
        processor, memory, _, memory_loader = SimpletronFactory.__initialize_components(
            MemoryType.Array, ParserVer.MNEMONIC_V1, useDebug
        )
        SimpletronFactory.__run_memory_load(memory_loader, fileAddress)
        return Controller(processor, memory, OperationLibrary.OPERATION_CODES_DEFAULT, debug=useDebug)

    @staticmethod
    def __use_version3(fileAddress: str, useDebug: bool) -> IController:
        processor, memory, _, memory_loader = SimpletronFactory.__initialize_components(
            MemoryType.Array, ParserVer.MNEMONIC_V2, useDebug
        )
        SimpletronFactory.__run_memory_load(memory_loader, fileAddress)
        return Controller(processor, memory, OperationLibrary.OPERATION_CODES_DEFAULT, debug=useDebug)

    @staticmethod
    def __run_memory_load(memory_loader: MemoryLoader, fileAddress: str) -> None:
        try:
            memory_loader.load(fileAddress)
        except Exception as e:
            raise RuntimeError(f"Memory loading failed: {e}") from e

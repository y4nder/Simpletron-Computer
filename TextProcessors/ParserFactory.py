from enum import Enum
from TextProcessors.parsers.LowLevelParser import LowLevelParser
from TextProcessors.parsers.MnemonicParser import MnemonicParserV1
from TextProcessors.parsers.MnemonicParserV2 import MnemonicParserV2
from Types.IParser import IParser


class ParserVer(str, Enum):
    LOW_LEVEL = "low_level"
    MNEMONIC_V1 = "mnemonic_v1"
    MNEMONIC_V2 = "mnemonic_v2"


class ParserFactory:
    @staticmethod
    def Use(version: ParserVer, memoryLimit: int = 99, debug: bool = False) -> IParser:
        """Returns a parser instance based on the given version."""
        version_map = {
            ParserVer.LOW_LEVEL: lambda: ParserFactory.LowLevelParser(debug),
            ParserVer.MNEMONIC_V1: lambda: ParserFactory.MnemonicParserV1(debug),
            ParserVer.MNEMONIC_V2: lambda: ParserFactory.MnemonicParserV2(memoryLimit, debug),
        }

        if version in version_map:
            return version_map[version]()

        raise ValueError(f"Invalid parser version: {version}")

    @staticmethod
    def LowLevelParser(debug: bool = False) -> IParser:
        """Parser for directly parsing simpletron operation codes."""
        return LowLevelParser(debug)

    @staticmethod
    def MnemonicParserV1(debug: bool = False) -> IParser:
        """First version of the mnemonic parser."""
        return MnemonicParserV1(debug=debug)

    @staticmethod
    def MnemonicParserV2(memoryLimit: int = 99, debug: bool = False) -> IParser:
        """Second version of the mnemonic parser with memory limit support."""
        return MnemonicParserV2(memoryLimit=memoryLimit, debug=debug)

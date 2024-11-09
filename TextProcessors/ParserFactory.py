from TextProcessors.IParser import IParser
from TextProcessors.parsers.LowLevelParser import LowLevelParser
from TextProcessors.parsers.MnemonicParser import MnemonicParserV1
from TextProcessors.parsers.MnemonicParserV2 import MnemonicParserV2

class ParserFactory:
    '''Parser for directly parsing simpletron operation codes'''
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
    
    def MnemonicParserV1(debug: bool = False) -> IParser:
        return MnemonicParserV1(debug=debug)
    
    def MnemonicParserV2(memoryLimit: int = 99, debug: bool = False) -> IParser:
        return MnemonicParserV2(memoryLimit=memoryLimit,debug=debug)
    
    
from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser
from TextProcessors.MnemonicParser import MnemonicParserV1
from TextProcessors.MnemonicParserV2 import MnemonicParserV2

class ParserFactory:
    '''Parser for directly parsing simpletron operation codes'''
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
    
    def MnemonicParserV1(debug: bool = False) -> IParser:
        return MnemonicParserV1(debug=debug)
    
    def MnemonicParserV2(memoryLimit: int = 99, debug: bool = False) -> IParser:
        return MnemonicParserV2(memoryLimit=memoryLimit,debug=debug)
    
    
    
    def GetParser(useMnemonic: bool, debug: bool = False) -> IParser:
        if useMnemonic:
            return MnemonicParserV1(debug=debug)
        else:
            return LowLevelParser(debug=debug)
        
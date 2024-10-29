from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser
from TextProcessors.MnemonicParser import MnemonicParser
from TextProcessors.MnemonicParserV2 import MnemonicParserV2

class ParserFactory:
    '''Parser for directly parsing simpletron operation codes'''
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
    
    def MnemonicParser(debug: bool = False) -> IParser:
        return MnemonicParser(debug=debug)
    
    def MnemonicParserV2(debug: bool = False) -> IParser:
        return MnemonicParserV2(debug=debug)
    
    
    
    def GetParser(useMnemonic: bool, debug: bool = False) -> IParser:
        if useMnemonic:
            return MnemonicParser(debug=debug)
        else:
            return LowLevelParser(debug=debug)
        
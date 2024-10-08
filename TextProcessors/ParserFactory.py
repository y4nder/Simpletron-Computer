from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser
from TextProcessors.MnemonicParser import MnemonicParser

class ParserFactory:
    '''Parser for directly parsing simpletron operation codes'''
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
    
    def MnemonicParser(debug: bool = False) -> IParser:
        return MnemonicParser(debug=debug)
    
    def GetParser(useMnemonic: bool, debug: bool = False) -> IParser:
        if useMnemonic:
            return MnemonicParser(debug=debug)
        else:
            return LowLevelParser(debug=debug)
        
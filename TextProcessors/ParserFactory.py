from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser
from TextProcessors.MnemonicParser import MnemonicParser

class ParserFactory:
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
    
    def MnemonicParser(debug: bool = False) -> IParser:
        return MnemonicParser(debug)
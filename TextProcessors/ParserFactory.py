from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser

class ParserFactory:
    def LowLevelParser(debug: bool = False) -> IParser:
        return LowLevelParser(debug)
from TextProcessors.IParser import IParser
from TextProcessors.LowLevelParser import LowLevelParser

class ParserFactory:
    def LowLevelParser() -> IParser:
        return LowLevelParser()
from Operations.MnemonicLibrary import MnemonicLibrary
from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction
from TextProcessors.LowLevelParser import LowLevelParser


class MnemonicParser(IParser):
    def __init__(self, lowLevelParser: IParser = LowLevelParser(), mnemonicLibray = MnemonicLibrary, debug: bool = True):
        super().__init__(debug)
        self.lowlevelParser = lowLevelParser
        self.mneomonicLibrary = mnemonicLibray.DEFAULT_MNEMONIC
        
    def parse(self, fileAddress: str) -> list[Instruction]:
        return self.__start(fileAddress)
    
    def __start(self, fileAddress: str):
        if(self.debug):
            print("-"*50)
            print(f"parsing file {fileAddress}")
        
        splittedWords = []
        with open(fileAddress, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                splittedWords.append(word)
                
                if self.debug:
                    print(word)
                    
        sanitizedCommands = self.__cleanUp(splittedWords)
        return sanitizedCommands    
                
    
    def __cleanUp(self, listOfCommands: list[list[str]]):
        if self.debug:
            print("-"*50)
            print("\nperform clean up\n")
            
        sanitizedCommands = []
        for lineCommand in listOfCommands:
            line = []
            for command in lineCommand:
                if(command == ";"):
                    break
                else:
                    line.append(command)
            if line:
                sanitizedCommands.append(line)
                
                if self.debug:
                    print(line)
                    
                line = []
        return self.__assignMnemonic(sanitizedCommands)
                
    def __assignMnemonic(self, sanitizedCommands: list[list[str]]):
        if self.debug:
            print("\nassigning mnemonics\n")
            
        convertedCommands: list[Instruction] = []
        for lineCommand in sanitizedCommands:
            address = lineCommand[0]
            mnemonic = lineCommand[1]
            data = lineCommand[2]
            
            opcode = str(self.mneomonicLibrary[mnemonic]) + data
            
            instuction = Instruction(int(address), opcode)
            convertedCommands.append(instuction)
            
        return convertedCommands
                
    
    

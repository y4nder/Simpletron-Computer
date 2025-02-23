from Operations.MnemonicLibrary import MnemonicLibrary
from TextProcessors.entities.Instruction import Instruction
from Types.IParser import IParser

class MnemonicParserV1(IParser):
    def __init__(self, mnemonicLibray = MnemonicLibrary, debug: bool = True):
        super().__init__(debug)
        self.mnemonicLibrary = mnemonicLibray.DEFAULT_MNEMONIC
        
    def parse(self, fileAddress: str) -> list[Instruction]:
        return self.__start(fileAddress)
    
    def __start(self, fileAddress: str) -> list[Instruction]:
        try:
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
                        
            return self.__cleanUp(splittedWords)
        
        except Exception as e:
            print(f"Error occurred during file parsing: {e}")
            return []
                
    
    def __cleanUp(self, listOfCommands: list[list[str]])-> list[Instruction]:
        if self.debug:
            print("-"*50)
            print("\nperform clean up\n")
            
        sanitizedCommands = []
        for lineCommand in listOfCommands:
            line = []
            for command in lineCommand:
                if(self.__isComment(command)):
                    break
                else:
                    line.append(command)
            if line:
                sanitizedCommands.append(line)
                
                if self.debug:
                    print(line)
                
                line = []
                
        return self.__assignMnemonic(sanitizedCommands)
                
    def __assignMnemonic(self, sanitizedCommands: list[list[str]])-> list[Instruction]:
        lineCount: int = 0
        if self.debug:
            print("\nassigning mnemonics\n")
            
        convertedCommands: list[Instruction] = []
        for lineCommand in sanitizedCommands:
            address = lineCount
            mnemonic = lineCommand[0]
            data = lineCommand[1]    
            opcode = str(self.mnemonicLibrary[mnemonic]) + data
            instuction = Instruction(int(address), opcode)
            convertedCommands.append(instuction)
            lineCount += 1
            
        return convertedCommands
            
    # helper methods
    def __isComment(self, command: str) -> bool:
        return command == ";" or command.startswith(";")
    
    

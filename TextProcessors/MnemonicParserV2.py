from Operations.MnemonicLibrary import MnemonicLibrary
from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction

class MnemonicParserV2(IParser):
    def __init__(self, mnemonicLibray = MnemonicLibrary, debug: bool = True):
        super().__init__(debug)
        self.mnemonicLibrary = mnemonicLibray.DEFAULT_MNEMONIC
        self.AddressMemoryCounter = 0;
        self.AddressMemoryDict = dict();
        self.HaltCommand = mnemonicLibray.HALT_COMMAND
        
        
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
            
            if(mnemonic == self.HaltCommand):
                print(self.HaltCommand)
                data = "00"
            else : 
                if(mnemonic.startswith("J")):
                    if(self.debug):
                        print("found jump statement")
                    data = self.__determineJumpAddress(lineCommand[1], sanitizedCommands)
                else:
                    data = self.__determinVariableAddress(lineCommand[1])  
            
            
            opcode = str(self.mnemonicLibrary[mnemonic]) + data.zfill(2)
            instuction = Instruction(int(address), opcode)
            convertedCommands.append(instuction)
            lineCount += 1
            
        return convertedCommands
            
    # helper methods
    def __isComment(self, command: str) -> bool:
        return command == ";" or command.startswith(";")
    
    
    def __determinVariableAddress(self, data:str):
        if(data.isalpha()):
            if(data in self.AddressMemoryDict):
                return str(self.AddressMemoryDict[data])
            else:
                self.AddressMemoryDict[data] = 99 - self.AddressMemoryCounter
                self.AddressMemoryCounter = self.AddressMemoryCounter + 1
                return str(self.AddressMemoryDict[data])
        else:
            return data
        
    
    def __determineJumpAddress(self, variable: str, lineCommands):
        lineCount:int = 0;
        for command in lineCommands:
            if(len(command) > 2 and command[3] == variable):
                if(self.debug):
                    print(f"{variable} jump address @ {lineCount}")
                return str(lineCount).zfill(2)
            lineCount = lineCount + 1   
        return None
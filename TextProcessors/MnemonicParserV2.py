from Operations.MnemonicLibrary import MnemonicLibrary
from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction

class MnemonicParserV2(IParser):
    def __init__(self, memoryLimit: int, mnemonicLibray = MnemonicLibrary, debug: bool = True):
        super().__init__(debug)
        self.mnemonicLibrary = mnemonicLibray.DEFAULT_MNEMONIC
        self.AddressMemoryCounter = 0;
        self.AddressMemoryDict = dict();
        self.memoryLimit = memoryLimit
        self.HaltCommand = mnemonicLibray.HALT_COMMAND
        self.JumpMarker = mnemonicLibray.JUMP_LABEL
        
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
            raise e
                
    
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
                
    def __assignMnemonic(self, sanitizedCommands: list[list[str]]) -> list[Instruction]:
        if self.debug:
            print("\nAssigning mnemonics\n")

        convertedCommands : list[Instruction]= [] 
        labelAddressMap = {}

        address: int = 0
        for lineCommand in sanitizedCommands:
            if len(lineCommand) > 2 and self.JumpMarker in lineCommand:
                label = lineCommand[-1]
                labelAddressMap[label] = address
            else: 
                address = address + 1
        
        address : int = 0
        for lineCommand in sanitizedCommands:
            if(lineCommand[0] == self.JumpMarker):
                continue
            mnemonic = Mnemonic(lineCommand[0], address)
            
            data:str
            
            if self._hasIndependentKeyWord(lineCommand, address):
                data = "00"
            elif mnemonic.IsJumpStatement():
                if self.debug:
                    print("Found jump statement")
                data = labelAddressMap.get(lineCommand[1], "??")
            else:
                data = self.__determineVariableAddress(lineCommand[1])

            opcode = str(self.mnemonicLibrary[mnemonic]) + str(data).zfill(2)
            instruction = Instruction(int(address), opcode)
            convertedCommands.append(instruction)
            address = address + 1

        return convertedCommands

    # helper methodss
    def _hasIndependentKeyWord(self, lineCommand, address):
        if len(lineCommand) == 1:
            mnemonic = Mnemonic(lineCommand[0], address)
            if mnemonic.IsIndependent():
                return True
        raise ValueError(f"invalid independent mnemonic usage {lineCommand[0]} at address {address}")
            
    def __isComment(self, command: str) -> bool:
        return command == ";" or command.startswith(";")
    
    
    def __determineVariableAddress(self, data:str):
        if data.isalpha():
            if(data in self.AddressMemoryDict):
                return str(self.AddressMemoryDict[data])
            else:
                self.AddressMemoryDict[data] = self.memoryLimit - self.AddressMemoryCounter
                self.AddressMemoryCounter += 1
                return str(self.AddressMemoryDict[data])
        else:
            return data
    
class Mnemonic(str):
    def __new__(cls, value, address):
        if not MnemonicLibrary.DEFAULT_MNEMONIC.get(value):
            raise ValueError(f"Unknown mnemonic: '{value}' at address: {address}")
        
        obj = super().__new__(cls, value)
        return obj
    
    def IsJumpStatement(self):
        return self.startswith("J") or self.startswith("j")

    def IsIndependent(self):
        return self in MnemonicLibrary.INDEPENDENT_MNEMONICS
            

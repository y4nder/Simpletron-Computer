from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction
from TextProcessors.Mnemonic import Mnemonic
from TextProcessors.Opcode import Opcode

class MnemonicParserV2(IParser):
    def __init__(self, memoryLimit: int, debug: bool = True):
        super().__init__(debug)
        self.AddressMemoryCounter = 0;
        self.AddressMemoryDict = dict();
        self.labelAddressMap = {};
        self.memoryLimit = memoryLimit
        
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
      
        address: int = 0
        for lineCommand in sanitizedCommands:
            if Mnemonic.JumpMarkerExistsIn(lineCommand):
                label = lineCommand[-1]
                self.labelAddressMap[label] = address
            else: 
                address +=1
        
        address : int = 0
        for lineCommand in sanitizedCommands:
            mnemonic = Mnemonic.ExtractFrom(lineCommand, address)
            
            if mnemonic.IsJumpMarker():
                continue
            
            data:int = self.__determineData(mnemonic, lineCommand, address)
            
            opcode = Opcode(mnemonic, data)
            instruction = Instruction(address, opcode)
            convertedCommands.append(instruction)
            address += 1

        return convertedCommands

    # helper methods
    def __determineData(self, mnemonic: Mnemonic, lineCommand, address) -> int:
        
        if mnemonic.IsIndependent(address, len(lineCommand)):
            return 00
        
        variable: str = lineCommand[1]
        
        if mnemonic.IsJumpStatement():
            if self.debug:
                print(f"Found jump statement {variable}")
            return self.labelAddressMap.get(variable, "??")
        else:
            return self.__determineVariableAddress(variable)
    
            
    def __isComment(self, command: str) -> bool:
        return command == ";" or command.startswith(";")
    
    def __determineVariableAddress(self, data:str) -> int:
        if data.isalpha():
            if(data in self.AddressMemoryDict):
                return self.AddressMemoryDict[data]
            else:
                self.AddressMemoryDict[data] = self.memoryLimit - self.AddressMemoryCounter
                self.AddressMemoryCounter += 1
                return self.AddressMemoryDict[data]
        else:
            return data
    

    

    
from TextProcessors.IParser import IParser
from TextProcessors.Instruction import Instruction

class LowLevelParser(IParser):
    def __init__(self, debug: bool = False):
        super().__init__(debug)
    
    def parse(self, fileAddress: str) -> list[Instruction]:
        return self.__startParse(fileAddress)

    def __startParse(self, fileAddress: str) -> list[Instruction]:
        if self.debug:
            print("-"*50)
            print(f"\nparsing the file: {fileAddress}\n")
            
        splittedWords = []
        with open(fileAddress, "r") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                if word:
                    splittedWords.append(word)
                    
                    if self.debug:
                        print(word) 
                    
        return self.__cleanUp(splittedWords)

    def __cleanUp(self, listOfCommands: list[list[str]]) -> list[Instruction]:
        
        if self.debug:
            print("-"*50)
            print("\nperforming cleaning up\n")
        
        lineNumber: int = 0
        sanitizedCommands: list[Instruction] = []
        for lineCommand in listOfCommands:
            line = []   
            for command in lineCommand:
                if(command == ";"):
                    break
                else:
                    line.append(command)
            if line:
                instruction = Instruction(int(line[0]),line[1])      
                sanitizedCommands.append(instruction)
                line = []
                lineNumber += 1
        return sanitizedCommands
            


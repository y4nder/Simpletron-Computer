from TextProcessors.entities.Instruction import Instruction


class Processor(object):
    def __init__(self):
        self.__accumulator = 0
        self.__programCounter = 0
        self.__instructionRegister = ""
        self.__operationCode = 0
        self.__operand = ""
        
    # Getter and Setter for accumulator
    @property
    def accumulator(self):
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, value):
        self.__accumulator = value

    # Getter and Setter for programCounter
    @property
    def programCounter(self):
        return self.__programCounter

    @programCounter.setter
    def programCounter(self, value):
        self.__programCounter = value

    # Getter and Setter for instructionRegister
    @property
    def instructionRegister(self):
        return self.__instructionRegister

    @instructionRegister.setter
    def instructionRegister(self, value):
        self.__instructionRegister = value

    # Getter and Setter for operationCode
    @property
    def operationCode(self):
        return self.__operationCode

    @operationCode.setter
    def operationCode(self, value):
        self.__operationCode = value

    # Getter and Setter for operand
    @property
    def operand(self):
        return self.__operand

    @operand.setter
    def operand(self, value):
        self.__operand = value
        
    def incrementProgramCounter(self) -> None:
        self.programCounter += 1
    
    def dump(self):
        print("REGISTERS: ")
        print(f"accumulator: +{self.__formatter(self.accumulator)}")
        print(f"programCounter: {self.__formatter(self.programCounter, zeroes=2)}")
        print(f"instructionRegister: +{self.__formatter(self.instructionRegister)}")
        print(f"operationCode: {self.__formatter(self.operationCode, zeroes=2)}")
        print(f"operand: {self.__formatter(self.operand, zeroes=2)}")
        
    def __formatter(self, data, zeroes = 4):
        return str(data).zfill(zeroes)
    
    def update_state(self, instruction: Instruction):
        operation_code, address = instruction.decode()
        self.instructionRegister = instruction.data
        self.operationCode = operation_code
        self.operand = address
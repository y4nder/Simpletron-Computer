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
        
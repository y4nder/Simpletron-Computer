class Instruction(object):
    def __init__(self, address:int, data:str):
        self.__address = address
        self.__data = data                

    @property
    def address(self) -> int:
        return self.__address
    
    @property
    def data(self) -> str:
        return self.__data
    
    def __str__(self) -> str:
        return f"address: {self.__address}  opcode: {self.__data}"
    
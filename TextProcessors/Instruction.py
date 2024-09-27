class Instruction(object):
    def __init__(self, address:int, data:str):
        self.__address = address
        self.__data = data
                
    def getAddress(self) -> int:
        return self.__address
    
    def getData(self) -> str:
        return self.__data
    
    def __str__(self) -> str:
        return f"address: {self.__address}  data: {self.__data}"
    
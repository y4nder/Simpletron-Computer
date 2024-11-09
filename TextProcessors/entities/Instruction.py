
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
    
            
    def decode(self):
        data = int(self.data)
        operation_code = data // 100
        address = data % 100
        return operation_code, address
    
    def encode(data: str, address: int):
        return Instruction(address, data)
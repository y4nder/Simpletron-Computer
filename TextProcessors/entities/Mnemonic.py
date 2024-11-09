from Operations.MnemonicLibrary import MnemonicLibrary


class Mnemonic(str):
    def __new__(cls, value, address):
        if not MnemonicLibrary.DEFAULT_MNEMONIC.get(value) and value not in MnemonicLibrary.RESERVED_KEYWORDS:
            raise ValueError(f"Unknown mnemonic: '{value}' at address: {address}")
        obj = super().__new__(cls, value)
        return obj
    
    def IsJumpStatement(self):
        return self.upper().startswith("J")

    def IsIndependent(self, address, length):
        if self in MnemonicLibrary.INDEPENDENT_MNEMONICS and length == 1:
            return True
        else:
            if(length == 1):
                raise ValueError(f"invalid independent mnemonic usage {self} at address {address} with length {length}")
            else:
                return False
            
    def IsJumpMarker(self):
        return self == MnemonicLibrary.JUMP_LABEL
    
    def JumpMarkerExistsIn(lineCommand:list[str]):
        return MnemonicLibrary.JUMP_LABEL in lineCommand and len(lineCommand) > 2
    
    def ExtractFrom(lineCommand: list[str], address: int):
        return Mnemonic(lineCommand[0], address)
    
    def RetrieveCode(self):
        return MnemonicLibrary.DEFAULT_MNEMONIC[self]
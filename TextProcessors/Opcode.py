from TextProcessors.Mnemonic import Mnemonic

class Opcode(str):
    def __new__(cls, mnemonic: Mnemonic, data: int):
        mnemonicCode = str(mnemonic.RetrieveCode())
        formattedData = str(data).zfill(2)
        obj = super().__new__(cls, mnemonicCode + formattedData)
        return obj
    
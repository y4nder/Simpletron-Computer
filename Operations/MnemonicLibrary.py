class MnemonicLibrary(object):
    HALT_COMMAND:str = "Halt"
    JUMP_LABEL: str = "Section"
    
    DEFAULT_MNEMONIC = {
        "Data"  : 00,
        "Read"  : 10,
        "Write" : 11,
        "WriteA": 12,
        "ReadI" : 13,
        "Load"  : 20,
        "Store" : 21,
        "LoadI" : 22,
        "Add"   : 30,
        "Sub"   : 31,
        "Div"   : 32,
        "Mod"   : 33,
        "Mul"   : 34,
        "AddI"  : 35,
        "SubI"  : 36,
        "DivI"  : 37,
        "ModI"  : 38,
        "MulI"  : 39,
        "JMP"   : 40,
        "JL"    : 41,
        "JZ"    : 42,
        HALT_COMMAND  : 43,
        "clr"   : 50
    }
    
    INDEPENDENT_MNEMONICS = ["WriteA", "ReadI", f"{HALT_COMMAND}"]
    
    
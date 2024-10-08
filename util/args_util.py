import argparse

class ArgumentFactory:    
    def DEFAULT_ARGUMENTS():
        argsParser = argparse.ArgumentParser(description="run simpletron script")
        argsParser.add_argument("filename", type=str, help="name of the file ending with .sml")
        argsParser.add_argument("-mp", action="store_true", help="Enable mnemonic parser, File must be written with valid mnemonics" )
        argsParser.add_argument("-debug", action="store_true", help="Enable debug mode")
        return argsParser.parse_args()
        
        
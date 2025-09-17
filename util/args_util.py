import argparse

class ArgumentFactory:    
    @staticmethod
    def DEFAULT_ARGUMENTS():
        argsParser = argparse.ArgumentParser(description="run simpletron script")
        argsParser.add_argument("filename", type=str, help="name of the file ending with .sml")
        argsParser.add_argument("-s", action="store_true", help="Run the program one at a time")
        return argsParser.parse_args()
        
        
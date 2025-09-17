import os

class CLIUtlity:
    @staticmethod
    def clearConsole():
        if os.name == "nt": 
            os.system("cls")
        else:
            os.system("clear")
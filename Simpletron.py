from os import path
from ControllerFiles.ComponentFactory import SimpletronFactory, SmpVer
from Types.IController import IController
from util.args_util import ArgumentFactory
from util.cli_util import CLIUtlity

def run(fileAddress: str, useDebug: bool) -> None:
    simpletron : IController = SimpletronFactory.Use(SmpVer.VERSION3, fileAddress, useDebug);
    
    if not isinstance(simpletron, IController):
        raise ValueError("Invalid controller instance")
    
    if(useDebug):
        print("-" * 50)
        print("executing file")
        
    simpletron.run()   

def main() -> None:
    args = ArgumentFactory.DEFAULT_ARGUMENTS()
    
    if not args.filename.endswith('.sml'):
        raise ValueError("Invalid file extension. File must end with '.sml'")
    
    fileAddress: str = path.join("codes", args.filename)
    useDebug: bool = args.s

    run(fileAddress, useDebug)

        
if __name__ == "__main__":
    CLIUtlity.clearConsole()
    main()
    
    
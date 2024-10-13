from os import system, path
from ControllerFiles.ComponentFactory import ComponentFactory
from util.args_util import ArgumentFactory

def run(fileAddress: str, useDebug: bool) -> None:
    simpletron = ComponentFactory.UseVersion1(fileAddress, useDebug);
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
    system("cls")
    main()
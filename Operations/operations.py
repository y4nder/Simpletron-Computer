from ControllerFiles.Controller import Controller

def read(controller: Controller, address: int, useDebug: bool = False):
    """Reads input into the memory address."""
    if useDebug:
        print("-"*100)
        print(f"Description: Get value from keyboard then store to address {str(address).zfill(2)}\n")
    value = int(input("Enter a number: "))    
    controller.get_memory_instance().store_data(address, value)
    controller.get_processor_instance().incrementProgramCounter()
    
def write(controller: Controller, address, useDebug: bool = False):
    """Writes the content of the memory address to output."""
    if useDebug:
        print("-"*100)
        print(f"Description: Read data from address {str(address).zfill(2)}\n")
    value = controller.get_memory_instance().read_data(address)
    print(f"\nMemory[{address}] = {value}")
    controller.get_processor_instance().incrementProgramCounter()

def write_acc(controller: Controller, _, useDebug: bool = False):
    """Writes the content of the accumulator."""
    if useDebug:
        print("-"*100)
        print("Description: Write to the screen the value in the accumulator\n")
    value = controller.get_processor_instance().accumulator
    print(f"accumulator: {value}")
    controller.get_processor_instance().incrementProgramCounter()
    
def readI(controller: Controller,_, useDebug: bool = False ):
    """Reads input into the memory address."""
    if useDebug:
        print("-"*100)
        print(f"Description: Read Value from keyboard and store to accumulator\n")
    value = int(input("Enter a number: "))    
    controller.get_processor_instance().accumulator = value
    controller.get_processor_instance().incrementProgramCounter();
    
def loadM(controller: Controller, address, useDebug: bool = False):
    """Loads the value from memory into the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Load the value from address {str(address).zfill(2)} into the accumulator\n")
    controller.get_processor_instance().accumulator = controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def store(controller: Controller, address, useDebug: bool = False):
    """Stores the accumulator's value into memory."""
    if useDebug:
        print("-"*100)
        print(f"Description: Store the accumulator value into address {str(address).zfill(2)}\n")
    controller.get_memory_instance().store_data(address, controller.get_processor_instance().accumulator)
    controller.get_processor_instance().incrementProgramCounter()

def loadI(controller: Controller, operand: int, useDebug: bool = False):
    """Load an immediate value (00-99) into the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Load the immediate value {str(operand).zfill(2)} into the accumulator\n")
    controller.get_processor_instance().accumulator = operand
    controller.get_processor_instance().incrementProgramCounter()

def addM(controller: Controller, address, useDebug: bool = False):
    """Adds the value from memory to the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Add the value from address {str(address).zfill(2)} to the accumulator\n")
    controller.get_processor_instance().accumulator += controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def subM(controller: Controller, address, useDebug: bool = False):
    """Subtracts the value from memory from the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Subtract the value from address {str(address).zfill(2)} from the accumulator\n")
    controller.get_processor_instance().accumulator -= controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def divM(controller: Controller, address, useDebug: bool = False):
    """Divides the accumulator by the value from memory."""
    if useDebug:
        print("-"*100)
        print(f"Description: Divide the accumulator by the value from address {str(address).zfill(2)}\n")
    controller.get_processor_instance().accumulator /= controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def modM(controller: Controller, address, useDebug: bool = False):
    """Performs modulo operation on the accumulator with the value from memory."""
    if useDebug:
        print("-"*100)
        print(f"Description: Modulo accumulator by the value from address {str(address).zfill(2)}\n")
    controller.get_processor_instance().accumulator %= controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def mulM(controller: Controller, address, useDebug: bool = False):
    """Multiplies the accumulator by the value from memory."""
    if useDebug:
        print("-"*100)
        print(f"Description: Multiply the accumulator by the value from address {str(address).zfill(2)}\n")
    controller.get_processor_instance().accumulator *= controller.get_memory_instance().read_data(address)
    controller.get_processor_instance().incrementProgramCounter()

def addI(controller: Controller, operand: int, useDebug: bool = False):
    """Add the immediate operand to the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Add immediate value {str(operand).zfill(2)} to the accumulator\n")
    controller.get_processor_instance().accumulator += operand
    controller.get_processor_instance().incrementProgramCounter()

def subI(controller: Controller, operand: int, useDebug: bool = False):
    """Subtract the immediate operand from the accumulator."""
    if useDebug:
        print("-"*100)
        print(f"Description: Subtract immediate value {str(operand).zfill(2)} from the accumulator\n")
    controller.get_processor_instance().accumulator -= operand
    controller.get_processor_instance().incrementProgramCounter()

def modI(controller: Controller, operand: int, useDebug: bool = False):
    """Perform modulo division: accumulator %= operand."""
    if useDebug:
        print("-"*100)
        print(f"Description: Modulo accumulator by immediate value {str(operand).zfill(2)}\n")
    if operand == 0:
        raise ZeroDivisionError("Cannot perform modulo division by zero.")
    controller.get_processor_instance().accumulator %= operand
    controller.get_processor_instance().incrementProgramCounter()

def divI(controller: Controller, operand: int, useDebug: bool = False):
    """Divide the accumulator by the immediate operand."""
    if useDebug:
        print("-"*100)
        print(f"Description: Divide accumulator by immediate value {str(operand).zfill(2)}\n")
    if operand == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    controller.get_processor_instance().accumulator //= operand
    controller.get_processor_instance().incrementProgramCounter()

def mulI(controller: Controller, operand: int, useDebug: bool = False):
    """Multiply the accumulator by the immediate operand."""
    if useDebug:
        print("-"*100)
        print(f"Description: Multiply the accumulator by immediate value {str(operand).zfill(2)}\n")
    controller.get_processor_instance().accumulator *= operand
    controller.get_processor_instance().incrementProgramCounter()

def jump(controller: Controller, address, useDebug: bool = False):
    """Jumps to a specific memory address."""
    if useDebug:
        print("-"*100)
        print(f"Description: Jump to address {str(address).zfill(2)}\n")
    controller.get_processor_instance().programCounter = address

def jump_if_negative(controller: Controller, address, useDebug: bool = False):
    """Jumps to a specific address if the accumulator is less than zero."""
    if useDebug:
        print("-"*100)
        print(f"Description: Jump to address {str(address).zfill(2)} if accumulator is negative\n")
    if controller.get_processor_instance().accumulator < 0:
        controller.get_processor_instance().programCounter = address
    else:
        controller.get_processor_instance().incrementProgramCounter()

def jump_if_zero(controller: Controller, address, useDebug: bool = False):
    """Jumps to a specific address if the accumulator is zero."""
    if useDebug:
        print("-"*100)
        print(f"Description: Jump to address {str(address).zfill(2)} if accumulator is zero\n")
    if controller.get_processor_instance().accumulator == 0:
        controller.get_processor_instance().programCounter = address
    else:
        controller.get_processor_instance().incrementProgramCounter()

def halt(controller: Controller, _, useDebug: bool = False):
    """Halts the program."""
    print()
    if useDebug:
        print("-"*100)
        print("Description: Program halted\n")
    controller.get_processor_instance().dump()
    controller.get_memory_instance().dump()
    exit()

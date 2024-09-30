# operations.py
from Controller import Controller


def read(controller: Controller, address: int):
    """Reads input into the memory address."""
    value = int(input("Enter a number: "))    
    controller.getMemory().store_data(address, value)
    controller.getProcessor().incrementProgramCounter()
    
def write(controller: Controller, address):
    """Writes the content of the memory address to output."""
    value = controller.getMemory().read_data(address)
    print(f"Memory[{address}] = {value}")
    controller.getProcessor().incrementProgramCounter()

def loadM(controller: Controller, address):
    """Loads the value from memory into the accumulator."""
    controller.getProcessor().accumulator = controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()

def store(controller: Controller, address):
    """Stores the accumulator's value into memory."""
    controller.getMemory().store_data(address, controller.getProcessor().accumulator)
    controller.getProcessor().incrementProgramCounter()
    
def loadI(controller: Controller, operand: int):
    """Load an immediate value (00-99) into the accumulator.  
    The 2 digit  operand becomes the immediate value to be loaded in the accumulator."""
    controller.getProcessor().accumulator = operand
    controller.getProcessor().incrementProgramCounter()

def addM(controller: Controller, address):
    """Adds the value from memory to the accumulator."""
    controller.getProcessor().accumulator += controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()

def subM(controller: Controller, address):
    """Subtracts the value from memory from the accumulator."""
    controller.getProcessor().accumulator -= controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()

def divM(controller: Controller, address):
    """Subtracts the value from memory from the accumulator."""
    controller.getProcessor().accumulator /= controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()

def modM(controller: Controller, address):
    """Subtracts the value from memory from the accumulator."""
    controller.getProcessor().accumulator %= controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()

def mulM(controller: Controller, address):
    """Subtracts the value from memory from the accumulator."""
    controller.getProcessor().accumulator *= controller.getMemory().read_data(address)
    controller.getProcessor().incrementProgramCounter()
    
def addI(controller: Controller, operand: int):
    """Add the immediate operand represented by the next 2 digits to the 
    word in the accumulator (leave the result in the accumulator)"""
    controller.getProcessor().accumulator += operand
    controller.getProcessor().incrementProgramCounter()
    
def subI(controller: Controller, operand: int):
    """Subtract the immediate operand from the accumulator."""
    controller.getProcessor().accumulator -= operand
    controller.getProcessor().incrementProgramCounter()

def modI(controller: Controller, operand: int):
    """Perform modulo division: accumulator %= operand."""
    if operand == 0:
        raise ZeroDivisionError("Cannot perform modulo division by zero.")
    controller.getProcessor().accumulator %= operand
    controller.getProcessor().incrementProgramCounter()
    
def divI(controller: Controller, operand: int):
    """Divide the accumulator by the immediate operand (leave the result in the accumulator)"""
    if operand == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    controller.getProcessor().accumulator //= operand
    controller.getProcessor().incrementProgramCounter()

def mulI(controller: Controller, operand: int):
    """Multiply the accumulator by the immediate operand."""
    controller.getProcessor().accumulator *= operand
    controller.getProcessor().incrementProgramCounter()

def jump(controller: Controller, address):
    """Jumps to a specific memory address."""
    controller.getProcessor().programCounter = address
    
def jump_if_negative(controller: Controller, address):
    """Jumps to a specific address if the accumulator is less than zero or negative"""
    if controller.getProcessor().accumulator < 0:
        controller.getProcessor().programCounter = address
    else:
        controller.getProcessor().incrementProgramCounter()

def jump_if_zero(controller: Controller, address):
    """Jumps to a specific address if the accumulator is zero."""
    if controller.getProcessor().accumulator == 0:
        controller.getProcessor().programCounter = address
    else:
        controller.getProcessor().incrementProgramCounter()

def halt(controller: Controller, _):
    """Halts the program."""
    print("Program halted.")
    print()
    controller.getProcessor().dump()
    controller.getMemory().dump()
    exit()

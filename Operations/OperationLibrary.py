from Operations import operations as op
from typing import Callable

class OperationLibrary(object):
    """ Dictionary mapping operation codes to corresponding functions.
        Each key represents an operation code, and the value is the function to execute for that code.
        Keys are integers representing operation codes, and values are functions from the 'op' module.
    """
    OPERATION_CODES_DEFAULT : dict[int, Callable[[], None]] = {
        10: op.read,
        11: op.write,
        12: op.write_acc,
        20: op.loadM,
        21: op.store,
        22: op.loadI,
        30: op.addM,
        31: op.subM,
        32: op.divM,
        33: op.modM,
        34: op.mulM,
        35: op.addI,
        36: op.subI,
        37: op.divI,
        38: op.modI,
        39: op.mulI,
        40: op.jump,
        41: op.jump_if_negative,
        42: op.jump_if_zero,
        43: op.halt   
    }
    # Author: [Leander Lorenz Lubguban]
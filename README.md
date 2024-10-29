# Simpletron Computer using Python 🐍💻

### Author 🤵: Leander Lorenz Lubguban

The Simpletron Computer is a simulated machine designed to execute basic machine-level instructions, similar to early computers. It operates with a custom instruction set and uses memory to store both data and instructions. The Simpletron reads and processes operations like addition, subtraction, input/output, and control flow (e.g., jumps and halts) based on predefined operation codes.

## Example Usage

1. create a file in the folder `codes` and name it `<your_program_name>`, save it as `.sml`

    ```sml
    ; Author: Leander Lorenz B. Lubguban BSCS 3-A
    ; this is an sml program that solves factorial

    Read    n           ;get input (variable n)
    LoadI   1           ;Store to accumulator value 1
    Store   fact        ;Store to variable fact value of accumulator
    Load    n           ;Load to accumulator value of n
    JZ      X := Y      ;jump to level X if accumulator is 0
    Load    fact        ;Load to accumulator value of variable fact
    Mul     n           ;Multiply accumulator value by variable n
    Store   fact        ;Store value of accumulator to variable factorial
    Load    n           ;Load to accumulator value of variable n
    SubI    1           ;Subtract value of accumulator by 1
    Store   n           ;Store to variable n value of accumulator
    JMP     Y           ;Jump to level Y
    Write   fact := X   ;Write to the screen variable factorial
    Halt
    ```

2. run in terminal
    ```bash
    py Simpletron.py <your_program_name>.sml
    ```

#### Optional Debugger

running the program with debugger lets you view how the file is parsed and how the memory and accumulators are updated.

```bash
py Simpletron.py <program_name>.sml -s
```

---

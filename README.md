# Simpletron Computer using Python 🐍💻

### Author 🤵: Leander Lorenz Lubguban

The Simpletron Computer is a simulated machine designed to execute basic machine-level instructions, similar to early computers. It operates with a custom instruction set and uses memory to store both data and instructions. The Simpletron reads and processes operations like addition, subtraction, input/output, and control flow (e.g., jumps and halts) based on predefined operation codes.

## Example Usage (Operation Code Syntax)

1. create a file in the folder `codes` and name it `<your_program_name>`, save it as `.sml`

    ```sml
    0000    1014    ;get input and store to address 14 (variable n)
    0001    2201    ;Store to accumulator value 1
    0002    2115    ;Store to address 15 value of accumulator (variable factorial)
    0003    2014    ;Store to accumulator value of N
    0004    4212    ;Jump to address 12 if accumulator is 0
    0005    2015    ;Load to accumulator value of variable factorial
    0006    3414    ;Multiply accumulator value by variable n
    0007    2115    ;Store value of accumulator to variable factorial
    0008    2014    ;Load to accumulator value of variable n
    0009    3601    ;Subtract value of accumulator by 1
    0010    2114    ;Store to variable N value of accumulator
    0011    4004    ;Jump to address 04
    0012    1115    ;Write to the screen variable factorial
    0013    4300    ;Halt
    0014    0000    ;variable n
    0015    0000    ;variable factorial
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

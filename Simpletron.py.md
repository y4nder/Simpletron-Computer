# Simpletron Emulator Documentation

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Overview](#1-overview)
* [2. Module Imports](#2-module-imports)
* [3. `run(fileAddress: str, useDebug: bool) -> None` Function](#3-runfileaddress-str-usedebug-bool---none-function)
* [4. `main() -> None` Function](#4-main---none-function)
* [5. Entry Point](#5-entry-point)


## 1. Overview

This document provides internal code documentation for the Simpletron emulator.  The emulator executes Simpletron Machine Language (SML) programs. It utilizes a factory pattern for Simpletron instantiation and command-line argument parsing for flexibility.


## 2. Module Imports

The code utilizes the following modules:

| Module             | Description                                      |
|----------------------|--------------------------------------------------|
| `os`                | Provides functions for interacting with the operating system (used for `system("cls")`). |
| `ControllerFiles.ComponentFactory` | Contains the factory class for creating Simpletron instances.  |
| `util.args_util`    | Contains the ArgumentFactory class for parsing command-line arguments. |


## 3. `run(fileAddress: str, useDebug: bool) -> None` Function

This function is responsible for executing the Simpletron program.

**Parameters:**

| Parameter    | Type     | Description                                         |
|---------------|----------|-----------------------------------------------------|
| `fileAddress` | `str`    | The path to the SML file to be executed.           |
| `useDebug`    | `bool`   | A flag indicating whether debug mode should be enabled. |

**Algorithm:**

1. **Simpletron Instantiation:** A Simpletron instance is created using `SimpletronFactory.UseVersion3(fileAddress, useDebug)`. This factory method likely handles loading the SML program from the specified file and initializes the Simpletron with the appropriate settings based on `useDebug`.
2. **Debug Output (Optional):** If `useDebug` is `True`, a separator and "executing file" message are printed to the console.
3. **Program Execution:** The `simpletron.run()` method is called, initiating the execution of the loaded SML program.  The implementation details of this method are not provided in this code snippet but would encompass the fetch-decode-execute cycle of the Simpletron.


## 4. `main() -> None` Function

This function serves as the main entry point for the program.

**Algorithm:**

1. **Argument Parsing:**  `args = ArgumentFactory.DEFAULT_ARGUMENTS()` retrieves command-line arguments using the `ArgumentFactory`.  The details of the `ArgumentFactory` class are not provided.  We assume it parses arguments such as filename and debug flag.
2. **File Extension Validation:** It checks if the filename has the `.sml` extension. If not, a `ValueError` is raised indicating an invalid file extension.
3. **File Path Construction:** The full file path is constructed using `path.join("codes", args.filename)`. This assumes the SML files are located in a "codes" directory.
4. **Debug Flag Assignment:** The debug flag (`useDebug`) is assigned from the parsed arguments (`args.s`).
5. **Program Execution:** The `run()` function is called with the constructed file path and the debug flag, initiating the Simpletron emulation.


## 5. Entry Point

The `if __name__ == "__main__":` block ensures that the `system("cls")` (which clears the console) and `main()` functions are executed only when the script is run directly (not imported as a module).

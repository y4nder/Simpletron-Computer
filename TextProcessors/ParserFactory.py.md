# ParserFactory Class Documentation

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Overview](#1-overview)
* [2. Class `ParserFactory`](#2-class-parserfactory)
    * [2.1 Methods](#21-methods)
        * [2.1.1 `LowLevelParser(debug: bool = False) -> IParser`](#211-lowlevelparserdebug-bool--false---iparser)
        * [2.1.2 `MnemonicParserV1(debug: bool = False) -> IParser`](#212-mnemonicparser1debug-bool--false---iparser)
        * [2.1.3 `MnemonicParserV2(memoryLimit: int = 99, debug: bool = False) -> IParser`](#213-mnemonicparser2memorylimit-int--99-debug-bool--false---iparser)


## 1. Overview

This document details the `ParserFactory` class, responsible for creating instances of different parser classes used for processing Simpletron operation codes.  The factory provides a clean and consistent interface for obtaining parser objects without needing to know the specific implementation details.


## 2. Class `ParserFactory`

The `ParserFactory` class provides methods to create instances of various parser implementations.  It decouples the creation of parsers from their usage, enhancing flexibility and maintainability. The class is designed for directly parsing Simpletron operation codes.


### 2.1 Methods

The `ParserFactory` class offers the following methods for creating parser instances:

| Method Name                     | Description                                                                                                    | Parameters                               | Return Type          |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------|----------------------|
| `LowLevelParser(debug: bool = False)` | Creates and returns an instance of the `LowLevelParser`.                                                      | `debug` (bool, optional): Enables debug mode. Defaults to `False`. | `IParser`             |
| `MnemonicParserV1(debug: bool = False)` | Creates and returns an instance of the `MnemonicParserV1`.                                                    | `debug` (bool, optional): Enables debug mode. Defaults to `False`. | `IParser`             |
| `MnemonicParserV2(memoryLimit: int = 99, debug: bool = False)` | Creates and returns an instance of the `MnemonicParserV2`.  | `memoryLimit` (int, optional): Sets the memory limit. Defaults to 99. <br> `debug` (bool, optional): Enables debug mode. Defaults to `False`. | `IParser`             |


#### 2.1.1 `LowLevelParser(debug: bool = False) -> IParser`

This method simply instantiates and returns a `LowLevelParser` object.  The `debug` parameter is passed directly to the `LowLevelParser` constructor.  No specific algorithm is implemented within this factory method; its role is purely instantiation.

#### 2.1.2 `MnemonicParserV1(debug: bool = False) -> IParser`

This method instantiates and returns a `MnemonicParserV1` object. Similar to `LowLevelParser`, the `debug` parameter is passed directly to the constructor of `MnemonicParserV1`.  The internal workings of `MnemonicParserV1` are not detailed here, but can be found in its own documentation.


#### 2.1.3 `MnemonicParserV2(memoryLimit: int = 99, debug: bool = False) -> IParser`

This method instantiates and returns a `MnemonicParserV2` object.  The `memoryLimit` and `debug` parameters are passed directly to the `MnemonicParserV2` constructor. The `MnemonicParserV2` likely employs a different parsing algorithm than `MnemonicParserV1`, potentially optimized for memory usage based on the provided `memoryLimit`.  Refer to the `MnemonicParserV2` documentation for algorithm details.

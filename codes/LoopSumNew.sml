LoadI   03
Store   A
LoadI   00
Read    B := Y
Add     B
Store   B
Load    A
SubI    01
JZ      X
Store   A
Load    B
JMP     Y
Write   B := X
Halt    
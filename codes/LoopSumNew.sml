LoadI   3
Store   A
LoadI   00

Section : loop
Read    B 
Add     B
Store   B
Load    A
SubI    01
JZ      display
Store   A
Load    B
JMP     loop

Section : display
Write   B 
Halt    
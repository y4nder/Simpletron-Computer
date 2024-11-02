LoadI   10          ; init accumulator with limit 10
Store   limit       ; store accumulator to variable A
LoadI   0           ; reset accumulator to 0
Read    input := a  ; user input
Sub     input       ; subtract accumulator value with input
JL      x           ; jump to level x if accumulator is less than zero  
JMP     y           ; jump to level y if accumulator
Load    input := x  ; load input to accumulator
Store   temp        ; Store value of accumulator to variable temp 
Load    limit := y  ; load the limit to the accumulator
SubI    1           ; decrement value of accumulator
JZ      z           ; jump to level z if accumulator is zero
Store   limit       ; return variable limit to its address
Load    temp        ; load temp to accumulator
JMP     a           ; loop
Write   temp := z   ; display temp
Halt
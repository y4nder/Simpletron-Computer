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



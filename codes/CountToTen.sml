LoadI   5
Store   A

Store   B

Section : loop
Sub     B
Store   C
Write   C
Load    B
SubI    1
JL      end
JMP     loop

Section : end
Halt

; 20 = A 
; 21 = B
; 22 = C
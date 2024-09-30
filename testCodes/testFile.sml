; this program accepts 2 inputs and adds both the inputs 

00	1007		; get input and store to address 07
01	1008		; get input and store to address 08
02	2007		; load address 07 to accumulator
03	3008		; add address 08 to accumulator
04	2109		; store value in accumulator to address 09
05	1109		; write to the screen address 09
06	4300		; Halt
07	0000		; Variable A
08	0000		; Variable B	
09	0000		; Result C
; this program accepts 2 inputs and adds both the inputs 

00	1008		; get input and store to address 08
01	1009		; get input and store to address 09
02	2008		; load address 08 to accumulator
03	3009		; add address 09 to accumulator
04	2110		; store value in accumulator to address 10
05	1110		; write to the screen address 10
06	1200		; write value to the screen value of accumulator
07	4300		; Halt
08	0000		; Variable A
09	0000		; Variable B	
10	0000		; Result C
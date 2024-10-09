read   14    ;get input and store to address 14 (variable n)
loadI  01    ;Store to accumulator value 1 	
store  15    ;Store to address 15 value of accumulator (variable factorial)	
load   14    ;Store to accumulator value of N	
jz     12    ;Jump to address 12 if accumulator is 0	
load   15    ;Load to accumulator value of variable factorial	
mul    14    ;Multiply accumulator value by variable n	
store  15    ;Store value of accumulator to variable factorial	
load   14    ;Load to accumulator value of variable n	
subI   01    ;Subtract value of accumulator by 1	
store  14    ;Store to variable N value of accumulator	
jmp    04    ;Jump to address 04	
write  15    ;Write to the screen variable factorial	
halt   00    	

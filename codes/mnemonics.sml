00  read    08    ; get input and store to address 08 (Variable A)
01  read    09    ; get input and store to address 09 (Variable B)
02  load    08    ; load address 08 into accumulator (Variable A)
03  add     09    ; add address 09 (Variable B) to accumulator
04  store   10    ; store the value in accumulator to address 10 (Result C)
05  write   10    ; write the value from address 10 (Result C) to the screen
06  writeA  00    ; write the value in the accumulator to the screen
07  halt    00    ; Halt the program
08  data    00    ; Variable A
09  data    00    ; Variable B    
10  data    00    ; Result C
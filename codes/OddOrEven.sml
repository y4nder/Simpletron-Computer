; Write an SML program that will read a number and will
; output 1 if the number is an even number, will output 0 otherwise.

read 11     ; rad input and store to address 11
load 11     ; load to accumulator value of address 11
modI 02     ; perform immediate module to accumulator value
jz 06       ; jump to address 8 if accumulator value is 0
loadI 00    ; load immediate value 0 to accumulator
jmp 07      ; jump to address 7 
loadI 01    ; load immediate value 1 to accumulator
store 12    ; store accumulator value to address 12
write 12    ; write value of address 12
halt 00





loadI 10    ; init accumulator with limit 10
store 20    ; store to address 20 the value of the accumulator
loadI 00    ; reset the value of the accumulator to zero
read 21     ; get user input and store to address 21
sub 21      ; subtract accumulator with value of address 21
jl 07       ; jump to address 07 if accumulator is negative
jmp 09      ; jump to address 09 if accumulator is not negative
load 21     ; load to accumulator value of address 21
store 22    ; store to address 22 value of accumulator
load 20     ; load value of address 20 to the accumulator
subI 01     ; subtract from the accumulator with 1
jz 15       ; jump to address 15 if accumulator is zero
store 20    ; store back to address 20 value of accumulator
load 22     ; store value of address 22 to accumulator
jmp 03      ; loop back to input address 03
write 22    ; write value of address 22
halt 00 

; Write a program that will read 10 numbers (using a loop) and will output the largest of the 10 numbers.
; this is a comment

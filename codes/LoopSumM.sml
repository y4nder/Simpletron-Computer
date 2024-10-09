; Write a program that will read 10 numbers (using a loop) and will output the sum of the numbers.

loadI   10  ; load immediate 10 to accumulator
store   20  ; store value of accumulator to address 20
loadI   00  ; reset accumulator to 0
read    21  ; input and then store to address 21
add     21  ; add value of address 21 to accumulator
store   21  ; store to address 21 value of accumulator
load    20  ; load the counter variable to the accumulator
subI    01  ; decrement value of accumulator
jz      12  ; jump to address 12 if accumulator is 0
store   20  ; store decremented value back to address 20
load    21  ; load value of address 21 to accumulator
jmp     03  ; jump to address 3 
write   21  ; write to screen value of 21
halt    00
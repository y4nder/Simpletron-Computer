; Write a program that will read 10 numbers (using a loop) and will output the largest of the 10 numbers.
; this is a comment

01  2120    ; store to address 20 the value of the accumulator
02  2200    ; reset the value of the accumulator to zero
03  1021    ; get user input and store to address 21
04  3121    ; subtract accumulator with value of address 21
05  4107    ; jump to address 07 if accumulator is negative
06  4009    ; jump to address 09 if accumulator is not negative
07  2021    ; load to accumulator value of address 21
08  2122    ; store to address 22 value of accumulator
09  2020    ; load value of address 20 to the accumulator
10  3601    ; subtract from the accumulator with 1
11  4215    ; jump to address 15 if accumulator is zero
12  2120    ; store back to address 20 value of accumulator
13  2022    ; store value of address 22 to accumulator
14  4003    ; loop back to input address 03
15  1122    ; write value of address 22
16  4300
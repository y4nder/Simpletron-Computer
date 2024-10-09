; Author: Leander Lubguban BSCS -3 

; Write a program that will read 10 numbers (using a loop) 
; and will output the largest of the 10 numbers.

loadI   10    ; test inline comment
store   20    
loadI   00    
read    21     
sub     21      
jl      07       
jmp     09      
load    21     
store   22    
load    20     
subI    01
jz      15  
store   20  
load    22     
jmp     03      
write   22   
halt    00 
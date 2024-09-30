0000    1014    ;get input and store to address 14 (variable n)
0001    2201    ;Store to accumulator value 1 
0002    2115    ;Store to address 15 value of accumulator (variable factorial)
0003    2014    ;Store to accumulator value of N
0004    4212    ;Jump to address 12 if accumulator is 0
0005    2015    ;Load to accumulator value of variable factorial
0006    3414    ;Multiply accumulator value by variable n
0007    2115    ;Store value of accumulator to variable factorial
0008    2014    ;Load to accumulator value of variable n
0009    3601    ;Subtract value of accumulator by 1
0010    2114    ;Store to variable N value of accumulator
0011    4004    ;Jump to address 04
0012    1115    ;Write to the screen variable factorial
0013    4300    ;Halt
0014    0000    ;variable n
0015    0000    ;variable factorial
00    read   14    	;get input and store to address 14 (variable n)
01    loadI  01    	
02    store  15    	
03    load   14    	
04    jz     12    	
05    load   15    	
06    mul    14    	
07    store  15    	
08    load   14    	
09    subI   01    	
10    store  14    	
11    jmp    04    	
12    write  15    	
13    halt   00    	
14    data   00    	
15    data   00    	
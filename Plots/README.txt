d1: Normal operation for 5 min
d2: false data injection attack for 5 min, toggle motor status value
d3: TCP SYN flood PLC1/* + MitM/DoS (    (i)   PLC1/PLC3 
    (ii)  PLC1/PLC2 
    (iii) PLC1/*)
    Duration: 10 min
d4: Duration: 15 min
    change readings to constant value: 
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2
    change readings to random values within the limits: 
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2   
d5: Duration: 15 min
    change readings to scaled values (+ve scaling): 
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2
    add random positive value to readings:
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2
d6: Duration:15 min
    change readings to scaled values (-ve scaling): 
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2
    add random negative value to readings:
    (i)   only PLC3 
    (ii)  only PLC2
    (iii) both PLC3&PLC2

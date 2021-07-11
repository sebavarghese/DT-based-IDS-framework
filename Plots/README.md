This folder contains two Jupyter notebooks, named Dataset and Plots
1) **Dataset.ipynb**: For plotting distribution of class labels in generated dataset. 
(Figure 5.1 in report made using this code)
2) **Plots.ipynb**: For plotting effect of modelled attacks on 4 process measurements - tank_liquidlevel, bottle_liquidlevel, flowlevel, motor_status.
Use the csv files corresponding to the below listed attack scenarios to generate plots.
d1: Normal operation for 5 min

d2: false data injection attack for 5 min, toggle motor status value

d3: TCP SYN flood PLC1/* + MitM/DoS ((i)PLC1/PLC3  (ii)PLC1/PLC2 (iii)PLC1/*)
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

**Note:** Each folder contains 4 plots (tl.png for tank_liquidlevel, bl.png for bottle_liquidlevel, fl.png for flowlevel, ms.png for motor_status.

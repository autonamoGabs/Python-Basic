def master_yoda(x):
    l = x.split()
    pon = -1
    for k in range(len(l)//2 + 1):
        j = l[k]
        l[k] = l[pon]
        l[pon] = j 
        pon -= 1
    
    print(" ".join(l))

    

master_yoda('I am home') 
master_yoda('No! Try not. Do. Or do not. There is no try.')

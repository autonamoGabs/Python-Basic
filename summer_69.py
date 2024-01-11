def summer_69(x):
    k = 0
    s = 0
    while k < len(x):
        if x[k] == 6:
            for m in range(k+1,len(x)):
                if x[m] == 9:
                    k = m+1
                    continue
        else:
            s += x[k]
            k += 1

    print(s)
    

    


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11]) 

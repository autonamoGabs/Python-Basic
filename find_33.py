def has_33(x):
    con = False
    if len(x) == 2:
        if (x[0] == 3 and x[1] == 3):
            con = True

    else:
        for k in range(1,len(x)-1):
            if (x[k] == 3 and x[k+1] == 3) or (x[k] == 3 and x[k-1] == 3):
                con = True
                break
    print(con)

    


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
has_33([1,1,1,1,1,1,3,3,1,1,1,1])
has_33([3,3])

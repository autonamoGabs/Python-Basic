def unique_list(x):
    l = []
    for k in x:
        if k not in l:
            l.append(k)
    print(l)


                
# Check
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

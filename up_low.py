import string

def up_low(s):
    l = list(s)
    ma,mi = 0,0
    ama = list(string.ascii_uppercase)
    ami = list(string.ascii_lowercase)

    for k in l:
        if k in ama:
            ma+=1
        if k in ami:
            mi+=1
    print(f"Original String :  {s}")
    print(f"No. of Upper case characters :  {ma}")
    print(f"No. of Lower case Characters : {mi} ")


                
# Check
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)





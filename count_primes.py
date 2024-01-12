def count_primes(k):
    s = 1
    for x in range(3,k+1):
        y = x-1
        while y != 1:
            if x % y == 0:
                y = 1
            else:
                y = y - 1
                if y == 1:
                    s += 1
    print(s)
                
# Check
count_primes(100)
count_primes(10)
count_primes(1000)

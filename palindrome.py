def palindrome(s):
    s = s.replace(" ","")
    if s == s[::-1]:
        print(True)
    else:
        print(False)


palindrome('helleh')
palindrome('madam')
palindrome('kayak')
palindrome('racecar')
palindrome('nurses run')

import string

def ispangram(x):
    a = list(string.ascii_lowercase)
    x = x.lower()
    l2 = []
    for k in x:
        if k not in l2 and k in a:
            l2.append(k)
    if len(l2) == len(a):
        print(True)
    else:
        print(False)

ispangram("The quick brown fox jumps over the lazy dog")
ispangram("Mr Jock, TV quiz PhD, bags few lynx.")
ispangram("Pack my box with five dozen liquor jugs.")
ispangram("THE JANITOR LION RULES")
ispangram("CWM FJORD BANK glyphs vext quiz.")
ispangram("Jinxed wizards pluck ivy from the big quilt.")
ispangram("Sphinx of black quartz, judge my vow.")

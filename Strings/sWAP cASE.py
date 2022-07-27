def swap_case(s):
    res=''
    for  c in s:
        new = c
        if c.islower() :
            new = c.upper()
        elif c.isupper():
            new = c.lower()
        res= res + new
    return res


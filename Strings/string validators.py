if __name__ == '__main__':
    s = input()
    b1 = b2 = b3 = b4 = b5 = False
    for c in s:
        if c.isalnum():
            b1 = True
            if c.isdigit():
                b3 = True
            else:
                b2 = True
                if c.islower():
                    b4 = True
                else:
                    b5 = True

    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)



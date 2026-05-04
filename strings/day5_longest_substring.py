def substr(s):
    p = []
    max_len = 0
    for ch in s:
        if ch not in p:
            p.append(ch)
        else:
            while ch in p:
                p.pop(0)
            p.append(ch)
        if len(p) > max_len:
            max_len = len(p)

    return max_len
s = input("enter long str: ")
print("longest substr:", substr(s))

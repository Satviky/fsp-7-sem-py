def sn(ns):
    res=0
    for n in ns:
        res = res^n
    return res

print(sn([11, 33, 22, 44, 33, 11, 22]))
print(sn([10, 20, 40, 30, 20, 10, 60, 60, 30]))
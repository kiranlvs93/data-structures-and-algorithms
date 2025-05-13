def power(a,b):
    if a==1:
        return 1
    if b == 0:
        return 1
    return a*power(a, b-1)

# print(power(2,10))


def fast_power(a, b):
    if a == 1:
        return 1
    if b==0:
        return 1
    p = fast_power(a, b//2)
    if b%2==0:
        return p*p
    else:
        return a*p*p

print(fast_power(2,4))
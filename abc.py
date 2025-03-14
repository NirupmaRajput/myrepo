def sun_dig(n,r):
    if n < 1:
        return r
    return sun_dig(n//10,r+(n%10))

print(sun_dig(0,0))
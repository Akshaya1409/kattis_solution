def reach_gas(c,x,m,menu):
    for s,fe in menu:
        if c/2 -  m/s * x >= m/fe:
            return f'YES {s}'
    return 'NO'


print(reach_gas(*tuple(map(float, input().split())),reversed([(lambda a,b: (int(a), float(b)))(*input().split()) for _ in range(6)])))

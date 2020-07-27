a, b = [float(x) for x in input().split()]
if b == 1:
    if a == 0: print('ALL GOOD')
    else: print('IMPOSSIBLE')
else:
    print(-a/(b-1))

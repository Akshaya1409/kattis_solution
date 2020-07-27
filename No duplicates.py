def fun_repeat(a):
    for i in a:
        if a.count(i)>1:
            return "no"
    return "yes"


a = input().split()
print(fun_repeat(a))

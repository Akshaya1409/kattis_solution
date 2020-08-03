flag = False
n = int(input())
count = 1
for i in range(n):
    x = int(input())
    for j in range(next, x):
        print(j)
        flag = True
    count = x + 1

if not flag:
    print('good job')

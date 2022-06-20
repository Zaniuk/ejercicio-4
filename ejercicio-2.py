print('Ingrese el numero inicial')
n_start = int(input())
print('Ingrese el numero final')
n_end = int(input())
res = []
for n in range(n_start, n_end):
    if(n % 2 != 0):
        res.append(n)
print(res)
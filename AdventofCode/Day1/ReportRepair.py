with open('input.txt', mode='r') as ip:
    y = ip.readlines()

thisset = set()
i = 0

x = [int(i.strip()) for i in y]

while i < len(x):
    j = 0
    while j < len(x):
        if (j != i) & (2020 == (x[i] + x[j])):
            thisset.add(x[i])
            thisset.add(x[j])
            print(f"{x[i]},{x[j]}")
        j += 1
    i += 1

result = 1
for i in thisset:
    result *= i

print(result)

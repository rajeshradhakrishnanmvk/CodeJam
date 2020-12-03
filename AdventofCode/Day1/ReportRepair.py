with open('input.txt', mode='r') as ip:
    expense_report = ip.readlines()

entries = set()
i = 0

x = [int(i.strip()) for i in y]

while i < len(x):
    j = 0
    while j < len(x):
        if (j != i) & (2020 == (x[i] + x[j])):
            entries.add(x[i])
            entries.add(x[j])
            # print(f"{x[i]},{x[j]}")
        j += 1
    i += 1

onestar = 1
for i in entries:
    onestar *= i

print(onestar)

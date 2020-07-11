
str1 = "103    123 4444 99 2000"
str1 = list(str1.split())

for i in range(0, len(str1)):
    str1[i] = int(str1[i])

weights = []
sum = 0
for x in str1:
    for y in str(x):
        sum += int(y)
    weights.append(sum)
    sum = 0

for i in range(0, len(str1)):
    str1[i] = str(str1[i])


print(str1)
print(weights)

Z = [x for _,x in sorted(zip(weights,str1))]
Z = " ".join(Z)

print(Z)

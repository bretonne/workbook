#Exercise 74: Multiplication Table

line = "\t"

for i in range(1, 11):
    line += str(i) + "\t"
print(line)
for j in range(1,11):
    line = str(j) + "\t"
    for i in range(1, 11):
        line += str(i*j) + "\t"
    print(line)

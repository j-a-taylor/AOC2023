input_file = open(r"input.txt","r")

cali_values = input_file.readlines()
x = 0

for line in cali_values:
    digits = []
    for i in line:
        if i.isdigit():
            digits.append(i)
    y = digits[0] + digits[-1]
    x = x + int(y)
print(x)

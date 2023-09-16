import re
# x = open("./regex_sum_42.txt", "r")
x = open('./regex_sum_1530356.txt', 'r')
count = 0
y = []
for i in x:
    y += re.findall('[0-9]+', i)

print(y)
for i in y:
    count += int(i)

print(count)


import re

str = input("Введіть рядок: ")


num = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)

num = [int(i) for i in num]

print("Рядок без чисел:\n", str, sep='')
print("Масив чисел з рядка:\n", num, sep='')


def function(str):
    str, result = str.title(), ""
    for word in str.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print("\nЗаміна першої і останньої букви у кожному слові на великі:\n", function(str), sep='')

max_num = max(num)
index = num.index(max_num)
print("\nМаксимальне число у масиві:", max_num)
vals = []

for i in range(len(num)):
    if i != index:
        temp = num[i] ** i
        vals.insert(i, temp)
print("Масив чисел піднесених до степеня:\n", vals, sep='')
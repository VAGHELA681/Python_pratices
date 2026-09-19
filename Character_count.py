text = "hello"

count = {}

for i in text:
    count[i] = count.get(i, 0) + 1

print(count)

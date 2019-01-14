hello = "hello"
hello2 = ""
for i in range(len(hello), 0, -1):
    hello2 += hello[i-1: i]

print(hello2)
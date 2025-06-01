

f = open("memo.txt", "w")
f.write("3\n")
f.close()
f = open("memo.txt", "r")
content = f.read()
a = int(content)
f = open("memo.txt", "w")
f.write("4\n")
f.close()
f = open("memo.txt", "r")
content = f.read()
b = int(content)
print(a*b)
f.close()


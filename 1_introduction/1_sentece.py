a="Hello World"

f = open("sentence.txt","x")
f.write(a)
f.close()

f = open("sentence.txt","r")
print(f.read())

f = open('example.txt', 'r')
contents = f.read()
print(contents)

print('<--------------------->\n')

f = open('example.txt')
for line in f:
    print(line)
    
print('<--------------------->\n')

f = open('example.txt', 'r')
print(f.readline())
    
print('<--------------------->\n')

f = open('example.txt', 'r')
print(f.readlines())

print('<--------------------->\n')

f = open('example.txt', 'r')
while f:
    line = f.readline()
    print(line)
    if line == "":
        break

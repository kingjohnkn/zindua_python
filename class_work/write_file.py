f = open('example.txt', 'w')
f.write('Hello World')
f = open('example.txt', 'r')
print(f.read())
f.close()

print('<--------------------->\n')

lines = ['Hello World!\n', 'This is a test.']
f = open('example2.txt', 'w')
f.writelines(lines)
f = open('example2.txt', 'r')
print(f.read())
f.close()

print('<--------------------->\n')
with open('example3.txt', 'r') as f:
    contents = f.read()

print(contents)
list=[1,56,73,53,98,33,75,35,65,43,143]

x=bytearray(list)
print(type(x))

print("all values before modification")
for i in x:
    print(i,end=' ')

x[3]=88
x[5]=32

print('\nall values after modification')
for i in x:
    print(i,end=' ')

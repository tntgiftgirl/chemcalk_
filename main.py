print('Enter Number of elements')
n = int(input())
c = 0
m = {}
a=[]
f = open('elements.txt', 'r')

for i in f:
    s=i.split(" ")
    m[s[0]]=float (s[2])

for i in range(n):
    print('Enter Element N=' + str(i))
    e = input()
    ma = m.get(e, None)
    print(ma)
    if ma == None:
        print('Error 404')
        print('Enter mass M=' + str(i))
        ma = int(input())
        m[e] = ma
    print('Enter Element Number of Core N=' + str(i))
    na = int(input())

    c = c + ma * na
    a.append(ma * na)
for i in range(n):
    s = a[i] / c
    print('Element N=' + str(i) + '|' + str(s) + str(ma))
print(c)
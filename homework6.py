s1 = 'www.my_site.com#about'
print (s1.replace('#','/'))
print ('=======================')

a = 'run'
b = 'work'
c = 'sing'
d = 'ing'
print (a+d+',', b+d+',', c+d)
print ('========================')

name = 'Ivanou Ivan'
n1 = name.split()
# print(n1)
n2 = (n1[::-1])
print(' '.join(n2))
print('========================')

name = ' My name is Yuliya '
print(name.lstrip())
print(name.rstrip())
print('========================')

city = 'pARiS'
print(city.capitalize())
print('========================')

str1 = 'Robin Singh'
str2 = 'I love arrays they are my favorite'
print(str1.split())
print(str2.split())
print('========================')

list1 = ['Robin', 'Singh']
w = 'Welcome'
air = 'airport'
j1 = ' '.join(list1)
print(f'Hello {j1}! {w} to {air}')
print('========================')

list2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
j2 = ' '.join(list2)
print(j2)
print('========================')

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3[3] = 12
del list3[6]
print(list3)
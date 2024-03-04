my_set = {122,234,453,377,4546}
print(my_set)
my_set.add(345)
print(my_set)
my_set.update([123,57,8659,576])
print(my_set)
my_set2 =  my_set.copy()
print(len(my_set))
my_set.discard(57)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2 ))
print(sum(my_set2)/len(my_set2))
names = {'Korah', 'Eng', 'Bowlin', 'Mako'}
if "Kinuthia"in names:
    print("Kinuthia is present at school")
else:
    print('Kinuthia is absent')

Parents = {'Andre 3000', 'Jpeg Mafia', 'Scott Mescudi', 'Isaiah Rashid', 'Sampha'}
one_parent = 'Sampha'
if one_parent in Parents:
    output = one_parent
    print(output)

set_1 = {123,234,468,20.24,345}
valued = 4
if valued in set_1:
    output = valued
    print(output)
else:
    print('null')
valued_1 = 12.23
if valued_1 in set_1:
    display = valued_1
    print(valued_1)
else:
    print('void')

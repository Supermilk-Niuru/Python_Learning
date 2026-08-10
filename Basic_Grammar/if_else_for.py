str1 = 'gun'
str2 = 'cuo'
str3 = f'{str1},{str2}'
print(str3)

a = 1/4
print(a)

b = 0
if b>9:
    print('kkk')
elif b>0 and b<9:
    print(999)
else:
    print(111)
print(int(a))

set_m = {'jj','kk','jj','mm'}
print(set_m)

list_v = [1,2,3]
cut_v = list_v[1:]
print(cut_v[0])
cut_v[1] = 'a'
print(cut_v)

schools = {888:'1',999:'2',000:'3'}
for school in schools.keys():
    print(school)
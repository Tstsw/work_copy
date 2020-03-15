import re
filename = 'baby1990.html'
year = re.search(r'[0-9]{4}', filename).group()
print(re.search(r'[0-9]{4}', filename))
print(year)
file = 'C:\Users\asus\Desktop\files\baby1990.html'
f = open(filename)
cont = f.read()
f.close()
dic = []
male_dict = []
ll_dict = re.findall('<tr align="right"><td>([0-9]+)</td><td>([A-Z][a-z]+)</td><td>([A-Z][a-z]+)', cont)
for name in all_dict:
    male_dict.append(name[1] + '  ' + name[0])
    dic.append(name[2] + '  ' + name[0])
dic.sort()
male_dict.sort()
male_dict.insert(0, '-' * 30 + 'Male' + '-' * 30)
dic.insert(0, year)
dic.insert(1, '-' * 30 + 'Female' + '-' * 30)
dic.extend(male_dict)
#python学籍管理系统开发
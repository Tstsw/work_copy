import re
import sys
def extract_names(filename):
  f = open(filename, 'r')  # Open and read the file.
  text = f.read()
  why = []
  if re.search(r'[0-9]{4}', filename):
    year = re.search(r'[0-9]{4}', filename).group()
  else:
    sys.exit(1)
  # print(list)
  tuples = []
  # Extract all the data tuples with a findall()
  # each tuple is: (rank, male-name, female-name)
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text) #extract rank、male_name、female_name
  feamlenames_rank = {}
  malenames_rank = {}
  for rank in tuples:#此处分别保存男女姓名
      malenames_rank[rank[1]] = rank[0]
      feamlenames_rank[rank[2]] = rank[0]

  malenames_rank=sorted(malenames_rank.items(), key=lambda x: x[0])
  feamlenames_rank = sorted(feamlenames_rank.items(), key=lambda x: x[0])
  #print(malenames_rank)
  why.insert(0,year)
  why.insert(1,'***********---male---**********')
  why.extend(malenames_rank)
  why.insert(len(malenames_rank)+2,'***********---female---**********')
  why.extend((feamlenames_rank))
  return why

names = extract_names('C:/Users/asus/Desktop/files/baby1990.html')
print(names)
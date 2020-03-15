import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

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


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
    [print(name) for name in names]

    # Make text out of the whole list
    #text = '\n'.join(names)
    #for name in names:
      #text = '\n'.join(name)

    if summary:
      with open(filename + '.txt', 'w') as fp:
        for name in names:
          fp.write(str(name)+'\n')
    else:
      print('error')
  
if __name__ == '__main__':
  main()


#D:/Users/asus/PycharmProjects/homework/venv/Lib/work/wbabynames.py --summaryfile  C:/Users/asus/Desktop/files/baby1990.html
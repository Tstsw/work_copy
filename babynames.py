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
  #from filename extraxt Particular year
  if re.search(r'[0-9]{4}', filename):
    year = re.search(r'[0-9]{4}', filename).group()
  else:
    sys.exit(1)
  f = open(filename)
  cont = f.read()
  f.close()
  dic = []
  male_dict = []
  all_dict = re.findall('<tr align="right"><td>([0-9]+)</td><td>([A-Z][a-z]+)</td><td>([A-Z][a-z]+)', cont)
  for name in all_dict:
    male_dict.append(name[1] + '  ' + name[0])
    dic.append(name[2] + '  ' + name[0])
  dic.sort()
  male_dict.sort()
  male_dict.insert(0, '-' * 30 + 'Male' + '-' * 30)
  dic.insert(0, year)
  dic.insert(1, '-' * 30 + 'Female' + '-' * 30)
  dic.extend(male_dict)
  return dic


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  for arg in args:
    names = extract_names(arg)
    print('\n'.join(names))
    if summary:
      sf = open(names[0] + '.txt', 'w')
      sf.write('\n'.join(names) + '\n')

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()

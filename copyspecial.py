#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
#import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):  #返回给定目录中特殊文件的绝对路径的列表
  pattern = "[__].*$"
  dir_path = []
  for (dirpath, dirnames, filenames) in os.walk(dir):
    for filename in filenames:
      if re.search(pattern, filename):
          print(filename)
          #print(re.search(pattern, filename))
          dir_path += [os.path.join(dirpath, filename)]
  return dir_path

def copy_to(paths, dir):  # 将这些文件复制到给定目录中
  isExists = os.path.exists(paths)
  # 判断结果
  if not isExists:
    os.makedirs(paths)
    print(paths + ' 目录创建成功')
  else:
    print(paths + ' 目录已存在')
  # 获取当前路径下的文件名，返回List
  fileNames = os.listdir(dir)
  for file in fileNames:
    oldfile = dir + '\\' + file
    newFile = paths + '\\' + file
    #print(newFile)
    shutil.copyfile(oldfile, newFile)
  print('复制成功')

def zip_to(zippath,paths):  #给出路径列表，将这些文件压缩到给定的zipfile中
  format = 'zip'
  shutil.make_archive(paths, format, zippath)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[2]
  #del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[2]
  if args[0] == '--get_special_paths':
    get_special_paths(args[1])

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  specials = args[1]
  if todir:
    copy_to(specials, todir)
  if tozip:
    zip_to(specials, tozip)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
#D:\Users\asus\PycharmProjects\homework\venv\Lib\work\copyspecial.py --get_special_paths D:\Users\asus\PycharmProjects\homework\venv\Lib\work\filetest
#D:\Users\asus\PycharmProjects\homework\venv\Lib\work\copyspecial.py --tozip D:\Users\asus\PycharmProjects\homework\venv\Lib\work\filetest2 D:\Users\asus\PycharmProjects\homework\venv\Lib\work\ziptest
#D:\Users\asus\PycharmProjects\homework\venv\Lib\work\copyspecial.py --todir D:\Users\asus\PycharmProjects\homework\venv\Lib\work\filetest3 D:\Users\asus\PycharmProjects\homework\venv\Lib\work\filetest2
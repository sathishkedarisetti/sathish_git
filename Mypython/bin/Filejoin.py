import sys
import os
import os.path
import re
from collections import OrderedDict


odict=OrderedDict()

def Is_file_exists(filenm):
  print os.path.isfile(filenm)
  if os.path.isfile(filenm):
    return 0
  else:
    print "Invalid File name Entered"
    return 1

def Validate_fileorder(odict,forder):
  print odict
  try:
     userInput = int(forder)
  except ValueError:
     print("Not an integer!")
     return 1
  else:
    print forder
    print userInput
    if userInput > 0:
      if userInput in odict:
        print "Entered File order is already existing please choose another order"
        return 1
      else:
        return 0
    else:
      print "Entered -ve integer please enter integer more than 0"
      return 1

def get_input():
  iterator =''
  orddict = OrderedDict()
  while iterator != "Y":
    filename = raw_input("Please enter the file name:" )
    fileorder = raw_input(" Please enter the file order:")
    if (Is_file_exists(filename)==0 and Validate_fileorder(orddict,fileorder)==0):
      orddict[fileorder]=filename
    else:
      print "Entered Filename/File order are not correct"
    print orddict
    iterator = raw_input( " Are you done with list? press Y else press any other key:")
  return orddict

def main():
  args = get_input()
  for keys in sorted(args.keys()):
    print keys,args[keys]
if __name__ == "__main__":
  main()

import os
import sys


def main():
  myvars = {}
  infile=raw_input("Enter the file name:")
  
  field_nm=raw_input("Enter the field name:")

  with open(infile) as myfile:
    for line in myfile:
        name, val = line.partition(":")[::2]
        myvars[name.strip()] =val

  print myvars[field_nm] 

if __name__=="__main__":
  main()


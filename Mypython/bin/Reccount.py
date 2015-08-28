#import pandas 
import os
import sys

def Get_file_name():
  return raw_input("Please enter the input filename:" )

def Check_file(filenm):
  if os.path.isfile(filenm):
    return 0
  else:
    print "Invalid File name Entered"
    return 1
 

def Check_rec_count(filenm):
  retstatus= Check_file(filenm)
  if retstatus==0:
    reccnt=sum(1 for line in open(filenm))
    print "record count: "
    print reccnt

def main():
  filenm=Get_file_name()
  print filenm
  reccnt=Check_rec_count(filenm)

if __name__ == "__main__" :
  main()

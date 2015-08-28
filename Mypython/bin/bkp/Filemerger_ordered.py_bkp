from collections import OrderedDict
from optparse import OptionParser
from argparse import ArgumentParser
import os
import pandas

def Get_Args():
  arg_parser=ArgumentParser(description='please enter the input files to be joined ')
  arg_parser.add_argument('--file1',default="/home/sathish/Mypython/DATA/INPUT/file1.csv")
  arg_parser.add_argument('--file1order',default="1")
  arg_parser.add_argument('--file2',default="/home/sathish/Mypython/DATA/INPUT/file2.csv")
  arg_parser.add_argument('--file2order',default="2")
  arg_parser.add_argument('--file3',default="/home/sathish/Mypython/DATA/INPUT/file3.csv")
  arg_parser.add_argument('--file3order',default="3")
  arg_parser.add_argument('--output_file',default="/home/sathish/Mypython/DATA/OUTPUT/ordered_filemerge_output.csv")
  options=arg_parser.parse_args()
  return options
#  Print_Args(options.file1,options.file1order,options.file2,options.file2order,options.file3,options.file3order,options.output_file)

def main():
  opt=Get_Args()
  print opt
  orddict = OrderedDict()
  d = { file
  csv1 = pandas.read_csv(opt.file1)
  csv2 = pandas.read_csv(opt.file2)
  merged = csv1.merge(csv2, on='id')
  merged.to_csv(opt.output_file, index=False)
if __name__ == "__main__":
  main()

import pandas
from argparse import ArgumentParser

def main():
 arg_parser=ArgumentParser(description=' please enter the input files to be joined ')
 arg_parser.add_argument('--file1',default="/home/sathish/Mypython/DATA/INPUT/file1.csv")
 arg_parser.add_argument('--file2',default="/home/sathish/Mypython/DATA/INPUT/file2.csv")
 arg_parser.add_argument('--output_file',default="/home/sathish/Mypython/DATA/OUTPUT/filejoin.csv")
 arg_parser.add_argument('--join_key1',default="id")
 arg_parser.add_argument('--join_key2',default="id2")
 options=arg_parser.parse_args()
# Print_Args(options.file1,options.file2,options.output_file)
 file1=options.file1
 file2=options.file2
 output_file=options.output_file
 join_key1=options.join_key1
 join_key2=options.join_key2
 csv1 = pandas.read_csv(file1)
 csv2 = pandas.read_csv(file2)
 merged = csv1.merge(csv2, on=(join_key1,join_key2))
 merged.to_csv(output_file, index=False)

if __name__ == "__main__":
 main()

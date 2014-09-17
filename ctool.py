import argparse 
import json
import json_dump
import os

def main():
	parser=argparse.ArgumentParser()
	parser.add_argument("--type",help="Type of file is to be searched")
	parser.add_argument("--startswith",help="File name startswith")
	parser.add_argument("--dir",help="Directory to be searched in",default=os.getcwd())

	args=parser.parse_args()
	if args.type:
		json_dump.indexing(os.getcwd(),args.type)
	name=json_dump.return_file()
	print(name)
	f=open(name,'r')
	
if __name__ == '__main__':
	main()

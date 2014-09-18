import argparse 
import json
import json_dump
import os
import tempfile

tem=tempfile.NamedTemporaryFile(mode="w+")

def main():
	parser=argparse.ArgumentParser()
	parser.add_argument("--type",help="Type of file is to be searched")
	parser.add_argument("--startswith",help="File name startswith")
	parser.add_argument("--dir",help="Directory to be searched in",default=os.getcwd())

	args=parser.parse_args()
	index=json_dump.indexing(args.dir,args.type,args.startswith)
	json.dump(index,tem)
	print(json_dump.return_file(tem))
if __name__ == '__main__':
	main()

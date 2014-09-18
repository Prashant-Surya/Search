#! usr/bin/env python3
import json
import os
import argparse
import tempfile

tags = {"py":"python","txt":"text", "c":"c", "cpp":"c++", 
"swp": "swap", "pyc": "pycache", "zip":"zip", "rar":"rar","mp3":"mp3",
"rst":"ReStructuredText", "md": "markdown", 
"java":"java","html":"html","css":"css","js":"js","php":"php",
"untagged": "unknown-Type", "jpg":"image", 
"png":"image", "jpeg":"image", "ko":"kernel", "o":"object", 
"flv":"video", "mkv":"video","mp4":"video"}

index={}

def get_extension(name):
	if '.' in name:
		name=name.split('.')
		return name[-1]
	else:
		return "untagged"
def indexing(dir,type,starts):
	print("indexing")
	for path,dirs,files in os.walk(dir):
		for file in files:
			fname=path+os.sep+file
			ext=get_extension(file)
			if type==None and starts==None:
				if(tags.get(ext)):
					index[fname]=tags[ext]
				else:
					index[fname]=ext
			elif type!=None and starts==None:
				if(tags.get(ext)==type):
					index[fname]=tags[ext]
			elif type==None and starts!=None:
				if file.startswith(starts):
					index[fname]=tags[ext]
			elif type!=None and starts!=None:
				if tags.get(ext)==type and file.startswith(starts):
					index[fname]=tags[ext]
	return index
def return_file(temp):
	return temp.name
def main():
	temp=tempfile.NamedTemporaryFile(mode="w+")
	prash={}
	parser=argparse.ArgumentParser()
	parser.add_argument("-dir",help="for selecting path",type=str)
	parser.add_argument("-type",help="Type of file",type=str)
	args=parser.parse_args()
	if args.dir==None:
		dir_path=os.getcwd()
	else:
		dir_path=args.dir
	if args.type==None:
		type=None
	else:
		type=args.type
	prash=indexing(dir_path,type)
	#with open('json.txt','w') as result:
	#	json.dump(index,result)
	json.dump(prash,temp)
	temp.flush()
	temp.seek(0)
	s=temp.read()
	print(s)
	print(return_file(temp))
if __name__ == '__main__':
	main()
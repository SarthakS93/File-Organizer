import os
import sys
import shutil

def getabspath(path):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

fileExt = set()
Mapper = {'mp4' : 'MediaFiles', 'mpg' : 'MediaFiles', 'mpeg' : 'MediaFiles', 
'mkv' : 'MediaFiles', 'flv' : 'MediaFiles', 'avi': 'MediaFiles', 'rmvb' : 'MediaFiles',  
'wmv' : 'MediaFiles', 'mp3' : 'Music', 'wav' : 'Music', 'py' : 'PythonSricpts', 
'jpg' : 'Images', 'png': 'Images', 'gif' : 'Images', 'txt' : 'TextFiles', 
'docx' : 'TextFiles', 'h' : 'cpp', 'htm' : 'html', 'js' : 'JavaScript', 'o' : 'cpp'}

def magic(Rsrc):
	src = getabspath(Rsrc)
	listsrc = os.listdir(src)

	for i in listsrc:
		path = os.path.join(src, i)
		if os.path.isfile(path):
			ext = path.split('.')[-1]
			if ext in Mapper:
				fileExt.add(Mapper[ext])
			else:
				fileExt.add(ext)				
			  
	for i in fileExt:
		dirpath = src + '/' + i;
		os.makedirs(dirpath)

	for i in listsrc:
		path = os.path.join(src, i)
		print (path)
		if os.path.isfile(path):
			ext = path.split('.')[-1]
			if ext in Mapper:
				folderName = Mapper[ext]
			else:
				folderName = ext
			dest = src + '/' + folderName + '/' + path.split('/')[-1]
			shutil.move(path, dest)    
			print(dest)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter valid arguments")
    else:
        magic(sys.argv[1])
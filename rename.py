#Usage python rename.py ./
import os       
import sys 
import re

def findnum(name):
	num=re.findall(r" ([0-9][0-9]) ",name)
	if len(num)==0:
		num=re.findall(r"\[([0-9][0-9])\]",name)
	if len(num)==0:
		num=re.findall(r"-([0-9][0-9])",name)
	if len(num)==0:
		num=re.findall(r"第([0-9][0-9])話",name)
	if len(num)==0:
		num=re.findall(r"([0-9][0-9])",name)
	return num[0]

def findtcsc(name):
	num=re.findall(r".tc.ass",name)
	if len(num)>0:
		return ".tc.ass"
	num=re.findall(r".sc.ass",name)
	if len(num)>0:
		return ".sc.ass"
	return ".ass"


def rename(path,layout):
	if os.path.isdir(path):
	    for root, dirs, files in os.walk(path):
	        for file_ in files:
	        	if file_.find('ass') >=0 and file_[0]!='.':
	        		num=findnum(file_)
	        		newname=layout.replace('XX',str(num),100)+findtcsc(file_)
	        		#print("old name= ",file_,"\n new name=",newname,"\n")
	        		print("old name= ",root+file_,"\n new name=",root+newname,"\n")
	        		os.rename(root+file_,root+newname)
	        		

if __name__ == '__main__':
	path = sys.argv[1]
	lan  = input("Please choose language: 中文请输入CN, EN for English. Example:EN\n")

	if len(re.findall(r"CN",lan)) >0:
		layout = input("请输入视频文件名格式，其中集数用XX代替，不要带后缀。\n例如:数码宝贝 第XX集 （BD 1920x1080）\n")
	elif len(re.findall(r"EN",lan))>0:
		layout = input("Please enter the video file name format without suffix, in which the episode number is replaced by XX. \nExample:Digimon-XX (BD 1920x1080) \n")
	else:
		print("Error, Thanks for using!")
		exit()
	print ("layout=",layout)
	#layout = "[Snow-Raws] 這いよれ！ニャル子さん 第XX話 (BD 1920x1080 HEVC-YUV420P10 FLACx2)"
	rename(path,layout)
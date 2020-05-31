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
        num=re.findall(r"第([0-9][0-9])话",name)
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

def findname(num,laypath):
    path = os.listdir(laypath)
    for file_ in path:
        if os.path.isfile(laypath+file_):
            if file_.find('.mkv') >=0 and file_[0]!='.' and file_.find('.mp4') and file_.find('.m4v') and file_.find('.mov') and file_.find('.avi') and file_.find(num):
                sty="\["+num+"\]"
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"[XX]",1)
                    newlay=newlay.split('.')[0]
                    return newlay
                sty='-'+num+']'
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"-XX",1)
                    newlay=newlay.split('.')[0]
                    return newlay
                sty='第'+num+'話'
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"第XX話",1)
                    newlay=newlay.split('.')[0]
                    return newlay
                sty='第'+num+'话'
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"第XX话",1)
                    newlay=newlay.split('.')[0]
                    return newlay
                sty=num
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"第XX話",1)
                    newlay=newlay.split('.')[0]
                    return newlay
    return 'NOT_FOUND_XX'

def rename(path,laypath):
    files = os.listdir(path)
    for file_ in files:
        if os.path.isfile(path+file_):
            if file_.find('.ass') >=0 and file_[0]!='.' :
                num=findnum(file_)
                layout=findname(num,laypath)
                newname=layout.replace('XX',str(num),100)+findtcsc(file_)
                #print("old name= ",file_,"\n new name=",newname,"\n")
                print("old name= ",path+file_,"\n new name=",path+newname,"\n")
                print ("\n\n")
                os.rename(path+file_,path+newname)
                

if __name__ == '__main__':
    path = sys.argv[1]
    laypath = sys.argv[2]
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    if (laypath[len(laypath)-1]!='/'):
        laypath=laypath.strip()+"/"
    #layout = "[Snow-Raws] 這いよれ！ニャル子さん 第XX話 (BD 1920x1080 HEVC-YUV420P10 FLACx2)"
    rename(path,laypath)




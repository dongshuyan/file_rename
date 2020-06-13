#Usage python rename.py ./
import os       
import sys 
import re
lan=""
def findnum(name):
    
    num=re.findall(r" ([0-9][0-9]) ",name)
    if len(num)!=0:
        sty=" "+num[0]+" "
        stz=" XX "
        stx=" "+num[0]+" "
        return num[0],sty,stz,stx

    num=re.findall(r"\[([0-9][0-9])\]",name)
    if len(num)!=0:
        sty="\["+num[0]+"\]"
        stz="[XX]"
        stx="["+num[0]+"]"
        return num[0],sty,stz,stx

    num=re.findall(r"-([0-9][0-9])",name)
    if len(num)!=0:
        sty='-'+num[0]
        stz="-XX"
        stx="-"+num[0]
        return num[0],sty,stz,stx

    num=re.findall(r"第([0-9][0-9])話",name)
    if len(num)!=0:
        sty='第'+num[0]+'話'
        stz="第XX話"
        stx='第'+num[0]+'話'
        return num[0],sty,stz,stx

    num=re.findall(r"第([0-9][0-9])话",name)
    if len(num)!=0:
        sty='第'+num[0]+'话'
        stz="第XX话"
        stx='第'+num[0]+'话'
        return num[0],sty,stz,stx

    num=re.findall(r"([0-9][0-9])",name)
    if len(num)!=0:
        sty=num[0]
        stz="XX"
        stx=num[0]
        return num[0],sty,stz,stx
        
    return num[0],sty,stz,stx

def findtcsc(name):
    num=re.findall(r".tc.ass",name)
    if len(num)>0:
        return ".tc.ass"
    num=re.findall(r".sc.ass",name)
    if len(num)>0:
        return ".sc.ass"
    return ".ass"

def findname(num,laypath,sty,stz,stx):
    path = os.listdir(laypath)
    for file_ in path:
        if os.path.isfile(laypath+file_):
            if file_.find('.mkv') >=0 and file_[0]!='.' and file_.find('.mp4') and file_.find('.m4v') and file_.find('.mov') and file_.find('.avi') and file_.find(num):
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    #print("file-name=",file_)
                    #print("sty=",sty)
                    #print("stz=",stz)

                    newlay=file_.replace(stx,stz,1)
                    newlay=newlay.split('.')[0]
                    print("newlay=",newlay)
                    return newlay
                '''
                sty="["+num+"]"
                res=re.findall(sty,file_)
                if not (len(res)==0):
                    newlay=file_.replace(sty,"[XX]",1)
                    newlay=newlay.split('.')[0]
                    return newlay
                sty='-'+num
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
                '''
    return 'NOT_FOUND_XX'

def rename(path,laypath):
    files = os.listdir(path)
    for file_ in files:
        if os.path.isfile(path+file_):
            if file_.find('.ass') >=0 and file_[0]!='.' :
                num,sty,stz,stx=findnum(file_)
                if len(re.findall(r"CN",lan)) >0:
                    print("找到第",num,"话字幕:",file_)
                elif len(re.findall(r"EN",lan))>0:
                	print("Find the "+num.strip()+"th video subtitle:"+file_)
                layout=findname(num,laypath,sty,stz,stx)
                #print("num=",num)
                #print("laypath=",laypath)
                #print("layout=",layout)
                #print("",layout)#print("",layout)
                newname=layout.replace('XX',str(num),100)+findtcsc(file_)
                #print("old name= ",file_,"\n new name=",newname,"\n")
                #print("old name= ",path+file_,"\n new name=",path+newname,"\n")
                if len(re.findall(r"CN",lan)) >0:
                    print("将原始字幕文件：",path+file_,"\n替换为：",path+newname)
                elif len(re.findall(r"EN",lan))>0:
                	print("Replace the original subtitle file:",path+file_,"\nwith:",path+newname)
                print ("\n\n")
                os.rename(path+file_,path+newname)
                

if __name__ == '__main__':
    lan  = input("Please choose language: \n(中文请输入CN, EN for English.) \nExample:CN\n")
    if len(re.findall(r"CN",lan)) >0:
        laypath = input("请输入视频文件所在文件夹绝对路径.\n例如: /Users/moyu/Downloads/video\n")
        path= input("请输入字幕文件所在文件夹绝对路径.\n例如: /Users/moyu/Downloads/subtitle\n")
    elif len(re.findall(r"EN",lan))>0:
        laypath = input("Please enter the absolute path of the folder where the video file is located.\nExample:/Users/moyu/Downloads/video\n")
        path= input("Please enter the absolute path of the folder where the subtitle file is located\n例如: /Users/moyu/Downloads/subtitle\n")
    else:
        print("Error, Thanks for using!")
        exit()
    #path = sys.argv[1]
    #laypath = sys.argv[2]
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    if (laypath[len(laypath)-1]!='/'):
        laypath=laypath.strip()+"/"
    if len(re.findall(r"CN",lan)) >0:
        print("字幕文件路径为：",path)
        print("视频文件路径为：",laypath)
    elif len(re.findall(r"EN",lan))>0:
        print("The subtitle folder path is：",path)
        print("Thevideo folder path is：",laypath)
    print("\n\n_____________START_____________")
    #layout = "[Snow-Raws] 這いよれ！ニャル子さん 第XX話 (BD 1920x1080 HEVC-YUV420P10 FLACx2)"
    rename(path,laypath)




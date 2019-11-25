import os.path
import re
li=os.listdir("C:\\Users\\kkumari27\\AppData\\Local\\Programs\\Python\\Python38-32\\Tools\\demo\\")

for i in li:

    net=os.path.splitext(i)
    if(net[1]==".log"):
        print(i)
        f=open("C:\\Users\\kkumari27\\AppData\\Local\\Programs\\Python\\Python38-32\\Tools\\demo\\"+i,"rb")
        data = f.read().decode()
        pattern="\S+@\S+"
        matches=re.findall(pattern,data)
        print(matches)


        f.close()
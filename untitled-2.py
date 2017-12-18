#/usr/bin/python
#coding=utf-8
import os,sys,time
import zipfile
filename = 'my.zip'  #要解压的文件名
filedir = 'C:\zz'  #解压后放入的目录
r = zipfile.is_zipfile(filename)
if r:
    starttime = time.time()
    fz = zipfile.ZipFile(filename,'r')
    for file in fz.namelist():
        print(file)  #打印zip归档中目录
        fz.extract(file,filedir)
    endtime = time.time()
    times = endtime - starttime
else:
    print('This file is not zip file')
print('times' + str(times))

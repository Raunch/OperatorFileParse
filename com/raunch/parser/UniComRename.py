'''
Created on 2015-3-17

@author: songshunzhang
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import zipfile
import xlrd
#file_path = "/Volumes/Macintosh_HD_E/unicomtest"
channels = {}

def listCocosName(filepath):
    data = xlrd.open_workbook(filepath)
    uni_sheet = data.sheet_by_index(0)
    nrows = uni_sheet.nrows
    for i in range(nrows):
        if i == 0:            
            dispatch_channle = uni_sheet.cell(i,0).value            
            channel_value = uni_sheet.cell(i,2).value
            print(dispatch_channle + ":" + channel_value)
            continue
        dispatch_channle = str(uni_sheet.cell(i,0).value).strip()
        channel_value = str(uni_sheet.cell(i,2).value).strip()
        channels[channel_value] = dispatch_channle
              
    print(nrows)
    for key in channels.keys():
        print key, channels[key]  
 
def modifyFileName(filename):
     for file in os.listdir(filename):
         if str(file).endswith(".zip"):
             rawname = str(file)             
             names = rawname.split("_")
             try:
                 newname = rawname.replace(names[0], channels[names[1]])
                 print newname, names[0], names[1]   
                 os.rename(os.path.join(filename, rawname), os.path.join(filename, newname))      
             except Exception,ex:
                 print rawname + "need to handle by yourself"
         else:
             continue      
                
if __name__ == '__main__':
    file_path = os.sys.argv[1]
    unicom_files = os.sys.argv[2]
    listCocosName(file_path)
    modifyFileName(unicom_files)
    pass

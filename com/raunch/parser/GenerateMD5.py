#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-12-11

@author: songshunzhang
'''

import os
import xlwt
import sys 

charge_folder = "/Volumes/Macintosh_HD_D/charge/"
charge_path = "/assets/Charge.xml"

index_channel_index = 0
#index_channel_name = 1
index_channel_value = 1

def generate_md5():
    cmd = "ls " + charge_folder
    out = os.popen(cmd).readlines()
    
    myexcel = xlwt.Workbook()
    sheet = myexcel.add_sheet("payCode", cell_overwrite_ok=True)
    
    index = 0
    sheet.write(index,index_channel_index,"number")
    #sheet.write(index,index_channel_name,"渠道名称")
    sheet.write(index,index_channel_value,"charge")
    
    
    for file in out:
        index = index + 1
        names = file.split('_')
        channel_index = names[0]
        #channel_name = names[1]
        sheet.write(index,index_channel_index,channel_index)
        #sheet.write(index,index_channel_index,channel_name)
        #print channel_name
        transferred_tmp_1 = file.replace("(", "\(")
        transferred_tmp = transferred_tmp_1.replace(" ", "\ ")
        transferred = transferred_tmp.replace(")", "\)")
        path = charge_folder + transferred.strip('\n') + charge_path
        output = getMD5(path)
        results = output.split('=')
        channel_value = results[1].strip(' ')
        sheet.write(index,index_channel_value,channel_value)
    
    
    myexcel.save('/Volumes/Macintosh_HD_D/md5.xls')

def getMD5(filepath):
    cmd = "md5 " + filepath
    return os.popen(cmd).read()
    

if __name__ == '__main__':
    generate_md5()
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-12-12

@author: songshunzhang
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import xlrd
import sys

dx_file_path = "/Volumes/Macintosh_HD_D/dianxin.xls"
dx_src_dir = "/Volumes/Macintosh_HD_D/dian_folder"
index_channel_number = 0
index_channel_name = 1
index_channel_code = 2
ck_default = "3003899679"

def generate_channel_file(folder_name, channel_value):
    if not os.path.exists(dx_src_dir):
        os.mkdir(dx_src_dir)    
    src_folder = os.path.join(dx_src_dir, folder_name)
    print src_folder
    if not os.path.exists(src_folder):
        os.mkdir(src_folder)
    internal_tmp = "assets"
    final_folder = os.path.join(src_folder, internal_tmp)
    if not os.path.exists(final_folder):
        os.mkdir(final_folder)
    file_name = final_folder + "/egame_channel.txt"
    file = open(file_name,'w')
    file.write(channel_value)
    file.close()
    
def handle_text_value(type, value):
    if type == 1:
        return value
    elif type == 2:
        values = str(value).split('.')
        return values[0]
    elif type == 5:
        return ck_default
    
def generate_dx_file():
    dx_data = xlrd.open_workbook(dx_file_path)
    dx_sheet = dx_data.sheet_by_index(0)
    nrows = dx_sheet.nrows
    for i in range(nrows):
        if i == 0:
            continue
        dispatch_channle = dx_sheet.cell(i,index_channel_number).value
        name_type = dx_sheet.cell_type(i,index_channel_name)
        dispatch_value = handle_text_value(name_type, dx_sheet.cell(i,index_channel_name).value)
        if dispatch_channle == " ":
            continue        
        type = dx_sheet.cell_type(i,index_channel_code)
        dx_code = handle_text_value(type, dx_sheet.cell(i,index_channel_code).value)
        #folder_name = dispatch_channle + "_" + dispatch_value
        folder_name = str(dispatch_channle) + "_" + str(i)
        print folder_name
        
        print (str(dispatch_channle) + ":" + dispatch_value + ":"+ dx_code)
        generate_channel_file(folder_name, dx_code)       
    


if __name__ == '__main__':
    print dx_file_path
    dx_file_path = sys.argv[1]    
    dx_src_dir = sys.argv[2]
    generate_dx_file()
    pass
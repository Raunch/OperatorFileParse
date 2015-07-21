'''
Created on 2014-12-11

@author: songshunzhang
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from xml.dom import minidom
import codecs
import xlrd
import os
import shutil
'''
filepath = "/Volumes/Macintosh_HD_D/mmiap.xml"
mm_xls_file = "/Volumes/Macintosh_HD_D/mm.xls"
mm_create_folder = "/Volumes/Macintosh_HD_D/MM_Folder"
'''
ck_default = "3003899679"
#exchanged_bak = "0000000000"
exchanged = "<channel>0000000000</channel>"

def fixed_writexml(self, writer, indent="", addindent="", newl=""):  
    # indent = current indentation  
    # addindent = indentation to add to higher levels  
    # newl = newline string  
    writer.write(indent+"<" + self.tagName)  
    print self.tagName
    attrs = self._get_attributes()  
    a_names = attrs.keys()  
    a_names.sort()  
  
    for a_name in a_names:  
        writer.write(" %s=\"" % a_name)  
        minidom._write_data(writer, attrs[a_name].value)  
        writer.write("\"")  
    if self.childNodes:  
        if len(self.childNodes) == 1 and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:  
            writer.write(">")  
            self.childNodes[0].writexml(writer, "", "", "")  
            writer.write("</%s>%s" % (self.tagName, newl))  
            return  
        writer.write(">%s"%(newl))  
        for node in self.childNodes:  
            if node.nodeType is not minidom.Node.TEXT_NODE:  
                node.writexml(writer,indent+addindent,addindent,newl)  
        writer.write("%s</%s>%s" % (indent,self.tagName,newl))  
    else:  
        writer.write("/>%s"%(newl))  
  
minidom.Element.writexml = fixed_writexml  

def get_attrvalue(node, attrname):
    return node.getAttribute(attrname) 

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) 

def change_mm_channel_xml(filename, channel_value):
    print filename
    print channel_value
    doc = minidom.parse(filename)
    root = doc.documentElement
    channel_code = get_xmlnode(root, "channel")[0]
    root.removeChild(channel_code)
    
    channel = doc.createElement('channel')
    root.appendChild(channel)
    new_value = doc.createTextNode(channel_value)
    channel.appendChild(new_value)
    
    f = codecs.open(filename,'w','UTF-8') 
    doc.writexml(f,addindent='  ',newl='\n',encoding = 'UTF-8')  
    f.close() 
    #channel_code.childNodes[0].
    #node_value = get_nodevalue(channel_code)
    #print(node_value)
    
def change_mm_channel(filename, channel_value):
    print filename
    print channel_value
    #command_bak = "sed -i 's/"+exchanged+"/"+ channel_value +"/g' " + filename
    command = "sed -i '' 's:"+exchanged+":"+"<channel>" + channel_value +"</channel>"+":g' " + filename
    print command
    result = os.popen(command).read()
    #print result
    
def handle_text_value(type, value):
    if type == 1:
        return value
    elif type == 2:
        values = str(value).split('.')
        return values[0]
    elif type == 5:
        return ck_default
    
def create_mm_channel(filename):
    if not os.path.exists(mm_create_folder):
        os.mkdir(mm_create_folder)
    
    data = xlrd.open_workbook(mm_xls_file)
    mm_sheet = data.sheet_by_index(0)
    nrows = mm_sheet.nrows
    for i in range(nrows):
        if i == 0:
            print (i)
            dispatch_channle = mm_sheet.cell(i,0).value
            
            mm_value = mm_sheet.cell(i,2).value
            print(dispatch_channle + ":" + mm_value)
            continue
        '''
        if i == 113:
            print (i)
            dispatch_channle = mm_sheet.cell_value(i,0)
            type = mm_sheet.cell_type(i,3)
            print type
            print mm_sheet.cell_value(i,3)
            mm_value = handle_text_value(type, mm_sheet.cell_value(i,3))
            print(dispatch_channle + ":" + mm_value)
            continue
        '''
        
        dispatch_channle = mm_sheet.cell(i,0).value
        dispatch_channle_type = mm_sheet.cell_type(i,0)
        dispatch_channle_value = handle_text_value(dispatch_channle_type, mm_sheet.cell(i,0).value)
        
        type = mm_sheet.cell_type(i,2)
        mm_value = handle_text_value(type, mm_sheet.cell(i,2).value)
        print(mm_value)
        print(dispatch_channle)
        sub_folder = dispatch_channle_value + "_" + str(i)
        sub_folder_name = os.path.join(mm_create_folder, sub_folder)
        if not os.path.exists(sub_folder_name):
            os.mkdir(sub_folder_name)
        shutil.copy(filepath, sub_folder_name)
        dst_file = sub_folder_name + "/mmiap.xml"
        change_mm_channel(dst_file, mm_value)
        print(dst_file)        
        
        
    print(nrows)

if __name__ == '__main__':   
    filepath = sys.argv[1]         
    mm_xls_file = sys.argv[2]
    mm_create_folder = sys.argv[3]
    create_mm_channel(filepath)
    pass
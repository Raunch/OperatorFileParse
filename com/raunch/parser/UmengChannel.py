'''
Created on 2015-2-12

@author: songshunzhang
'''
import sys
import os
import zipfile
from xml.dom import minidom

jar_path =  "/Volumes/Macintosh_HD_E/ref-tool/AXMLPrinter2.jar"

def get_attrvalue(node, attrname):
    return node.getAttribute(attrname) 

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) 

path_input = sys.argv[1];
print path_input

files = os.listdir(path_input)
for file in files:
    if str(file).startswith('.DS_Store') or str(file).startswith("AndroidManifest"):
        pass
    else: 
        z = zipfile.ZipFile(path_input + "/" + file, "r")       
        content = z.read("AndroidManifest.xml")
        fh = open(path_input + "/" + "AndroidManifest.xml", "w")
        fh.write(content)
        fh.close()
        print "File name: "  + str(file)
        result = os.system("java -jar " + jar_path + " " + path_input + "/" + "AndroidManifest.xml > " + path_input + "/test.xml")
        doc = minidom.parse(path_input + "/" + "test.xml")
        root = doc.documentElement
        package_name = get_attrvalue(root, "package")
        print "Package name: " + package_name
        app_node = get_xmlnode(root, "application")[0]
        meta_data_nodes = get_xmlnode(app_node, "meta-data")
        for meta_data in meta_data_nodes:
            name = get_attrvalue(meta_data, "android:name")
            if name == "UMENG_CHANNEL":
                value = get_attrvalue(meta_data, "android:value")
                print "UMENG channel: " + value
                break
        print "\n"
        
print "End"
if __name__ == '__main__':
    pass
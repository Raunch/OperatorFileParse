'''
Created on 2014-12-3

@author: songshunzhang
'''
# coding=gbk
from xml.dom import minidom
import xlwt

filepath = "/Volumes/Macintosh_HD_D/ItemMapper.xml"
index_itemname = 0
index_itemcode = 1
index_itemprice = 2
index_gb = 3
index_mm = 4
index_mdo = 5
index_uni_sms = 6
index_egame = 7
index_egame_sms = 8
index_pb = 9
index_sky = 10

def get_attrvalue(node, attrname):
    return node.getAttribute(attrname) 

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) 

def get_xml_data(filename):
    
    myexcel = xlwt.Workbook()
    sheet = myexcel.add_sheet("payCode", cell_overwrite_ok=True)
    
    index = 0
    sheet.write(index,index_itemname,"name")
    sheet.write(index,index_itemcode,"paycode")
    sheet.write(index,index_itemprice,"price"+"(yuan)")
    sheet.write(index,index_gb,"GB")
    sheet.write(index,index_mm,"MM")
    sheet.write(index,index_mdo,"MDO")
    sheet.write(index,index_uni_sms,"uni_sms")
    sheet.write(index,index_egame,"egame")
    sheet.write(index,index_egame_sms,"egame_sms")
    sheet.write(index,index_pb,"PB")
    sheet.write(index,index_sky,"SKY")
    #myexcel.save('/Volumes/Macintosh_HD_D/test.xls')
    
    
    doc = minidom.parse(filename)
    root = doc.documentElement
    apps = get_xmlnode(root, "item")
    
    try:
        mdo_config = get_xmlnode(root, "MDOConfig")[0]
        mdo_config_content_index = get_xmlnode(mdo_config, "ContentIndex")[0]
        mdo_content_index = get_nodevalue(mdo_config_content_index)
        print(mdo_content_index)
    except Exception,ex:
        mdo_content_index = "N/A"
    
    
    for it in apps:
        index = index + 1
        print(get_attrvalue(it, "itemCode"))
        sheet.write(index,index_itemcode,get_attrvalue(it, "itemCode"))
        
        name = get_xmlnode(it, "itemName")
        item_name =  get_nodevalue(name[0])
        print(item_name)
        sheet.write(index,index_itemname,item_name)
        
        price = get_xmlnode(it, "itemPrice")
        item_price = int(get_nodevalue(price[0])) / 100        
        print(item_price)
        sheet.write(index,index_itemprice,item_price)
        
        prop = name = get_xmlnode(it, "payProps")
        
        
        pay_prop = prop[0]
        pays = get_xmlnode(pay_prop, "pay")
        for pay in pays:
            type = get_attrvalue(pay, "payType")        
            if type == "0":
                try:
                    paycodes = get_xmlnode(pay, "payCode")
                    paycode = get_nodevalue(paycodes[0])                    
                except Exception,ex:
                    paycode = "N/A"
                print(paycode)
                sheet.write(index,index_gb,paycode)
            elif type == "1":
                try:
                    paycodes = get_xmlnode(pay, "payCode")
                    paycode = get_nodevalue(paycodes[0])                    
                except Exception,ex:
                    paycode = "N/A"
                print(paycode)
                sheet.write(index,index_mm,paycode)                
            elif type == "3":
                try:
                    contentIds = get_xmlnode(pay, "contentID")                    
                    contentId = get_nodevalue(contentIds[0])
                    bussinessIndexs = get_xmlnode(pay, "bussinessIndex")
                    bussinessIndex = get_nodevalue(bussinessIndexs[0])
                    payCodeIndexs = get_xmlnode(pay, "payCodeIndex")
                    payCodeIndex = get_nodevalue(payCodeIndexs[0])
                except Exception,ex:
                    contentId = "N/A"
                    bussinessIndex = "N/A"
                    payCodeIndex = "N/A"                    
                print(payCodeIndex+","+contentId+","+bussinessIndex)
                if contentId == "N/A" or bussinessIndex == "N/A" or payCodeIndex == "N/A":
                    paycode = "N/A"
                else:
                    paycode = "YX," + mdo_content_index + "," + payCodeIndex + "," + contentId + ","+bussinessIndex + ",*"
                
                sheet.write(index,index_mdo,paycode)
            elif type == "102":
                try:
                    paycodes = get_xmlnode(pay, "payCode")
                    paycode = get_nodevalue(paycodes[0])                    
                except Exception,ex:
                    paycode = "N/A"
                print(paycode)   
                sheet.write(index,index_uni_sms,paycode)             
            elif type == "201":
                try:
                    aliaes = get_xmlnode(pay, "alias")
                    alias = get_nodevalue(aliaes[0])
                except Exception,ex:
                    alias = "N/A"
                print(alias)
                sheet.write(index,index_egame,alias) 
            elif type == "202":
                try:
                    aliaes = get_xmlnode(pay, "alias")
                    alias = get_nodevalue(aliaes[0])
                except Exception,ex:
                    alias = "N/A"
                print(alias)
                sheet.write(index,index_egame_sms,alias) 
            elif type == "253":
                try:
                    payPointNums = get_xmlnode(pay, "payPointNum")
                    payPointNum = get_nodevalue(payPointNums[0])
                except Exception,ex:
                    payPointNum = "N/A"
                print(payPointNum)
                sheet.write(index,index_sky,payPointNum) 
            elif type == "254":
                try:
                    pbmoneys = get_xmlnode(pay, "pbmoney")
                    pbmoney = get_nodevalue(pbmoneys[0])
                except Exception,ex:
                    pbmoney = "N/A"
                print(pbmoney)
                sheet.write(index,index_pb,pbmoney)                
                    
            
        #print(name)
        
    myexcel.save('/Volumes/Macintosh_HD_D/test.xls')

if __name__ == '__main__':
    print("hello word")
    get_xml_data(filepath)    
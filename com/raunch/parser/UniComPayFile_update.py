'''
Created on 2015-3-17

@author: songshunzhang
'''
import os
import zipfile
#file_path = "/Volumes/Macintosh_HD_E/unicomtest"
file_path = "/Volumes/Macintosh_HD_E/test"

def get_pay_file(filepath):
    files = os.listdir(filepath)     
    for file in files:
        out_put_file = filepath + "/" + file
        print out_put_file
        sub_files = os.listdir(out_put_file)
        for sub_file in sub_files:
            print sub_file
            if str(sub_file).startswith('Multimode_UniPay_payinfo'):
                unzip_file(out_put_file + "/" +sub_file, out_put_file)
                os.remove(os.path.join(out_put_file, sub_file))  
            else:
                #pass
                os.remove(os.path.join(out_put_file, sub_file))
                    

def unzip_file(input, output):
    if not os.path.exists(output):
        os.makedirs(output)
    zfobjs = zipfile.ZipFile(input)
    for name in zfobjs.namelist():
        print str(name)
        if str(name).startswith("META-INF"):           
            pass
        else:            
            if str(name).endswith('/'):
                os.makedirs(os.path.join(output, name))
            else:            
                ext_filename = os.path.join(output, name)
                ext_dir= os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                out_file = open(ext_filename, "wb")
                out_file.write(zfobjs.read(name))
                out_file.close()    
                
if __name__ == '__main__':
    file_path = os.sys.argv[1]
    get_pay_file(file_path)
    pass

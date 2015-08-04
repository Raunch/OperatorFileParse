'''
Created on 2015-8-3

@author: songshunzhang
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import fnmatch
import shutil

def iterfindfiles(path, exp):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if str(filename).endswith(exp):
                yield os.path.join(root, filename)
 


if __name__ == '__main__':
    folder = sys.argv[1]
    ends = sys.argv[2] 
    output = sys.argv[3]
    for filename in iterfindfiles(folder, ends):
        print filename
        shutil.copy(filename, output)
    pass
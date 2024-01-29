import os
text = input("input string")
path = input('input path:')
def get_files(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    for filename in files:
        abspath = os.path.abspath(filename)
        if os.path.isdir(abspath):
            get_files(abspath)
        if os.path.isfile(abspath):
            f = open(filename,'r')
            if text in f.read():
                f=1
                print(text,'Found in')
                final_path = os.path.abspath(filename)
                print(final_path)
                return True
    if f == 0:
        print(text,'Not Found')
        return False
    
# function call
get_files(path)
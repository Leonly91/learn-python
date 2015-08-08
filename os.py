import os.path, time
from datetime import datetime

def dir_l():
    print('     Size     Last Modifyed     Name')
    print('--------------------------------------')
    for f in os.listdir('.'):
        fsize = os.path.getsize(f)
        if os.path.isfile(f):
            flag = ''
        elif os.path.isdir(f):
            flag = '/'
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M")
        print('%8d    %s    %s%s' % (fsize, mtime, f, flag))

if __name__ == '__main__':
    dir_l()

import os
ret = os.system('cp /opt/file1 /home/jcy/file1')
if ret==0:
    print('file copied.')
else:
    print('copy file failed!!')

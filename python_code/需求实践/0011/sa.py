# coding=utf8
import time,os
import glob

FFMPEG_PATH = 'd:/detect_data/bandicam/tmp/ffmpeg.exe'
VIDEO_DIR  = 'd:\\'


def recording():
    # 输出视频文件
    outputfile = VIDEO_DIR  + time.strftime('%Y%模块与包%d_%H%M%S', time.localtime()) + '.mp4'

    # 工具目录

    settings = '-y -rtbufsize 100M -f gdigrab -framerate 20 ' +\
               '-draw_mouse 1 -i desktop -c:v libx264 -r 20 ' +\
               '-crf 35 -pix_fmt yuv420p ' \
               '-fs 100M   "%s"' % outputfile


    recordingCmdLine = FFMPEG_PATH + ' ' + settings

    # 查看命令内容
    print(recordingCmdLine)

    # 执行命令录制视频
    os.system(recordingCmdLine)


def merging():

    os.chdir(VIDEO_DIR)
    fileList = glob.glob(VIDEO_DIR + '*.mp4')
    fileList =  [os.path.basename(one) for one in fileList]


    if fileList:
        print('\n目录中有这些视频文件：')
    else:
        print('\n目录中没有视频文件')
        return

    idx = 1
    for one in fileList:
        print('%s - %s' % (idx, one))
        idx += 1

    print('\n请选择要合并视频的视频文件序号(格式 1,2,3,4) :', end=' ')

    mergeSequence = input('')
    videoFilesToMer = mergeSequence.split(',')
    videoFileNamesToMer = [fileList[int(one.strip())-1] for one in videoFilesToMer]

    print(videoFileNamesToMer)

    with open('concat.txt','w',encoding='utf8') as f:
        for one in videoFileNamesToMer:
            f.write('file ' + one + '\n')


    cmd = FFMPEG_PATH + ' -f concat -i concat.txt -codec copy out.mp4'
    # 执行命令录制视频
    os.system(cmd)

while True:
    print('\n请选择您要做的操作：1-录制视频，2-合并视频 :', end=' ')
    choice = input('')
    if choice == '1':
        recording()
    elif choice == '2':
        merging()
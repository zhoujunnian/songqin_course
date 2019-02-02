# coding=utf8
import time,os
from subprocess import check_output,CalledProcessError,STDOUT,Popen,PIPE

# 输出视频文件
outputfile = 'e:/tmp/'  + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.mp4'

# 工具目录


ffmpegDir = r'd:\tools\ffmpeg\bin\ffmpeg.exe'


detectAudioParas = '-list_devices true -f dshow -i dummy'

detectCmd = ' '.join([ffmpegDir,detectAudioParas])


popen = Popen(detectCmd, stdout=PIPE, stderr=PIPE, shell=True)
out,err = popen.communicate()
devicesInfo = (out + err).decode('utf8')


def getAudioDevice(output):
    markWords = "] DirectShow audio devices"
    pos = output.rfind(markWords)
    if pos < 0:
        print u'!!!没有找到音频输入设备 : code 1'
        return

    output = output[pos + len(markWords):]

    tmplist = output.split('\n')

    audioList = []
    for oneline in tmplist:
        if ('Alternative name' not in oneline) and ('"' in oneline):
            pos1 = oneline.find('"')
            pos2 = oneline.rfind('"')
            audioList.append(oneline[pos1:pos2 + 1])

    for one in audioList:
        print one

    return audioList


audioDevs = getAudioDevice(devicesInfo)


settings = [
    '-y -rtbufsize 100M -f gdigrab -framerate 20',   # 帧率等
    '-offset_x 1000 -offset_y 0 -video_size 640x480', # 录制指定屏幕区域
    '-draw_mouse 1 -i desktop',          # 视频编码格式

    # 音频参数
    '-f dshow -i audio=%s' % audioDevs[0],
    '-af "highpass=f=200, lowpass=f=3000" -c:v libx264 -r 20 -preset medium -tune zerolatency -crf 35 ',
    '-pix_fmt yuv420p -c:a aac  -ac 2 -b:a 48k -fs 100M  -movflags +faststart "%s"' % outputfile  # 大小限制 等
]

recordingCmdLine = ' '.join([ffmpegDir]+settings)

# 查看命令内容
print recordingCmdLine

# 执行命令录制视频
os.system(recordingCmdLine.encode('gbk'))
# coding=utf8
import time,os

# 输出视频文件
outputfile = 'd:/data/bandicam/tmp/'  + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.mp4'

# 工具目录
ffmpegDir = r'd:\data\bandicam\tmp\ffmpeg.exe'

settings = [
    '-y -rtbufsize 100M -f gdigrab -framerate 10',   # 帧率等
    '-offset_x 1000 -offset_y 540 -video_size 640x480', # 录制指定屏幕区域
    '-draw_mouse 1 -i desktop -c:v libx264',         # 视频编码格式
    '-r 20 -preset medium -tune zerolatency -crf 35', # 视频压缩参数
    '-pix_fmt yuv420p -fs 100M  -movflags +faststart "%s"' % outputfile  # 大小限制 等
]

# 将参数组合起来
recordingCmdLine = ' '.join([ffmpegDir]+settings)

# 查看命令内容
print(recordingCmdLine)

# 执行命令录制视频
os.system(recordingCmdLine)
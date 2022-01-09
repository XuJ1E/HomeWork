#!/anaconda3/~/bin python3
# -*- coding: utf-8 -*-
# @Time     : 2022/1/9 下午1:05
# @Project  : Rtsp_Python
# @File     : Rtsp.py
# @Author   : XuJieYa
# @version  : python3
import os
import cv2

USERNAME = 'admin'
PASSWORD = 'BWQXKG'
RTSP_URL = f"rtsp://{USERNAME}:{PASSWORD}@192.168.1.22/11/Streaming/Channels/1"
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport:udp'
# is place we put the code of rtsp
cap = cv2.VideoCapture(RTSP_URL)
print(cap)


if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
ret, frame = cap.read()

while ret:
    ret, frame = cap.read()
    cv2.imshow('current frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

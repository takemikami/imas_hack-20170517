# 学習用データの生成プログラム
#
# 処理
# 1. アニメ顔検出器のダウンロード ( http://ultraist.hatenablog.com/entry/20110718/1310965532 )
# 2. プラチナスターズのアイドルPVをダウンロード
# 3. コマ送りにしてアイドルの顔画像を切り出す
# 4. 適当な雪歩・美希、やよいの画像データをダウンロード
#
# 出力
# data/pv/ アイドルPV
# data/train/[yukiho|miki|yoyai] 教師データ(顔画像)
#

import os
import urllib
from pytube import YouTube
import cv2

# 1. アニメ顔検出器のダウンロード ( http://ultraist.hatenablog.com/entry/20110718/1310965532 )
if not os.path.isdir('data'):
    os.makedirs('data')
if not os.path.isfile('data/lbpcascade_animeface.xml'):
    urllib.request.urlretrieve('https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml', 'data/lbpcascade_animeface.xml')

# 2. プラチナスターズのアイドルPVをダウンロード
pv_url = {
  'yukiho': 'https://www.youtube.com/watch?v=o7WCt196x6Y',
  'miki':   'https://www.youtube.com/watch?v=i-jjWfJytso',
  'yayoi':  'https://www.youtube.com/watch?v=v0jUg6r2_u0'
}

yt = YouTube()
if not os.path.isdir('data/pv'):
    os.makedirs('data/pv')
for k, v in pv_url.items():
    fname = 'data/pv/%s.mp4' % (k)
    if not os.path.isfile(fname):
        yt.url = v
        video = yt.get('mp4', '720p')
        yt.set_filename(k)
        video.download('data/pv/')
        print('save ', fname)

# 3. コマ送りにしてアイドルの顔画像を切り出す
cascade = cv2.CascadeClassifier("data/lbpcascade_animeface.xml")
for k in pv_url.keys():
    if not os.path.isdir('data/train/%s' % (k)):
        os.makedirs('data/train/%s' % (k))
        cap = cv2.VideoCapture("data/pv/%s.mp4" % (k))
        image_idx = 0
        for i in range(110):
            cap.set(cv2.CAP_PROP_POS_FRAMES,10*(i+1))
            ret, img = cap.read()
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.equalizeHist(gray_img, gray_img)
            facerect = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
            maxsize = 0
            maximagerect = None
            if len(facerect) > 0:
                for rect in facerect:
                    if maxsize < rect[2] * rect[3]:
                        maxsize = rect[2] * rect[3]
                        maximagerect = rect
            if maximagerect is not None:
                x = maximagerect[0]
                y = maximagerect[1]
                w = maximagerect[2]
                h = maximagerect[3]
                cv2.imwrite("data/train/%s/%d.jpg" % (k, image_idx), img[y:y+h, x:x+w])
                print("save data/train/%s/%d.jpg" % (k, image_idx))
                image_idx = image_idx + 1
        cap.release()

# 4. 適当な雪歩・美希、やよいの画像データをダウンロード
img_url = {
  'yukiho1': 'https://pbs.twimg.com/media/CpV3o9-VMAA9r9M.jpg:large',
  'yukiho2': 'https://pbs.twimg.com/media/CpL2RQ4VUAATNQb.jpg:large',
  'yukiho3': 'https://pbs.twimg.com/media/Cosys5uUAAA8evH.jpg:large',
  'yukiho4': 'https://pbs.twimg.com/media/Coss77VUIAAfHqi.jpg:large',
  'yukiho5': 'https://pbs.twimg.com/media/CoojYLsVYAEVTxG.jpg:large',
  'yayoi1': 'https://pbs.twimg.com/media/CpbQZq0UEAIbRh3.jpg:large',
  'yayoi2': 'https://pbs.twimg.com/media/Coc3punVUAIWW5g.jpg:large',
  'miki1': 'https://pbs.twimg.com/media/Cosx3YyVUAAzei6.jpg:large'
}
if not os.path.isdir('data/sample'):
    os.makedirs('data/sample')
for k, v in img_url.items():
    fname = 'data/sample/%s.jpg' % (k)
    if not os.path.isfile(fname):
        urllib.request.urlretrieve(v, fname)
        print('save ', fname)

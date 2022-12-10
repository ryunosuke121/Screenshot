import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
## execution.shで指定したスクリーンショットを取得
screenshot = os.environ['saveTo']
##　対象とする広告画像を指定する
adImage='advertisement/yahoo1.jpg'

##グレースケール表示
def display(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

##広告元の画像を読み込み
adimage = cv2.imread(adImage)
adimage = cv2.cvtColor(adimage,cv2.COLOR_BGR2RGB)
display(adimage)
##スクリーンショットの読み込み
screen = cv2.imread(screenshot)
screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
display(screen)
##特徴マッチング開始
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(adimage,None)
kp2, des2 = sift.detectAndCompute(screen,None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good = []
for match1,match2 in matches:
    if match1.distance < 0.75*match2.distance:
        good.append([match1])
sift_matches = cv2.drawMatchesKnn(adimage,kp1,screen,kp2,good,None,flags=2)
display(sift_matches)
##特徴マッチング数の表示
print(len(good))
##広告元の画像が含まれているか表示
if len(good)>150:
  print("含まれている")
else:
  print("含まれていない")
##結果画像の保存
plt.savefig("document.png")
import cv2
import numpy as np 
from PIL import Image
import as, glob
import random, math
from pathlib import Path 



DATA_DIR = Path('./img/')

names = ['aizawa', 'doi', 'hayashi', 'ipei', 'karin', 
        'matsuyama', 'mitsuki', 'nanri', 'mnonaka', 'risa',
        'shimizu', 'ueki', 'yamazaki', 'yuka', 'yukina', 'yurichu']
types = ['b', 'l1', 'l2', 'l3', 'l4', 'p1', 'p2', 'p3', 'p4', 'c1', 'c2', 'c3', 'c4']
parts = ['f','c'] # f=額，c=頬
angles = ['f','l','r', 'u','d']

# 画像のサイズを揃える

# RGB->HSV変換

def rgb_to_hsv(src, ksize = 3):
    # 高さ・幅・チャンネ数
    h, w, c = src.shape
    #srcと同じ大きさのdst用の空配列生成
    dst = np.empty((h, w, c))


    for y in range(0, h):
        for x in range(0, w):
            # R, G, Bの値を取得して0～1の範囲に
            [b, g, r] = src[y][x] / 255.0
            # R, G, Bの値の最大値と最小値を計算
            mx, mn = max(r, g, b), min(r, g, b)
            # 最大値―最小値
            diff = mx -mn

            # H
            if mx == mn 




# 特徴量抽出


import cv2
import numpy as np 
import pandas as pd
from PIL import Image
#import as, glob
import random, math
from pathlib import Path 


DATA_DIR = Path('./img/')
names = ['aizawa', 'doi', 'hayashi', 'ipei', 'karin', 
        'matsuyama', 'mitsuki', 'nanri', 'mnonaka', 'risa',
        'shimizu', 'ueki', 'yamazaki', 'yuka', 'yukina', 'yurichu']
types = ['b', 'l1', 'l2', 'l3', 'l4', 'p1', 'p2', 'p3', 'p4', 'c1', 'c2', 'c3', 'c4']
parts = ['f','c'] # f=額，c=頬
angles = ['f','l','r', 'u','d']


''' 画像のサイズを揃える '''

''' RGB->HSV変換 '''
def rgb_to_hsv(src, ksize = 3):
    # 高さ・幅・チャンネル数
    h, w, c = src.shape
    print(src.shape)
    #srcと同じ大きさのdst用の空配列生成
    dst = np.empty((h, w, c))

    for y in range(0, h):
        for x in range(0, w):
            # R, G, Bの値を取得して0～1の範囲に
            [b, g, r] = src[y][x] / 255.0
            # R, G, Bの値の最大値と最小値を計算
            mx, mn = max(r, g, b), min(r, g, b)
            # 最大値―最小値
            diff = mx - mn

            # H
            if mx == mn:
                h = 0
            elif mx == r:
                h = 60 * ((g - b) / diff)
            elif mx == g:
                h = 60 * ((b - r) / diff) + 120
            elif mx == b:
                h = 60 * ((r - g) / diff) + 240
            if h < 0:
                h = h + 360
            # S
            if mx != 0:
                s = diff / mx
            # V
            v = mx

            # H:0~359, S,V:0~100の範囲の値に変換
            dst[y][x] = [h * 0.5, s * 100, v * 100]
    
    return dst

#img = cv2.imread(str(DATA_DIR / "doi_l1_c_l.jpg"))
#print(rgb_to_hsv(img).shape)

''' 特徴量計算 '''
# 平均
def calc_means(hsv):
    h, s, v = hsv.shape
    # 平均
    sum_h_cos = 0.0
    sum_h_sin = 0.0
    sum_s = 0.0
    sum_v = 0.0
    for y in range(0, h):
        for x in range(0, s):
            #print(hsv[y][x][2])
            # hは円なので・・・
            sum_h_cos = math.cos(math.radians(hsv[y][x][0]))
            sum_h_sin = math.sin(math.radians(hsv[y][x][0]))

            sum_s = sum_s + hsv[y][x][1]
            sum_v = sum_v + hsv[y][x][2]

    h_tan = sum_h_sin / sum_h_cos
    print(h_tan)
    mean_h = np.arctan(h_tan) * 180 / math.pi
    mean_s = sum_s / (h * s)
    mean_v = sum_v / (h * s)
    
    # label

    means_hsv = [mean_h , mean_s, mean_v]

    return means_hsv

# 分散
def calc_std(hsv, means):
    h, s, v = hsv.shape

    #hsvと同じ大きさのdst用の空配列生成
    var = np.empty((h, s, v))
   
    # 偏差
    for y in range(0, h):
        for x in range(0, s):
            var[y][x] = [hsv[y][x][0] - means[0], 
                        hsv[y][x][1] - means[1],
                        hsv[y][x][2] - means[2]]

    # 分散
    dist_h = 0.0
    dist_s = 0.0 
    dist_v = 0.0
    for y in range(0, h):
        for x in range(0, s):
            dist_h = dist_h + var[y][x][0] * var[y][x][0]
            dist_s = dist_s + var[y][x][1] * var[y][x][1]
            dist_v = dist_v + var[y][x][2] * var[y][x][2]
    dist = [dist_h / (h * s), dist_s / (h * s), dist_v / (h * s)]

    # 標準偏差
    std = [math.sqrt(dist[0]), math.sqrt(dist[1]), math.sqrt(dist[2])]

    # 尖度
    # 歪度
    return std

''' 特徴量計算ここまで '''

''' 特徴量をcsvに書き込む '''
def main():

    output = pd.DataFrame(columns = ['label', 'name', 'type', 'part', 'angle',
                                    'mean_h', 'mean_s', 'mean_v',
                                    'std_h', 'std_s', 'std_v'])
    '''
    for n in names:
        for t in types:
            for p in parts:
                for a in angles:
                    # 入力画像の読み込み
                    img = cv2.imread(str(DATA_DIR / f'{n}_{t}_{p}_{a}.jpg'))
                    # hsv変換
                    hsv = rgb_to_hsv(img)
                    # 平均
                    means = calc_means(hsv)
                    # 標準偏差
                    std = calc_std(hsv, means)

                    if t == 'b':
                        label = 'bare'
                    else:
                        label = 'foundation'

                    df = pd.DataFrame([[label, n, t, p, a, 
                                        means[0], means[1], means[2], 
                                        std[0], std[1], std[2]]], 
                                        columns = ['label', 'name', 'type', 'part', 'angle',
                                                    'mean_h', 'mean_s', 'mean_v',
                                                    'std_h', 'std_s', 'std_v'])
                    
                    print(df)  
                    output =  output.append(df, ignore_index = True)

    output.to_csv(DATA_DIR / 'features.csv', index=None)

                     
                
    '''

    n = 'doi'
    t = 'l1'
    p = 'c'
    a = 'l'

    #
    # 入力画像の読み込み
    img = cv2.imread(str(DATA_DIR / f'{n}/{n}_{t}_{p}_{a}.jpg'))
    # hsv変換
    hsv = rgb_to_hsv(img)
    # 平均
    means = calc_means(hsv)
    # 標準偏差
    std = calc_std(hsv, means)

    if t == 'b':
        label = 'bare'
    else:
        label = 'foundation'

    df = pd.DataFrame([[label, n, t, p, a, 
                        means[0], means[1], means[2], 
                        std[0], std[1], std[2]]], 
                        columns = ['label', 'name', 'type', 'part', 'angle',
                                    'mean_h', 'mean_s', 'mean_v',
                                    'std_h', 'std_s', 'std_v'])
    
    print(df)  
    output =  output.append(df, ignore_index = True)

    output.to_csv(DATA_DIR / 'features.csv', index=None)


if __name__ == '__main__':
    main()

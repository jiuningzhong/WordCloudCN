# coding: utf-8


import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # 词云库
import os
from os import path
from PIL import Image
import numpy as np
import random

def txt2set(zn_StopWordPath):
    '''
    读取本地中文停用词文本并转换为列表
    :param zn_StopWordPath: 中文停用词文本路径
    :return stopWordList: 一个装有中文停用词的列表
    '''
    with open(zn_StopWordPath, 'r', encoding='utf-8') as f:
        text = f.read()
        stopWordList = text.split(';\n')
        return stopWordList

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


# 本地中文文本文件路径
zn_filePath = path.join(d, 'resources', 'xiaowangzi.txt') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\xiaowangzi.txt'
# 中文停用词文本路径
zn_StopWordPath = path.join(d, 'resources', 'zn_STOPWORDS.txt') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\zn_STOPWORDS.txt'
# 词云图保存路径
imageSavePath = path.join(d, 'resources', 'wordcloud.png') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\wordcloud.png'
# 本地中文字体路径
zn_fontPath = path.join(d, 'resources', 'yahei.ttc') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\yahei.ttc'
dic_path = path.join(d, 'resources', 'dict.txt.big.txt') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\dict.txt.big.txt'

zn_STOPWORDS = txt2set(zn_StopWordPath)
stopwords = set(zn_STOPWORDS)
stopwords.add('是')
# 如果檔案內有一些編碼錯誤，使用 errors='ignore' 來忽略錯誤
with open(zn_filePath, encoding="gbk", errors='ignore') as f:
    text = f.read()

# 設定使用 big5 斷詞
jieba.set_dictionary(dic_path)
wordlist = jieba.cut(text, cut_all=False)
words = '/'.join(wordlist)

# 從 Google 下載的中文字型
wc = WordCloud(font_path=zn_fontPath, background_color='white', max_words=100,
                        stopwords=stopwords, random_state=42, max_font_size=60).generate(words)

plt.imshow(wc)
plt.axis('off')      # 关闭图像坐标系
plt.show()           # 在IDE中显示图片
wc.to_file(imageSavePath)  # 按照背景图的宽高度保存词云图

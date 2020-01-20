# encoding:utf-8

import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # 词云库
from PIL import Image
import numpy as np
import os
from os import path

def zn_wordcloudGenerater(filePath, fontPath, imagePath, imageSavePath, zn_STOPWORDS, isImageColor):
    '''
    中文词云图生成器
    :param filePath: 本地文本文件路径
    :param fontPath: 字体文件路径
    :param imagePath: 本地图片(最好是白底)路径
    :param imageSavePath: 词云图保存路径
    :param zn_STOPWORDS: 中文停用词(List类型)
    :param isImageColor: 是否使用背景图片颜色作为词的颜色(bool值)
    '''
    # 使用上下文管理器with读取本地文本文件
    with open(filePath, 'r', encoding='gbk') as f:
        # 1、读入txt文本数据
        text = f.read()
        # 2.使用jieba进行中文分词;cut_all参数表示分词模式,True为全局模式,False为精确模式,默认为False
        cut_text = jieba.cut(text, cut_all=False)
        result = '/'.join(cut_text)
        # 3、设置中文停用词(可通过add方法添加所需中文词汇或标点符号)
        stopwords = set(zn_STOPWORDS)
        stopwords.add('是')
        # 4.1、获取本地背景图片
        image = np.array(Image.open(imagePath))
        if isImageColor:
            # 4.2、获取背景图片颜色
            image_colors = ImageColorGenerator(image)
        # 5、创建WordCloud实例并自定义设置参数(如背景色,背景图片和停用词等)
        wc = WordCloud(font_path=fontPath, background_color='white', max_words=200,  min_font_size = 4, margin = 2, scale = 2,
                       mask=image,
                       stopwords=stopwords, random_state=42, max_font_size=150)
        # 6、根据设置的参数，统计词频并生成词云图
        wc.generate(result)
        # 7、将生成的词云图保存在本地
        plt.figure('词云图')  # 指定所绘图名称
        if isImageColor:
            plt.imshow(wc.recolor(color_func=image_colors))  # 以图片的形式显示词云,并依据背景色重置词的颜色
        else:
            plt.imshow(wc)
        plt.axis('off')      # 关闭图像坐标系
        plt.show()           # 在IDE中显示图片
        wc.to_file(imageSavePath)  # 按照背景图的宽高度保存词云图

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

if __name__ == '__main__':

    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # 本地中文文本文件路径
    zn_filePath = path.join(d, 'resources', 'xiaowangzi.txt') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\xiaowangzi.txt'
    # 中文停用词文本路径
    zn_StopWordPath = path.join(d, 'resources', 'zn_STOPWORDS.txt') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\zn_STOPWORDS.txt'
    # 词云图保存路径
    imageSavePath = path.join(d, 'resources', 'wordcloud.png') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\wordcloud.png'
    # 本地中文字体路径
    zn_fontPath = path.join(d, 'resources', 'yahei.ttc') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\yahei.ttc'
    # 本地图片(最好是白底)路径
    imagePath = path.join(d, 'resources', 'mask.jpg') # 'C:\\Users\\Jiuning\\PycharmProjects\\WordCloudCN\\resources\\girl.png'
    # 中文词云图生成器
    zn_StopWordsList = txt2set(zn_StopWordPath)
    zn_wordcloudGenerater(zn_filePath, zn_fontPath, imagePath, imageSavePath, zn_StopWordsList, False)

# coding: utf-8

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

# 如果檔案內有一些編碼錯誤，使用 errors='ignore' 來忽略錯誤
with open("cnword.txt", encoding="UTF-8", errors='ignore') as f:
    text = f.read()

# 設定使用 big5 斷詞
jieba.set_dictionary('dict.txt.big')
wordlist = jieba.cut(text)
words = " ".join(wordlist)

# 從 Google 下載的中文字型
font = 'SourceHanSansTW-Regular.otf'
my_wordcloud = WordCloud(font_path=font).generate(words)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

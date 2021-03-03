import matplotlib.font_manager as fm
from wordcloud import WordCloud
from PIL import Image
import numpy as np


text = ""
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            #데이터 클렌징
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘','')

#폰트 선택
font_path = 'C:/Windows/Fonts/malgunbd.ttf'

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_wordcloud.png")


import requests,json,jieba,wordcloud
import matplotlib.pyplot as plt
from bosonnlp import BosonNLP
from scipy.misc import imread
from get_text import*
#情感分析
def Affective_analysis(text):
    nlp = BosonNLP("x-gOGutn.27554.G6_6QvdJafES")
    rest=nlp.sentiment(text)
    return rest
#
def Entity_extraction(text):
    nlp = BosonNLP("x-gOGutn.27554.G6_6QvdJafES")
    rest=nlp.ner(text)[0]
    print(rest)
    words=rest['word']
    entities=rest['entity']
    tags=rest['tag']
    for entity in entities:
        print(" ".join(words[entity[0]:entity[1]]),entity[2])
#关键字提取
def Key_word(text):
    nlp=BosonNLP("x-gOGutn.27554.G6_6QvdJafES")
    rest=nlp.extract_keywords(text,top_k=20)
    return rest

def abstract(text):
    nlp = BosonNLP("x-gOGutn.27554.G6_6QvdJafES")
    rest=nlp.summary("",text)
    plt.figure(figsize=(10, 5))
    plt.subplot(3, 3, 2)
    plt.axis([0, 20, 0, 10])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    rest=list(rest)
    for i in range(len(rest)):
        if i and i%60==0:
            rest[i]+="\n"
    rest="".join(rest)
    plt.title("摘要提取")
    plt.text(5, 10, rest, fontsize=10, style='oblique', ha='center', va='top', wrap=True)
    plt.axis("off")
    plt.show()

def show_pie(text):
    plt.style.use("ggplot")
    data=Affective_analysis(text)[0]
    labels=['积极','消极']
    explode=[0.2,0]
    colors=['limegreen','lightblue']
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    plt.axes(aspect='equal')
    plt.xlim(0,4)
    plt.ylim(0,4)
    plt.pie(x=data,explode=explode,labels=labels,colors=colors,
            autopct='%.1f%%',
            pctdistance=0.8,
            labeldistance=1.15,
            startangle=180,
            radius=1.5,
            counterclock=False,
            textprops={'fontsize':12,'color':'k'},
            center=(2,2),
            frame=1)
    plt.xticks(())
    plt.yticks(())
    plt.title("情感分析")
    plt.show()
def show_keyword(text):
    data=Key_word(text)
    content=""
    for weight,word in data:
        content+=int(weight*20)*word
    content=" ".join(jieba.lcut(content))
    # mask = imread("map.jpg")
    # plt.title("关键字提取")
    w = wordcloud.WordCloud(font_path="msyh.ttc", width=400, height=300, background_color="white", font_step=1)
    w.generate(content)
    plt.imshow(w)
    plt.axis("off")
    plt.show()

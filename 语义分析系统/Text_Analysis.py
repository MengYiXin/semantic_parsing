from bosonnlp import BosonNLP
import jieba.analyse
import jieba.posseg as pseg
import matplotlib.pyplot as plot
import numpy as np
import networkx as nx
import requests
from bs4 import BeautifulSoup
import random
def Entity_extraction(sentence): #文本实体分析
    nlp = BosonNLP('TPDuivpZ.27572.rVuPCI9-kUlN')
    result = nlp.ner(sentence)
    List = []
    for i in range(len(result[0]['entity'])):
        a = []
        a.append(result[0]['word'][result[0]['entity'][i][0]])
        a.append(result[0]['entity'][i][2])
        List.append(a)
    location_list=[] #地名
    time_list=[] #时间
    person_name=[] #人名
    job_list=[] #工作
    for i in range(len(List)):
        if List[i][1] == 'location':
            location_list.append(List[i][0])
        if List[i][1] == 'time':
            time_list.append(List[i][0])
        if List[i][1] == 'person_name':
            person_name.append(List[i][0])
        if List[i][1] == 'job_title':
            job_list.append(List[i][0])
    location_list = list(set(location_list))
    time_list = list(set(time_list))
    person_name  = list(set(person_name))
    job_list = list(set(job_list))
    location = {}
    location['地名'] = location_list
    time = {}
    time['时间'] = time_list
    person = {}
    person['人名'] = person_name
    job = {}  
    job['工作'] = job_list
    print('地名：{}\n\n时间：{}\n\n人名：{}\n\n工作：{}'.format(location['地名'],time['时间'],person['人名'],job['工作']))
    # 绘制文本实体分析
    plot.rcParams['font.sans-serif']=['SimHei']
    plot.rcParams['axes.unicode_minus']=False
    DG=nx.DiGraph()
    plot.figure(figsize=(8,8))
    plot.subplot(1,1,1)
    DG.add_nodes_from(['文本','地名','时间','人名','工作'])    
    DG.add_edges_from([('文本','地名'),('文本','人名'),('文本','工作'),('文本','时间')])   
    location_next = location['地名']
    DG.add_nodes_from(location_next)
    for i in range(len(location_next)):
        DG.add_edge('地名',location_next[i])
    time_next = time['时间']
    DG.add_nodes_from(time_next)
    for i in range(len(time_next)):
        DG.add_edge('时间',time_next[i])
    person_next = person['人名']
    DG.add_nodes_from(person_next)
    for i in range(len(person_next)):
        DG.add_edge('人名',person_next[i])
    job_next = job['工作']
    DG.add_nodes_from(job_next)
    for i in range(len(job_next)):
        DG.add_edge('工作',job_next[i])
    colors=['red','deepskyblue','magenta','limegreen','dimgrey']
    for i in range(len(location_next)):
        colors.append('lightblue')
    for i in range(len(time_next)):
        colors.append('plum')
    for i in range(len(person_next)):
        colors.append('lightgreen')
    for i in range(len(job_next)):
        colors.append('darkgray')
    nx.draw(DG,with_labels=True,node_size = 700,node_color=colors)
    plot.title('文本实体分析',color = 'red',fontsize = 20)
    plot.show()
def Word_List(sentence): #分词词频统计
    tokens = pseg.cut(sentence)
    word_list = []
    for word,flag in tokens:
        a=[]
        a.append(word)
        a.append(flag)
        word_list.append(a)
    N_list=[] #名词
    V_list=[] #动词
    A_list=[] #形容词
    R_list=[] #代词
    P_list=[] #介词
    D_list=[] # 副词
    for i in range(len(word_list)):
        if word_list[i][1] == 'n':
           N_list.append(word_list[i])
        elif word_list[i][1] == 'v':
           V_list.append(word_list[i])
        elif word_list[i][1] == 'a':
            A_list.append(word_list[i])
        elif word_list[i][1] == 'r':
            R_list.append(word_list[i])
        elif word_list[i][1] == 'p':
            P_list.append(word_list[i])
        elif word_list[i][1] == 'd':
            D_list.append(word_list[i])
    
    print('名词：{}个\n动词：{}个\n形容词：{}个\n代词：{}个\n介词：{}个\n副词：{}个'.format(len(N_list),len(V_list),len(A_list),len(R_list),len(P_list),len(D_list)))
    #绘制柱状图
    plot.rcParams['font.sans-serif']=['SimHei']
    plot.rcParams['axes.unicode_minus']=False
    x = ('名词','动词','形容词','代词','介词','副词')
    values = [len(N_list),len(V_list),len(A_list),len(R_list),len(P_list),len(D_list)]
    plot.figure(figsize=(5,4)) #定义窗口大小
    plot.subplot(1,1,1)
    index = np.arange(6)
    p2 = plot.bar(index,values,width=0.35,label='淡蓝色',color='#87CEFA')
    plot.ylabel('出现次数')
    plot.title('词频统计',color = 'red',fontsize = 15)
    plot.xticks(index,x)
    height=max(len(N_list),len(V_list),len(A_list),len(R_list),len(P_list),len(D_list))
    plot.yticks(np.arange(0,height+(height/10),height/10))
    plot.legend(loc='upper right')
    plot.show()
def Class_ification(sentence):  #进行文本分类
    plot.rcParams['font.sans-serif']=['SimHei']
    plot.rcParams['axes.unicode_minus']=False
    nlp = BosonNLP('TPDuivpZ.27572.rVuPCI9-kUlN')
    result=nlp.classify(sentence)
    info={
        0:"体育",
        1:"教育",
        2:"财经",
        3:"社会",
        4:"娱乐",
        5:"军事",
        6:"国内",
        7:"科技",
        8: "互联网",
        9: "房产",
        10: "科技",
        11: "女人",
        12: "汽车",
        13: "游戏",
    }
    DG=nx.DiGraph()
    plot.figure(figsize=(3,3))
    plot.subplot(1,1,1)
    plot.title('文本分类',color = 'red',fontsize = 15)
    DG.add_node(info[result[0]])
    nx.draw(DG,with_labels=True,node_size = 6000,node_color='lightblue')
    plot.show()

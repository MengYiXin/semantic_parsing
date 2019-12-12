from tkinter import*
from tkinter import messagebox
from analysis import *
from get_text import*
from Text_Analysis import*

def Get_words():
    if text.get("1.0","1.end")=="":
        messagebox.showinfo("提示","文本不能为空,请输入文本或点击随机新闻按钮抓取新闻")
    return text.get("1.0","1.end")
def Get_Text():
    text.delete("1.0","1.end")
    words=Get_text()
    text.insert(END, words)
window=Tk()
window.title("语义分析系统")
window.geometry("900x640+540+300")
label=Label(window,text="请输入需要分析的文本,或者点击抓取按钮随机生成新闻:",font=("微软雅黑",15),fg="blue")
label.grid()
text=Text(window,width=100,height=20)
button1=Button(window,text="随机新闻",width=10,height=1,bg="cyan",command=lambda:Get_Text())
button1['activebackground']="green"
button1.grid(row=0,column=1,padx=5)
text.grid(row=1,columnspan=2,padx=10)

sc=Scrollbar(window)
sc.grid(row=1,column=3,sticky=NS)
frame=Frame(width=700,height=40)
frame.grid(row=2,columnspan=2)
button_Entity_extraction=Button(frame,text='实体抽取',width=10,height=1,bg="pink",command=lambda:Entity_extraction(Get_words()))
button_Entity_extraction['activebackground']='limegreen'
button_Entity_extraction.grid(row=2,column=0,sticky=W)

button_Word_frequency=Button(frame,text='词频统计',width=10,height=1,bg="DarkOrange",command=lambda:Word_List(Get_words()))
button_Word_frequency['activebackground']='limegreen'
button_Word_frequency.grid(row=2,column=1,padx=5)

button_classification=Button(frame,text='文本分类',width=10,height=1,bg="yellow",command=lambda:Class_ification(Get_words()))
button_classification['activebackground']='limegreen'
button_classification.grid(row=2,column=2,padx=5)

button_Affective_analysis=Button(frame,text='情感分析',width=10,height=1,bg="red",command=lambda:show_pie(Get_words()))
button_Affective_analysis['activebackground']='limegreen'
button_Affective_analysis.grid(row=2,column=3,padx=5)

button_Key_word=Button(frame,text='关键字提取',width=10,height=1,bg="limegreen",command=lambda:show_keyword(Get_words()))
button_Key_word['activebackground']='limegreen'
button_Key_word.grid(row=2,column=5,padx=5)

button_abstract=Button(frame,text="摘要提取",width=10,height=1,bg="lightskyblue",command=lambda:abstract(Get_words()))
button_abstract['activebackground']='limegreen'
button_abstract.grid(row=2,column=6,padx=5)

window.mainloop()


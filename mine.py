# -*- coding: cp936 -*-
from Tkinter import *
import random

            
class Saoleiqidong:          #设置游戏启动类
    def __init__(self,master):
        master.title("Minesweeper-Launch")
        #############################################################
        #   布置控件
        v=IntVar()
        v.set(0)
        Radiobutton(master,text="easy",variable=v,value=1).pack()
        Radiobutton(master,text="normal",variable=v,value=2).pack()
        Radiobutton(master,text="difficult",variable=v,value=3).pack()
        qidongButton=Button(master,text="Play",command=lambda:self.playGame(v.get()))
        qidongButton.pack()
        #####################################################################
    def playGame(self,a):   #难度选择函数
        ###################################################################
        #   正常选择了难度的情况
        if a!=0:
            myApp=Saolei(a)
        ###################################################################
        #   忘记选择难度，直接点击"Play"的情况
        else:
            root=Tk()
            img=PhotoImage(master=root,file="haha.gif")
            c=Canvas(root,width=704,height=300,bg="white")
            c.pack()
            c.create_image(0,0,anchor=NW,image=img)
            root.mainloop()
        ####################################################################
class Saolei:
    def __init__(self,a):
        self.root=Tk()
        self.b=[]
               #b用于储存各个按钮
        self.d=[]
               #d用于标记各个按钮状态
        self.e=0
               #用于标记是否为第一次点击
        self.f=0
               #用于记录标记的雷数
        if a==1:
            self.x=9
            self.y=9
            self.root.title("Minesweeper-easyLevel")
            self.leiDian=random.sample(range(81),10)
            #############################################################
            #       用于之后第一次点到雷后后的重新复制
            self.leiDianji=range(81)
            self.number=10
            ###############################################################
        if a==2:
            self.x=16
            self.y=16
            self.root.title("Minesweeper-normalLevel")
            self.leiDian=random.sample(range(256),40)
            self.leiDianji=range(256)
            self.number=40
        if a==3:
            self.x=16
            self.y=30
            self.root.title("Minesweeper-difficultLevel")
            self.leiDian=random.sample(range(480),99)
            self.leiDianji=range(480)
            self.number=99
        
       #设置雷点列表
        #####################################################################################
        #       初始化b和d
        for i in range(self.x):
            self.b.append([])
            self.d.append([])
        for i in range(self.x):
            for j in range(self.y):
                self.b[i].append([])
                self.d[i].append([])
        #######################################################################################
        for i in range(self.x):
            for j in range(self.y):
                self.b[i][j]=Button(self.root,width=2,height=1,relief="raised",bg="lightblue")
                self.b[i][j].grid(row=i,column=j)
                c=self.y*i+j
                if c in self.leiDian:
                    self.b[i][j].bind("<Button-1>",self.wuLeidian1)
                            #左键点到了雷上
                    self.b[i][j].bind("<Button-3>",self.youLeidian)
                            #右键点到了雷上
                else:
                    self.b[i][j].bind("<Button-1>",self.wuleidian2)
                            #左键点到了无雷点上
                    self.b[i][j].bind("<Button-3>",self.youLeidian)
                            #右键点到了无雷点上，注意与右键点到雷上是同一个函数
     ############################################################################################
               #        布置控件用于显示剩余雷数 
        aLabel=Label(self.root,text="mines left:").grid(row=self.x,column=0,columnspan=3)
        self.aLabel=Label(self.root,text=self.number)
        self.aLabel.grid(row=self.x,column=3)
        self.button=Button(self.root,text="Finish",command=self.saoLeifinish).grid(row=self.x,column=self.y-2,columnspan=2)
                            #提交结果按钮
        self.root.mainloop()
    def youLeidian(self,event):     #右键点到按钮上对应的函数
        ######################################################
        #   返回事件发生的按钮
        m=int(event.widget.grid_info()['row'])
        n=int(event.widget.grid_info()['column'])
        ########################################################
        if self.d[m][n]==[]:
            event.widget.config(text="!",fg="red")
            self.d[m][n].append("a")
            self.f=self.f+1
            number=self.number-self.f
            self.aLabel.config(text=number)
        else:
            if self.d[m][n]==["a"]:
                event.widget.config(text="")
                self.d[m][n]=[]
                self.f=self.f-1
                number=self.number-self.f
                self.aLabel.config(text=number)
    def wuLeidian1(self,event):     #左键点到雷上对应的函数
        m=int(event.widget.grid_info()['row'])
        n=int(event.widget.grid_info()['column'])
        ##############################################################################
        ##      用于标记是否第一次点到雷，如果点到，重新生成雷点，并重新进行绑定，之后执行
        if self.e==0:
            self.e=1
            s1={self.y*m+n}
            s2=set(self.leiDianji)-s1
            self.leiDian=random.sample(list(s2),self.number)
            for i in range(self.x):
                for j in range(self.y):
                    self.b[i][j].unbind("<Button-1>")
                    self.b[i][j].unbind("<Button-3>")
                    c=self.y*i+j
                    if c in self.leiDian:
                        self.b[i][j].bind("<Button-1>",self.wuLeidian1)
                        self.b[i][j].bind("<Button-3>",self.youLeidian)
                    else:
                        self.b[i][j].bind("<Button-1>",self.wuleidian2)
                        self.b[i][j].bind("<Button-3>",self.youLeidian)
            self.wuleidian2_zhixing(m,n)
        ##############################################################################
        else:
            if self.d[m][n]==[]:
                self.b[m][n].config(text="X")
        #############################################################
        ####       这一段生成点到雷上游戏失败的画面
                for i in range(self.x):
                    for j in range(self.y):
                        self.b[i][j].unbind("<Button-1>")
                        self.b[i][j].unbind("<Button-3>")                
                root=Tk()
                img=PhotoImage(master=root,file="caidaolei.gif")
                c=Canvas(root,height=322,width=598)
                c.pack()
                c.create_image(0,0,anchor=NW,image=img)
                root.mainloop()
    	######################################################################################
    def wuleidian2(self,event):     #左键点到无雷点上对应的函数，其中调用了执行函数和扩展函数
        m=int(event.widget.grid_info()['row'])
        n=int(event.widget.grid_info()['column'])
        if self.e==0:
            self.e=1
        if self.d[m][n]==[]:
            self.wuleidian2_zhixing(m,n)
        else:
            if self.d[m][n]==["b"]:
                        #注意一个按钮点开之后标记为"b"
                self.wuleidian2_kuozhan(m,n)
    def wuleidian2_zhixing(self,a,b):   #递归定义的执行函数
        if self.d[a][b]==[]:
            c=set(self.leiDian)
            self.d[a][b].append("b")
            self.b[a][b].config(bg="gray")
            #############################################################
            #       第一行对应的操作
            if a==0:
                if b==0:
                    fujin={1,self.y,self.y+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(0,1)
                        self.wuleidian2_zhixing(1,0)
                        self.wuleidian2_zhixing(1,1)
                elif b==self.y-1:
                    fujin={self.y-2,self.y+self.y-2,self.y+self.y-1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(0,self.y-2)
                        self.wuleidian2_zhixing(1,self.y-2)
                        self.wuleidian2_zhixing(1,self.y-1)
                else:
                    fujin={b-1,b+1,b+self.y-1,b+self.y,b+self.y+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(0,b-1)
                        self.wuleidian2_zhixing(0,b+1)
                        self.wuleidian2_zhixing(1,b-1)                    
                        self.wuleidian2_zhixing(1,b)             
                        self.wuleidian2_zhixing(1,b+1)
            #####################################################################
            #       最后一行对应的操作
            elif a==self.x-1:
                if b==0:
                    fujin={self.y*(self.x-2),self.y*(self.x-2)+1,self.y*(self.x-1)+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(self.x-2,0)
                        self.wuleidian2_zhixing(self.x-2,1)
                        self.wuleidian2_zhixing(self.x-1,1)
                elif b==self.y-1:
                    fujin={self.y*(self.x-2)+self.y-2,self.y*(self.x-2)+self.y-1,self.y*(self.x-1)+self.y-2}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(self.x-2,self.y-2)
                        self.wuleidian2_zhixing(self.x-2,self.y-1)
                        self.wuleidian2_zhixing(self.x-1,self.y-2)
                else:
                    fujin={self.y*(self.x-2)+b-1,self.y*(self.x-2)+b,self.y*(self.x-2)+b+1,self.y*(self.x-1)+b-1,self.y*(self.x-1)+b+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(self.x-2,b-1)
                        self.wuleidian2_zhixing(self.x-2,b)
                        self.wuleidian2_zhixing(self.x-2,b+1)                    
                        self.wuleidian2_zhixing(self.x-1,b-1)             
                        self.wuleidian2_zhixing(self.x-1,b+1)
            ###############################################################
            #       中间几行对应的操作
            else:
                if b==0:
                    fujin={self.y*(a-1),self.y*(a-1)+1,self.y*a+1,self.y*(a+1),self.y*(a+1)+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(a-1,0)
                        self.wuleidian2_zhixing(a-1,1)
                        self.wuleidian2_zhixing(a,1)                    
                        self.wuleidian2_zhixing(a+1,0)             
                        self.wuleidian2_zhixing(a+1,1)
                elif b==self.y-1:
                    fujin={self.y*(a-1)+self.y-2,self.y*(a-1)+self.y-1,self.y*a+self.y-2,self.y*(a+1)+self.y-2,self.y*(a+1)+self.y-1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(a-1,self.y-2)
                        self.wuleidian2_zhixing(a-1,self.y-1)
                        self.wuleidian2_zhixing(a,self.y-2)                
                        self.wuleidian2_zhixing(a+1,self.y-2)             
                        self.wuleidian2_zhixing(a+1,self.y-1)
                else:
                    fujin={self.y*(a-1)+b-1,self.y*(a-1)+b,self.y*(a-1)+b+1,self.y*a+b-1,self.y*a+b+1,self.y*(a+1)+b-1,self.y*(a+1)+b,self.y*(a+1)+b+1}
                    fujingeshu=len(fujin&c)
                    if fujingeshu!=0:
                        self.b[a][b].config(text=fujingeshu,fg="blue")
                    else:
                        self.wuleidian2_zhixing(a-1,b-1)
                        self.wuleidian2_zhixing(a-1,b)
                        self.wuleidian2_zhixing(a-1,b+1)                
                        self.wuleidian2_zhixing(a,b-1)             
                        self.wuleidian2_zhixing(a,b+1)
                        self.wuleidian2_zhixing(a+1,b-1)
                        self.wuleidian2_zhixing(a+1,b)
                        self.wuleidian2_zhixing(a+1,b+1)
            #####################################################################
    ####################    快速展开已标记周围雷的点的函数
    def wuleidian2_kuozhan(self,a,b):
        ###########################################################################
        #       寻找这个按钮周围的按钮
        f=[(a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b+1)]
        fuJin=[]
        fuJin_biaojilei=[]
        fuJin_shijilei=[]
        for c in f:
            if c[0]>=0 and c[0]<=self.x-1 and c[1]>=0 and c[1]<=self.y-1:
                fuJin.append(c)
        #######################################################################
        #       寻找这个按钮周围已标记为雷的按钮
        for d in fuJin:
            if self.d[d[0]][d[1]]==["a"]:
                fuJin_biaojilei.append(d)
        #####################################################################
        #       寻找这个按钮周围的有雷的按钮
        for d in fuJin:
            if self.y*d[0]+d[1] in self.leiDian:
                fuJin_shijilei.append(d)
        #######################################################################
        #   判断如果雷标记少了，则无现象；如果标记错了，则失败
        s1=set(fuJin_biaojilei)
        s2=set(fuJin_shijilei)
        if s1<=s2:
            if s1==s2:
                for d in fuJin:
                    if self.d[d[0]][d[1]]==[]:
                        self.wuleidian2_zhixing(d[0],d[1])
        else:
            for i in range(self.x):
                for j in range(self.y):
                    self.b[i][j].unbind("<Button-1>")
                    self.b[i][j].unbind("<Button-3>")            
            root=Tk()
            img=PhotoImage(master=root,file="biaojicuo.gif")
            c=Canvas(root,height=303,width=762)
            c.pack()
            c.create_image(0,0,anchor=NW,image=img)
            root.mainloop()
    #################################################################################
    def saoLeifinish(self):
                #扫完雷后提交的函数
        leiSet=set()
        for i in range(self.x):
            for j in range(self.y):
                if self.d[i][j]==["a"]:
                    leiSet=leiSet|{self.y*i+j}                    
        if leiSet==set(self.leiDian):
        #########################################################################
        #       这一段用于生成游戏胜利的画面
            for i in range(self.x):
                for j in range(self.y):
                    self.b[i][j].unbind("<Button-1>")
                    self.b[i][j].unbind("<Button-3>")            
            root=Tk()
            img=PhotoImage(master=root,file="shengli.gif")
            c=Canvas(root,height=303,width=712)
            c.pack()
            c.create_image(0,0,anchor=NW,image=img)
            root.mainloop()
        #######################################################################
        #       这一段用于生成提交结果时标记雷点不对导致游戏失败的画面
        else:
            for i in range(self.x):
                for j in range(self.y):
                    self.b[i][j].unbind("<Button-1>")
                    self.b[i][j].unbind("<Button-3>")            
            root=Tk()
            c=Canvas(root,height=303,width=762)
            c.pack()
            if len(leiSet)<len(self.leiDian):
                img=PhotoImage(master=root,file="biaojishao.gif")
                c.create_image(0,0,anchor=NW,image=img)
                root.mainloop()                                
                        #雷标记少了
            else:
                img=PhotoImage(master=root,file="biaojicuo.gif")
                c.create_image(0,0,anchor=NW,image=img)
                root.mainloop()
                        #雷标记错了
        ##############################################################################
def main():
    root=Tk()
    app=Saoleiqidong(root)
    root.mainloop()
main()

        


# -*- coding: cp936 -*-
from Tkinter import *
import random

            
class Saoleiqidong:          #������Ϸ������
    def __init__(self,master):
        master.title("Minesweeper-Launch")
        #############################################################
        #   ���ÿؼ�
        v=IntVar()
        v.set(0)
        Radiobutton(master,text="easy",variable=v,value=1).pack()
        Radiobutton(master,text="normal",variable=v,value=2).pack()
        Radiobutton(master,text="difficult",variable=v,value=3).pack()
        qidongButton=Button(master,text="Play",command=lambda:self.playGame(v.get()))
        qidongButton.pack()
        #####################################################################
    def playGame(self,a):   #�Ѷ�ѡ����
        ###################################################################
        #   ����ѡ�����Ѷȵ����
        if a!=0:
            myApp=Saolei(a)
        ###################################################################
        #   ����ѡ���Ѷȣ�ֱ�ӵ��"Play"�����
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
               #b���ڴ��������ť
        self.d=[]
               #d���ڱ�Ǹ�����ť״̬
        self.e=0
               #���ڱ���Ƿ�Ϊ��һ�ε��
        self.f=0
               #���ڼ�¼��ǵ�����
        if a==1:
            self.x=9
            self.y=9
            self.root.title("Minesweeper-easyLevel")
            self.leiDian=random.sample(range(81),10)
            #############################################################
            #       ����֮���һ�ε㵽�׺������¸���
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
        
       #�����׵��б�
        #####################################################################################
        #       ��ʼ��b��d
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
                            #����㵽������
                    self.b[i][j].bind("<Button-3>",self.youLeidian)
                            #�Ҽ��㵽������
                else:
                    self.b[i][j].bind("<Button-1>",self.wuleidian2)
                            #����㵽�����׵���
                    self.b[i][j].bind("<Button-3>",self.youLeidian)
                            #�Ҽ��㵽�����׵��ϣ�ע�����Ҽ��㵽������ͬһ������
     ############################################################################################
               #        ���ÿؼ�������ʾʣ������ 
        aLabel=Label(self.root,text="mines left:").grid(row=self.x,column=0,columnspan=3)
        self.aLabel=Label(self.root,text=self.number)
        self.aLabel.grid(row=self.x,column=3)
        self.button=Button(self.root,text="Finish",command=self.saoLeifinish).grid(row=self.x,column=self.y-2,columnspan=2)
                            #�ύ�����ť
        self.root.mainloop()
    def youLeidian(self,event):     #�Ҽ��㵽��ť�϶�Ӧ�ĺ���
        ######################################################
        #   �����¼������İ�ť
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
    def wuLeidian1(self,event):     #����㵽���϶�Ӧ�ĺ���
        m=int(event.widget.grid_info()['row'])
        n=int(event.widget.grid_info()['column'])
        ##############################################################################
        ##      ���ڱ���Ƿ��һ�ε㵽�ף�����㵽�����������׵㣬�����½��а󶨣�֮��ִ��
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
        ####       ��һ�����ɵ㵽������Ϸʧ�ܵĻ���
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
    def wuleidian2(self,event):     #����㵽���׵��϶�Ӧ�ĺ��������е�����ִ�к�������չ����
        m=int(event.widget.grid_info()['row'])
        n=int(event.widget.grid_info()['column'])
        if self.e==0:
            self.e=1
        if self.d[m][n]==[]:
            self.wuleidian2_zhixing(m,n)
        else:
            if self.d[m][n]==["b"]:
                        #ע��һ����ť�㿪֮����Ϊ"b"
                self.wuleidian2_kuozhan(m,n)
    def wuleidian2_zhixing(self,a,b):   #�ݹ鶨���ִ�к���
        if self.d[a][b]==[]:
            c=set(self.leiDian)
            self.d[a][b].append("b")
            self.b[a][b].config(bg="gray")
            #############################################################
            #       ��һ�ж�Ӧ�Ĳ���
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
            #       ���һ�ж�Ӧ�Ĳ���
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
            #       �м伸�ж�Ӧ�Ĳ���
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
    ####################    ����չ���ѱ����Χ�׵ĵ�ĺ���
    def wuleidian2_kuozhan(self,a,b):
        ###########################################################################
        #       Ѱ�������ť��Χ�İ�ť
        f=[(a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b+1)]
        fuJin=[]
        fuJin_biaojilei=[]
        fuJin_shijilei=[]
        for c in f:
            if c[0]>=0 and c[0]<=self.x-1 and c[1]>=0 and c[1]<=self.y-1:
                fuJin.append(c)
        #######################################################################
        #       Ѱ�������ť��Χ�ѱ��Ϊ�׵İ�ť
        for d in fuJin:
            if self.d[d[0]][d[1]]==["a"]:
                fuJin_biaojilei.append(d)
        #####################################################################
        #       Ѱ�������ť��Χ�����׵İ�ť
        for d in fuJin:
            if self.y*d[0]+d[1] in self.leiDian:
                fuJin_shijilei.append(d)
        #######################################################################
        #   �ж�����ױ�����ˣ��������������Ǵ��ˣ���ʧ��
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
                #ɨ���׺��ύ�ĺ���
        leiSet=set()
        for i in range(self.x):
            for j in range(self.y):
                if self.d[i][j]==["a"]:
                    leiSet=leiSet|{self.y*i+j}                    
        if leiSet==set(self.leiDian):
        #########################################################################
        #       ��һ������������Ϸʤ���Ļ���
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
        #       ��һ�����������ύ���ʱ����׵㲻�Ե�����Ϸʧ�ܵĻ���
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
                        #�ױ������
            else:
                img=PhotoImage(master=root,file="biaojicuo.gif")
                c.create_image(0,0,anchor=NW,image=img)
                root.mainloop()
                        #�ױ�Ǵ���
        ##############################################################################
def main():
    root=Tk()
    app=Saoleiqidong(root)
    root.mainloop()
main()

        


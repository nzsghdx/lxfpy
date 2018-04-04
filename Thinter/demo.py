# 导入tkinter的所有模块:从tkinter中导入所有
from tkinter import *
# 导入tkinter的messagebox的子模块并且重命名为messagebox
import tkinter.messagebox as messagebox

# 创建整个项目类
class Application(Frame):
    # 初始化一些内容,使用Frame,调用createWidgets函数(自己手动编写的)
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    # 具体的窗体信息设置
    def createWidgets(self):
        # 使用nameInput设置Entry,暂时不知道语句具体是什么意思,先用着吧
        self.nameInput=Entry(self)
        # 任何语句都需要使用pack函数,把设置的信息给捣鼓进widget
        self.nameInput.pack()
        # 弹出(alter)一个button,并且设置button的显示信息,调用了类中的hello函数
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
       # self.helloLabel=Label(self,text='Hello,Tkinter!')
       # self.helloLabel.pack()
       # self.quitButton=Button(self,text='Quit',command=self.quit)
       # self.quitButton.pack()

    def hello(self):
        # hello函数,使用get函数用于显示设置的信息,否则显示world
        name=self.nameInput.get() or 'world'
        # 应该显示的信息是如下,应该显示的是Message,第二个参数是Message的值
        messagebox.showinfo('Message','Hello,%s'%name)

# 实例化主体函数类
app=Application()
# 设置窗口标题
app.master.title('Hello,World')
# 主消息循环,恩,不知道loop是啥意思,所以这一句也不懂,理解为启动操作吧
app.mainloop()


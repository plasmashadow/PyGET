
import Tkinter as tk
import ttk
class Downloader:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("FireDW Downloader")
        self.window.geometry('500x600')
        ############adding components################
        self.menubar=tk.Menu(self.window)
        #########
        self.Dloadmenu=tk.Menu(self.menubar,tearoff=0)
        self.Dloadmenu.add_command(label="Single Download",command=self.ColorChange)
        self.Dloadmenu.add_command(label="List Download")
        self.Dloadmenu.add_separator()
        self.Dloadmenu.add_command(label="Exit",command=self.window.quit)
        self.menubar.add_cascade(label="Download",menu=self.Dloadmenu)
        #########
        self.Aboutmenu=tk.Menu(self.menubar,tearoff=0)
        self.Aboutmenu.add_command(label="About")
        self.menubar.add_cascade(label="About",menu=self.Aboutmenu)
        ###########
        self.window.config(menu=self.menubar)
        #########
        self.lab=tk.Label(self.window,text="Enter the URl of the Link")
        self.lab.pack()
        self.txt=tk.Entry(self.window,width=800)
        self.txt.pack()
        ###############intitalising#####################
        
        ################################################
        ################################################
        self.btn=tk.Button(self.window,text="Download")
        self.btn.pack()
        
        self.lab=tk.Label(self.window,text="In Active",bg='red',width=720)
        self.lab.pack(side=tk.BOTTOM)
        self.pbbar=ttk.Progressbar(self.window,length=1800)
        self.pbbar.pack(side=tk.BOTTOM)
        self.window.mainloop()
    def ColorChange(self):
            self.lab.config(bg='green',text='Active')
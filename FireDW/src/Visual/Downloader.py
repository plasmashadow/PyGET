import Tkinter as tk
import ttk
import urllib2
class Downloader:
    def __init__(self):
        self.bytes=0
        self.file_size_dl=0
        self.window=tk.Tk()
        self.window.title("FireDW Downloader")
        self.window.geometry('500x500')
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
        self.Aboutmenu.add_command(label="About",command=self.Create_about_frame)
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
        self.btn=tk.Button(self.window,text="Download",command=self.func)
        self.btn.pack()
        
        self.lab=tk.Label(self.window,text="In Active",bg='red',width=720)
        self.lab.pack(side=tk.BOTTOM)
        self.pbbar=ttk.Progressbar(self.window,length=1800,orient="horizontal",mode="determinate")
        self.barlength=0
        self.pbbar.pack(side=tk.BOTTOM)
        self.window.mainloop()
    def ColorChange(self):
            self.lab.config(bg='brown',text='Downloading In progress')
    def func(self):
        self.lab.config(bg='brown',text='Downloading In progress')
        self.url=self.txt.get()
        self.filename=self.url.split("/")[-1]
        self.u=urllib2.urlopen(self.url)
        self.f = open("/home/sathyagriffin/"+self.filename, 'wb')
        self.meta = self.u.info()
        self.file_size = int(self.meta.getheaders("Content-Length")[0])
        self.pbbar["value"]=0
        self.pbbar["maximum"]=self.file_size
        self.paint_progress()

    def paint_progress(self):
         block_sz = 1024
         buffer =self.u.read(block_sz)
         if not buffer:
             exit
         self.file_size_dl += len(buffer)
         self.f.write(buffer)         
         if(self.file_size_dl<self.file_size):
             self.pbbar["value"] +=block_sz
             self.window.after(1, self.paint_progress)
         if(self.file_size_dl>=self.file_size):
             self.pbbar["value"]=self.file_size
             self.lab.config(bg='green',text='Download Complete')
    def Create_about_frame(self):
        root=tk.Tk()
        root.title("About")
        root.geometry('300x100')
        label=tk.Label(root,text="Fire Downloader \n Author: Plasmashadow(Sathya Narrayanan)")
        label.pack()
        label11=tk.Label(root,text="License: GPL (General public licence)\n Source Code is Available on \n http:\\\github.com\plasmashadow\PyGET")
        label11.pack()
        root.mainloop()

import Tkinter as tk
import urllib2
import ttk
import time
class listdownload:
    def __init__(self):
        self.downloadlist=[]
        self.file_size_dl=0
        self.window1=tk.Tk()
        self.window1.title("List Download")
        self.window1.geometry('400x320')
        self.List=tk.Listbox(self.window1,width=390)
        self.List.pack()
        self.label=tk.Label(self.window1,text="Enter the URL:")
        self.label.pack()
        self.txt=tk.Entry(self.window1,width=390)
        self.txt.pack()
        self.Add=tk.Button(self.window1,text="Add Download",command=self.Add_downloads)
        self.Add.pack()
        self.download=tk.Button(self.window1,text="Start List Download",command=self.Start_download)
        self.download.pack()
        self.lab=tk.Label(self.window1,text="In active",width=390)
        self.pbbar=ttk.Progressbar(self.window1,length=1800,orient="horizontal",mode="determinate")
        self.pbbar.pack(side=tk.BOTTOM)
        self.lab.pack(side=tk.BOTTOM)
        self.window1.mainloop()
    def Add_downloads(self):
        self.List.insert(tk.END,self.txt.get())
    def Start_download(self):
        self.downloadlist=self.List.get(0,tk.END)
        for url in self.downloadlist:
            print "Downloading :"+url
            self.download_function(url)
            print "Completed downloading: "+url
    def download_function(self,url):
        self.lab.config(bg='brown',text='download in progress')
        self.filename=url.split("/")[-1]
        self.u=urllib2.urlopen(url)
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
             self.window1.after(1, self.paint_progress)
         if(self.file_size_dl>=self.file_size):
             self.pbbar["value"]=self.file_size
             self.lab.config(bg='green',text='Download Complete')
             time.sleep(1)
             self.pbbar["value"]=0
             self.lab.config(bg='green',text="Starting new Download")
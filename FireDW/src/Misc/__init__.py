import urllib
import subprocess
from multiprocessing.pool import wait
import time
def return_size_in_MB(text):
    return(float(float(text/1000)/1000))

def return_content_size(url):
    file_name = url.split('/')[-1]
    d = urllib.urlopen(url)
    #----GET FILE SIZE----
    meta = d.info()
   # print ("Download Details", meta)
    file_size = int(meta.getheaders("Content-Length")[0])
    return file_size

def start_single_download(url):
    filename=url.split('/')[-1];
    command="~/"+filename
    name = subprocess.Popen(['wget',url,'-O',command])

def get_the_current_size_of_file(filename):
     f=open(filename,'rb')
     f.seek(0,2)
     size=f.tell()
     return size
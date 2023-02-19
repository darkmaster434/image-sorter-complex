import tkinter as tk
import os
import shutil
from PIL import Image, ImageTk
from win32api import GetSystemMetrics
screen_width = GetSystemMetrics(0)-200 #get screen width
screen_height = GetSystemMetrics(1)-200 #get screen height
main_window_x = screen_width-200
main_window_y = screen_height-200
image_resize_precentage = 55  # %
img_width = int((image_resize_precentage/100)*main_window_y)
img_height = int((image_resize_precentage/100)*main_window_x)
global img1,c,img3
global img2
img2=list()

c=0
d_path=os.path.expanduser("~\Desktop")

cc_path=os.path.join(d_path,'Category')

s_path='C:/Users/Corrupted/Desktop/S_data' #semantics directory
c_path='C:/Users/Corrupted/Desktop/sorted' # my given directory
plain_path='G:/Download/Compressed/unique_uis.tar/unique_uis' # palin screenshot dirctory main one
img_list=os.listdir(s_path)
btn_list=os.listdir(c_path)

class MuGUI():
   
    def __init__(self) -> None:
        t_no_files=0
        t_no_optimize=0
        t_no_not_optimize=0
        empty_dir=list()
        if os.path.exists(cc_path):
            c_o=0
            c_n_o=0
            for i in os.walk(cc_path):
                folder_name=i[0].split('\\')[-1]
                no_folder=len(i[1])
                no_files=len(i[2])
                t_no_files+=no_files
                if 'not' in folder_name.split('_'):
                    t_no_not_optimize+=no_files
                else:
                    t_no_optimize+=no_files
                if no_folder==0 and no_files==0:
                    empty_dir.append(folder_name)
                print(f'\n♦ Folder:{folder_name}\n ╚Number Folder:{no_folder}\n ╚Number Files:{no_files}')

            print(f'\n⌐Total Sorted:{t_no_files}\n⌐Total optimized:{t_no_optimize}\n⌐Total Not Optimize:{t_no_not_optimize}\n\nEmpty Directories:')
            for i in empty_dir:
                print(' ├',i)
                
        global img1,img2
        self.root=tk.Tk()
        self.root.geometry(str(screen_width)+'x'+str(screen_height))
        self.fframe=tk.Frame(self.root)
        self.fframe.columnconfigure(0,weight=1)
        self.fframe.columnconfigure(1,weight=1)
        self.fframe.columnconfigure(2,weight=1)
        self.fframe.columnconfigure(3,weight=1)
        
        b_frame=tk.Frame(self.fframe,background='yellow')
        b_frame.columnconfigure(0,weight=1)
        b_frame.columnconfigure(1,weight=1)
        b_frame.columnconfigure(2,weight=1)
        r=0
        for i in range(0,len(btn_list),3):
            try:
                b1=tk.Button(b_frame,text=btn_list[i],command=lambda b=btn_list[i]:self.get_img(b))
                b2=tk.Button(b_frame,text=btn_list[i+1],command=lambda b=btn_list[i+1]:self.get_img(b))
                b3=tk.Button(b_frame,text=btn_list[i+2],command=lambda b=btn_list[i+2]:self.get_img(b))
            except:
                pass
            b1.grid(row=r,column=0,sticky=tk.W+tk.E)
            b2.grid(row=r,column=1,sticky=tk.W+tk.E)
            b3.grid(row=r,column=2,sticky=tk.W+tk.E)
            r+=1
        dec_btn_fram=tk.Frame(b_frame,background='blue')
        
        self.btn_good=tk.Button(dec_btn_fram,text='Good',command=self.sendToGood,background='green')
        self.btn_good.pack(fill=tk.X,side=tk.LEFT,expand=1)
        self.btn_bad=tk.Button(dec_btn_fram,text='Bad',command=self.sendToBad,background='red')
        self.btn_bad.pack(fill=tk.X,side=tk.RIGHT,expand=1)
        
        dec_btn_fram.grid(row=r,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.make_dir=tk.Button(b_frame,text='Make Directory and Refresh',command=self.mkdir,background='cyan')
        self.make_dir.grid(row=r+1,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.delete=tk.Button(b_frame,text='Delete',command=self.delete_this,background='Red',font=('Arial',15))
        self.delete.grid(row=r+2,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        
        self.img_label=tk.Label(b_frame,text=img_list[c],font=('Arial',20))
        self.img_label.grid(row=r+3,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        t = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img3 = ImageTk.PhotoImage(t)
        self.photo_label2 = tk.Label(self.fframe, image=img3)
        self.photo_label2.grid(row=0,column=0,sticky=tk.W+tk.E+tk.S+tk.N)
        
        t = Image.open(s_path+'/'+img_list[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(t)
        self.photo_label1 = tk.Label(self.fframe, image=img1)
        self.photo_label1.grid(row=0,column=1,sticky=tk.W+tk.E+tk.S+tk.N)
        
        
        if os.path.exists(cc_path):
            ll=os.listdir(cc_path)
            r=r+3+1
            for i in range(0,len(ll),2):
                b1=tk.Button(b_frame,text=ll[i],background='hot pink',command=lambda b=ll[i]:self.sendToSend(b))
                b1.grid(row=r+i,column=0,sticky=tk.W+tk.E+tk.S+tk.N)
                b2=tk.Button(b_frame,text=ll[i+1],background='SeaGreen1',command=lambda b=ll[i+1]:self.sendToSend(b))
                b2.grid(row=r+i,column=1,columnspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
        b_frame.grid(row=0,column=2,sticky=tk.W+tk.E)
        self.img_frame=tk.Frame(self.fframe,background='red')
        self.img_frame.columnconfigure(1)
        self.img_frame.columnconfigure(2)
        self.img_frame.columnconfigure(3)
        self.img_frame.grid(row=0,column=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.fframe.pack(padx=10,pady=10)
        self.root.mainloop()
    
    def get_img(self,b):
        global img2
        img2=list()
        new_path=c_path+'/'+b
        new_imgs=os.listdir(new_path)
        self.btn_bad.config(text=b+' Bad')
        self.btn_good.config(text=b+' Good')
        if len(new_imgs)>10:
            l=9
        else:
            l=len(new_imgs)
        r=0
        c=0
        for i in range(l):
            t = Image.open(c_path+'/'+b+'/'+new_imgs[i])
            t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
            t = ImageTk.PhotoImage(t)
            img2.append(t)
        # t = Image.open(c_path+'/'+b+'/'+new_imgs[0])
        # t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
        # new_img=Image.new('RGB',(img_width+250,img_height),'black')
        # new_img.paste(t,(0,0))
        # t = Image.open(c_path+'/'+b+'/'+new_imgs[2])
        # t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
        # new_img.paste(t,(img_width-250+5,0))
        for i in range(9):
            self.photo_label3 = tk.Label(self.img_frame, image=img2[i])
            self.photo_label3.grid(row=r,column=c)
            r+=1
            if (i+1)%3==0:
                r=0
                c+=1
        
    def sendToGood(self,b_t=None):
        global c,img1,img3
        img3=''
        if b_t==None:
            b_t=self.btn_good.cget('text')
        if b_t!='Good':
            d_name=str(b_t).split()[0]
            shutil.move(s_path+'/'+img_list[c],d_path+'/Category/'+d_name+'_optimize/'+img_list[c])
            c+=1
            
            t = Image.open(s_path+'/'+img_list[c])
            t = t.resize((img_width, img_height), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(t)
            self.photo_label1.config(image=img1)
            
            ta = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
            ta = ta.resize((img_width, img_height), Image.LANCZOS)
            img3 = ImageTk.PhotoImage(ta)
            self.photo_label2.config(image=img3)
        
        
    def sendToBad(self,b_t=None):
        global c,img1,img3
        if b_t == None:
            b_t=self.btn_bad.cget('text')
        if b_t!='Bad':
            d_name=str(b_t).split()[0]
            shutil.move(s_path+'/'+img_list[c],d_path+'/Category/'+d_name+'_not_optimize/'+img_list[c])
            c+=1
            t = Image.open(s_path+'/'+img_list[c])
            t = t.resize((img_width, img_height), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(t)
            self.photo_label1.config(image=img1)
            
            aa = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
            aa = aa.resize((img_width, img_height), Image.LANCZOS)
            img3 = ImageTk.PhotoImage(aa)
            self.photo_label2.config(image=img3)
    
    def mkdir(self):
        cate_path=os.path.join(d_path,'Category')
        if not os.path.exists(cate_path):
           
            os.mkdir(cate_path)
        else:
            print(cate_path+' Exist')
        for i in btn_list:
            good_path=os.path.join(cate_path,i+'_optimize')
            bad_pth=os.path.join(cate_path,i+'_not_optimize')
            if not os.path.exists(good_path):
                os.mkdir(good_path)
            else:
                print(good_path,' Exist')
            if not os.path.exists(bad_pth):
                os.mkdir(bad_pth)
            else:
                print(bad_pth,' Exist')
        self.root.destroy()
        MuGUI()
    def delete_this(self):
        global img1,c,img3
        os.remove(s_path+'/'+img_list[c])
        c+=1
        t = Image.open(s_path+'/'+img_list[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(t)
        self.photo_label1.config(image=img1)
        
        ta = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
        ta = ta.resize((img_width, img_height), Image.LANCZOS)
        img3 = ImageTk.PhotoImage(ta)
        self.photo_label2.config(image=img3)
    def sendToSend(self,b):
        b=str(b).split('_')
        if b[1]=='not':
            self.sendToBad(b[0])
        else:
            self.sendToGood(b[0])
        
MuGUI()import tkinter as tk
import os
import shutil
from PIL import Image, ImageTk
from win32api import GetSystemMetrics
screen_width = GetSystemMetrics(0)-200 #get screen width
screen_height = GetSystemMetrics(1)-200 #get screen height
main_window_x = screen_width-200
main_window_y = screen_height-200
image_resize_precentage = 55  # %
img_width = int((image_resize_precentage/100)*main_window_y)
img_height = int((image_resize_precentage/100)*main_window_x)
global img1,c,img3
global img2
img2=list()

c=0
d_path=os.path.expanduser("~\Desktop")

cc_path=os.path.join(d_path,'Category')

s_path='C:/Users/Corrupted/Desktop/S_data' #semantics directory
c_path='C:/Users/Corrupted/Desktop/sorted' # my given directory
plain_path='G:/Download/Compressed/unique_uis.tar/unique_uis' # palin screenshot dirctory main one
img_list=os.listdir(s_path)
btn_list=os.listdir(c_path)

class MuGUI():
   
    def __init__(self) -> None:
        t_no_files=0
        t_no_optimize=0
        t_no_not_optimize=0
        empty_dir=list()
        if os.path.exists(cc_path):
            c_o=0
            c_n_o=0
            for i in os.walk(cc_path):
                folder_name=i[0].split('\\')[-1]
                no_folder=len(i[1])
                no_files=len(i[2])
                t_no_files+=no_files
                if 'not' in folder_name.split('_'):
                    t_no_not_optimize+=no_files
                else:
                    t_no_optimize+=no_files
                if no_folder==0 and no_files==0:
                    empty_dir.append(folder_name)
                print(f'\n♦ Folder:{folder_name}\n ╚Number Folder:{no_folder}\n ╚Number Files:{no_files}')

            print(f'\n⌐Total Sorted:{t_no_files}\n⌐Total optimized:{t_no_optimize}\n⌐Total Not Optimize:{t_no_not_optimize}\n\nEmpty Directories:')
            for i in empty_dir:
                print(' ├',i)
                
        global img1,img2
        self.root=tk.Tk()
        self.root.geometry(str(screen_width)+'x'+str(screen_height))
        self.fframe=tk.Frame(self.root)
        self.fframe.columnconfigure(0,weight=1)
        self.fframe.columnconfigure(1,weight=1)
        self.fframe.columnconfigure(2,weight=1)
        self.fframe.columnconfigure(3,weight=1)
        
        b_frame=tk.Frame(self.fframe,background='yellow')
        b_frame.columnconfigure(0,weight=1)
        b_frame.columnconfigure(1,weight=1)
        b_frame.columnconfigure(2,weight=1)
        r=0
        for i in range(0,len(btn_list),3):
            try:
                b1=tk.Button(b_frame,text=btn_list[i],command=lambda b=btn_list[i]:self.get_img(b))
                b2=tk.Button(b_frame,text=btn_list[i+1],command=lambda b=btn_list[i+1]:self.get_img(b))
                b3=tk.Button(b_frame,text=btn_list[i+2],command=lambda b=btn_list[i+2]:self.get_img(b))
            except:
                pass
            b1.grid(row=r,column=0,sticky=tk.W+tk.E)
            b2.grid(row=r,column=1,sticky=tk.W+tk.E)
            b3.grid(row=r,column=2,sticky=tk.W+tk.E)
            r+=1
        dec_btn_fram=tk.Frame(b_frame,background='blue')
        
        self.btn_good=tk.Button(dec_btn_fram,text='Good',command=self.sendToGood,background='green')
        self.btn_good.pack(fill=tk.X,side=tk.LEFT,expand=1)
        self.btn_bad=tk.Button(dec_btn_fram,text='Bad',command=self.sendToBad,background='red')
        self.btn_bad.pack(fill=tk.X,side=tk.RIGHT,expand=1)
        
        dec_btn_fram.grid(row=r,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.make_dir=tk.Button(b_frame,text='Make Directory and Refresh',command=self.mkdir,background='cyan')
        self.make_dir.grid(row=r+1,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.delete=tk.Button(b_frame,text='Delete',command=self.delete_this,background='Red',font=('Arial',15))
        self.delete.grid(row=r+2,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        
        self.img_label=tk.Label(b_frame,text=img_list[c],font=('Arial',20))
        self.img_label.grid(row=r+3,column=0,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        t = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img3 = ImageTk.PhotoImage(t)
        self.photo_label2 = tk.Label(self.fframe, image=img3)
        self.photo_label2.grid(row=0,column=0,sticky=tk.W+tk.E+tk.S+tk.N)
        
        t = Image.open(s_path+'/'+img_list[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(t)
        self.photo_label1 = tk.Label(self.fframe, image=img1)
        self.photo_label1.grid(row=0,column=1,sticky=tk.W+tk.E+tk.S+tk.N)
        
        
        if os.path.exists(cc_path):
            ll=os.listdir(cc_path)
            r=r+3+1
            for i in range(0,len(ll),2):
                b1=tk.Button(b_frame,text=ll[i],background='hot pink',command=lambda b=ll[i]:self.sendToSend(b))
                b1.grid(row=r+i,column=0,sticky=tk.W+tk.E+tk.S+tk.N)
                b2=tk.Button(b_frame,text=ll[i+1],background='SeaGreen1',command=lambda b=ll[i+1]:self.sendToSend(b))
                b2.grid(row=r+i,column=1,columnspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
        b_frame.grid(row=0,column=2,sticky=tk.W+tk.E)
        self.img_frame=tk.Frame(self.fframe,background='red')
        self.img_frame.columnconfigure(1)
        self.img_frame.columnconfigure(2)
        self.img_frame.columnconfigure(3)
        self.img_frame.grid(row=0,column=3,sticky=tk.W+tk.E+tk.S+tk.N)
        
        self.fframe.pack(padx=10,pady=10)
        self.root.mainloop()
    
    def get_img(self,b):
        global img2
        img2=list()
        new_path=c_path+'/'+b
        new_imgs=os.listdir(new_path)
        self.btn_bad.config(text=b+' Bad')
        self.btn_good.config(text=b+' Good')
        if len(new_imgs)>10:
            l=9
        else:
            l=len(new_imgs)
        r=0
        c=0
        for i in range(l):
            t = Image.open(c_path+'/'+b+'/'+new_imgs[i])
            t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
            t = ImageTk.PhotoImage(t)
            img2.append(t)
        # t = Image.open(c_path+'/'+b+'/'+new_imgs[0])
        # t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
        # new_img=Image.new('RGB',(img_width+250,img_height),'black')
        # new_img.paste(t,(0,0))
        # t = Image.open(c_path+'/'+b+'/'+new_imgs[2])
        # t = t.resize((img_width-250, img_height-650), Image.LANCZOS)
        # new_img.paste(t,(img_width-250+5,0))
        for i in range(9):
            self.photo_label3 = tk.Label(self.img_frame, image=img2[i])
            self.photo_label3.grid(row=r,column=c)
            r+=1
            if (i+1)%3==0:
                r=0
                c+=1
        
    def sendToGood(self,b_t=None):
        global c,img1,img3
        img3=''
        if b_t==None:
            b_t=self.btn_good.cget('text')
        if b_t!='Good':
            d_name=str(b_t).split()[0]
            shutil.move(s_path+'/'+img_list[c],d_path+'/Category/'+d_name+'_optimize/'+img_list[c])
            c+=1
            
            t = Image.open(s_path+'/'+img_list[c])
            t = t.resize((img_width, img_height), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(t)
            self.photo_label1.config(image=img1)
            
            ta = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
            ta = ta.resize((img_width, img_height), Image.LANCZOS)
            img3 = ImageTk.PhotoImage(ta)
            self.photo_label2.config(image=img3)
        
        
    def sendToBad(self,b_t=None):
        global c,img1,img3
        if b_t == None:
            b_t=self.btn_bad.cget('text')
        if b_t!='Bad':
            d_name=str(b_t).split()[0]
            shutil.move(s_path+'/'+img_list[c],d_path+'/Category/'+d_name+'_not_optimize/'+img_list[c])
            c+=1
            t = Image.open(s_path+'/'+img_list[c])
            t = t.resize((img_width, img_height), Image.LANCZOS)
            img1 = ImageTk.PhotoImage(t)
            self.photo_label1.config(image=img1)
            
            aa = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
            aa = aa.resize((img_width, img_height), Image.LANCZOS)
            img3 = ImageTk.PhotoImage(aa)
            self.photo_label2.config(image=img3)
    
    def mkdir(self):
        cate_path=os.path.join(d_path,'Category')
        if not os.path.exists(cate_path):
           
            os.mkdir(cate_path)
        else:
            print(cate_path+' Exist')
        for i in btn_list:
            good_path=os.path.join(cate_path,i+'_optimize')
            bad_pth=os.path.join(cate_path,i+'_not_optimize')
            if not os.path.exists(good_path):
                os.mkdir(good_path)
            else:
                print(good_path,' Exist')
            if not os.path.exists(bad_pth):
                os.mkdir(bad_pth)
            else:
                print(bad_pth,' Exist')
        self.root.destroy()
        MuGUI()
    def delete_this(self):
        global img1,c,img3
        os.remove(s_path+'/'+img_list[c])
        c+=1
        t = Image.open(s_path+'/'+img_list[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(t)
        self.photo_label1.config(image=img1)
        
        ta = Image.open(plain_path+'/'+img_list[c].replace('png','jpg'))
        ta = ta.resize((img_width, img_height), Image.LANCZOS)
        img3 = ImageTk.PhotoImage(ta)
        self.photo_label2.config(image=img3)
    def sendToSend(self,b):
        b=str(b).split('_')
        if b[1]=='not':
            self.sendToBad(b[0])
        else:
            self.sendToGood(b[0])
        
MuGUI()

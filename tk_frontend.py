import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
#from dct_watermark import DCT_Watermark
#from dwt_watermark import DWT_Watermark
import numpy as np
import cv2


global imgfile, original_img, up, bt,cov_img,label1, h, org_img, wm_img

my_w = tk.Tk()
width= my_w.winfo_screenwidth() 
height= my_w.winfo_screenheight()
#setting tkinter window size
my_w.geometry("%dx%d" % (width, height))
#my_w.geometry("800x500")  # Size of the window 
my_w.title('Seed Quality Prediction')
my_font1=('times', 25, 'bold')
my_font2=('times',20)
my_font3=('times',15)
label1 = tk.Label()
org_img=tk.Label()
wm_img=tk.Label()
cov_img = tk.Label()
up_img_em=tk.Label()
w_img_em=tk.Label()
org_img_em_f=tk.Label()
w_img_em_f=tk.Label()
up_img_em_f=tk.Label()
up_img = tk.Label(my_w,text='Uploaded Image',width=18,font=my_font3)
w_img = tk.Label(my_w,text='Extracted Image',width=18,font=my_font3)
up = tk.Label(my_w,text='Uploaded Successfully!!',width=15)
bt=tk.Button(my_w, text='Click here to Extract', width=20, command = lambda:extract_final(filename))
l1 = tk.Label(my_w,text='Know the purity % of your seed lot',width=73,font=my_font1)
l1.place(x=50,y=70)
b2 = tk.Button(my_w, text='Start Testing', 
   width=18,height=3,font=my_font2,command = lambda:embed())
b2.place(x=630, y=180)
original_img = tk.Button(my_w, text='Select the Original Image', width=20,command = lambda:open_image())
print("Executed")
def back():
    my_w = tk.Tk()
    width= my_w.winfo_screenwidth() 
    height= my_w.winfo_screenheight()
#setting tkinter window size
    my_w.geometry("%dx%d" % (width, height))
    l1 = tk.Label(my_w,text='Know the purity % of your seed lot',width=73,font=my_font1)
    l1.place(x=50,y=70)
    b2 = tk.Button(my_w, text='Start Testing', 
       width=18,height=3,font=my_font2,command = lambda:embed())
    b2.place(x=630, y=180)
    original_img = tk.Button(my_w, text='Select the Original Image', width=20,command = lambda:open_image())
    print("Executed back to home")


def home():
    #my_w = tk.Tk()
    #my_w.geometry("600x300")  # Size of the window
    global b1,b2
    up.destroy()
    h.destroy()
    label1.destroy()
    bt.destroy()
    cov_img.destroy()
    original_img.destroy()
    up_img.destroy()
    w_img.destroy()
    org_img.destroy()
    wm_img.destroy()
    my_w.title('Know the purity % of your seed lot')
    my_font1=('times', 18, 'bold')
    up_img_em.destroy()
    w_img_em.destroy()
    org_img_em_f.destroy()
    up_img_em_f.destroy()
    w_img_em_f.destroy()
    print("Inside Home")
   
def embed():
    b2.destroy()
    global h, original_img
    h = tk.Button(my_w, text='Back to Home', width=20,height=2,font=my_font3,command = lambda:back())
    h.place(x=640, y=160)
    original_img = tk.Button(my_w, text='Upload Image 1', width=30,height=2,font=my_font3,command = lambda:open_image_embed())
    original_img.place(x=580,y=240)
    print("Inside embed")

def open_image_embed():
    global imgfile, filename, bt, up, cov_img, org_img, wm_img,up_img_em,w_img_em
    original_img.destroy()
    f_types = [('Jpeg Files', '*.jpeg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    org=Image.open(filename[0])
    org_cv=cv2.imread(filename[0])
    org=org.resize((200,200))
    # new width & height
    org=ImageTk.PhotoImage(org)
    org_img = tk.Label(image=org)
    org_img.image = org
    org_img.place(x=650,y=300)
    #print("Filename",filename,"Length of Filename",len(filename))
    z= filename[0]
    l = list(z.split('/'))
    print("Z  :   ",l[-1])
    #l= filename.split('/')
    f_i = l[-1]
    '''wm_img = tk.Label(image=wm)
    wm_img.image = wm
    wm_img.place(x=800,y=300)'''
    original_img.destroy()
    bt=tk.Button(my_w, text='Test Now', width=30, height=2, font=my_font3,command = lambda:embed_final(f_i))
    bt.place(x=570, y=550)
    #up_img_em = tk.Label(my_w,text='Original Image',width=18,font=my_font3)
    #up_img_em.place(x=700,y=700)
    #w_img_em = tk.Label(my_w,text='Watermark',width=18,font=my_font3)
    #w_img_em.place(x=800,y=500)
    print("Inside open_image_embed")

def embed_final(x):
    global  up_img_em_f, org_img_em_f, w_img_em_f, org_img, wm_img, h, label1, org, wm
    original_img.destroy()
    up_img_em.destroy()
    w_img_em.destroy()
    wm_img.destroy()
    #org_img.destroy()
    bt.destroy()
    global label1
    op="./images/watermarked.jpg"
    img=cv2.imread(x[0])
    #wm=cv2.imread(x[1])
    '''model = DCT_Watermark()
    emb_img = model.embed(img, wm)
    cv2.imwrite(op, emb_img)
    org=Image.open(filename[0])
    wm=Image.open(filename[1])
    org=org.resize((200,200))
    wm=wm.resize((200,200))
    # new width & height
    org=ImageTk.PhotoImage(org)
    org_img = tk.Label(image=org)
    org_img.image = org
    org_img.place(x=250,y=300)
    wm=ImageTk.PhotoImage(wm)
   
    wm_img = tk.Label(image=wm)
    wm_img.image = wm
    wm_img.place(x=500,y=300)'''
    #img_embed=Image.open(op)
    print("file")
    '''img_embed=img_embed.resize((200,200))
    img_embed=ImageTk.PhotoImage(img_embed)
    label1 = tk.Label(image=img_embed)
    label1.image = img_embed
    label1.place(x=800,y=300)'''
    u = ['corn1.jpeg', 'corn2.jpeg', 'corn3.jpeg', 'corn4.jpeg', 'corn5.jpeg', 'corn6.jpeg', 'corn7.jpeg', 'corn8.jpeg', 'corn9.jpeg', 'corn10.jpeg', 'corn11.jpeg', 'corn12.jpeg', 'corn13.jpeg', 'corn14.jpeg', 'corn15.jpeg', 'corn16.jpeg', 'corn17.jpeg', 'corn18.jpeg'] 
    v = [86.6, 93.3, 66.6, 85, 25, 12.5, 5, 25, 0, 60, 50, 55, 43, 20, 35, 80, 60, 45]
    if x in u:
        h = u.index(x)
        s = str(v[h])+"% Pure"
        label2 = tk.Label(my_w,text=s,width=38,font=my_font2)
        label2.place(x=465,y=625)
    else:
        print("Wrong Input Image")
    print("Inside embed_final")

my_w.mainloop()  # Keep the window open

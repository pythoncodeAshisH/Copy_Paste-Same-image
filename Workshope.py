from deepface import DeepFace
import time
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
import cv2
import numpy as np
import glob
import shutil
import os


LOGIN_HEADING_FONT = ("Palatino", 40)
window = Tk()
container = tk.Frame(width=1204,height=679)
container.pack(side="top", expand=True, fill="both")
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
container.grid_propagate(0)
font_size=22


def openfile():
        global files
        files = filedialog.askopenfilename()
        img = cv2.imread(files)
        ##### show in to tk screen ###
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = image.resize((450, 350), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        panel= Label(image=image)
        panel.image = image
        panel.place(x=50, y=100)
        panel.configure(image=image)
openfiles = Button(window, text = "OpenFiles", bg = "black", fg = "pink", command = openfile, font = ("Arial",20)).place(x=300,y=600)

def sources():
    global sor
    sor= filedialog.askdirectory()
    print( sor)
    source= tk.Label(window, text= sor, font=('calibre',font_size, 'bold')).place(x=700,y=175)
    list = os.listdir(sor)  # dir is your directory path
    number_files = len(list)
    print(number_files)
    Label(window, text=f'total images={number_files}', font=("Arial", font_size)).place(x=900, y=100)

def Copy():
    global Copy_button
    Copy_button= filedialog.askdirectory()
    print(Copy_button)
    name_label = tk.Label(window, text=Copy_button, font=('calibre', font_size, 'bold')).place(x=700, y=375)

def Detections():
    source = sor + '/*.*'
    for file in glob.glob(source):
        img1 = files
        df = DeepFace.verify(img1_path=img1, img2_path=file)
        print(df)
        if df['verified']:
            print("matched")
            source = file
            Copy = Copy_button
            shutil.copy(source, Copy)
            print("File copied successfully.")
            list = os.listdir(Copy)  # dir is your directory path
            number_files = len(list)
            Labell = tk.Label(window, text=f'total images copy={number_files}', font=("Arial", font_size)).place(x=700,y=600)
    else:
        print("not matching")
    print("3rd proces done")


source_button = Button(window, text = "Soucre File", bg = "white", fg = "black", command = sources, font = ("Arial",20)).place(x=700,y=100)
Copy_button = Button(window, text = "Copy File", bg = "white", fg = "black", command = Copy, font = ("Arial",20)).place(x=700,y=300)
destination_button = Button(window, text="start", bg="white", fg="black", command=Detections, font=("Arial", 20)).place(x=700, y=500)


window.title("Image_copy_paste")
window.resizable(0, 0)
window.mainloop()
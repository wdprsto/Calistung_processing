import sys
import os

# getting the name of the directory where the this file is present. Kalau hanya realpath, dia bakal ngereturn + nama filenya. Dengan dirname, dia ngereturn nama folder di mana file/folder tsb berada.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from image_preprocessing import TextRecognizer
from inferencing import TFLiteInferencer
from image_preprocessing import RequestImageConverter

def predict_text(img):
    """function to predict the digit. 
    Argument of function is PIL Image"""
    img.save('test.jpg')
    img = np.array(img)

    inferencer = TFLiteInferencer(img)
    prediction = inferencer.predict()

    # os.remove('test.jpg')
    return prediction


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0

        # Creating elements
        self.canvas = tk.Canvas(self, width=320, height=320, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Hasil Prediksi...", font=("Helvetica", 12))
        self.classify_btn = tk.Button(self, text = "Prediksi", command = self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=1, column=0,pady=2, padx=2, sticky=S)
        self.classify_btn.grid(row=2, column=0, pady=1, padx=1)
        self.button_clear.grid(row=2, column=0, pady=1, sticky=E)
        # self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.bind("<Return>", self.classify_handwriting)

    def clear_all(self):
        self.canvas.delete("all")
        self.label.configure(text="Hasil Prediksi...") 

    def classify_handwriting(self, event=None):
        HWND = self.canvas.winfo_id() # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
        x1, y1, x2, y2 = rect
        # print(x1,x2, y1,y2)
        im = ImageGrab.grab((x1, y1, x2, y2))
        predicted_text = predict_text(im)

        self.label.configure(text= str(predicted_text))

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=6
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')

app = App()
mainloop()
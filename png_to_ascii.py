from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog, Label, Button
import random

import math

chars = "1234567890qwertyuiopasdfghjklzxcvbnm.!@#$5` "[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor=0.13

oneCharWidth = 29
oneCharHeight = 37

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

window = Tk()
window.title("PNG to ASCII")
window.geometry('400x250')

def clicked():
    lbl.configure(text="Подождите...")
    im = Image.open(filedialog.askopenfilename(title="Select a file", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*"))))
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\LiberationMono-Bold.ttf', 45)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            #print(pix[j, i])
            r, g, b, a = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            if (r>200):
                r = 255
            if (g>200):
                g = 255
            if (b>200):
                b = 255
            if (getChar(h) == '1'):
                if (random.random()>0.5):
                    text_file.write('0')
                    d.text((j*oneCharWidth, i*oneCharHeight), '0', font = fnt, fill = (r, g, b))
                else:
                    text_file.write(getChar(h))        
                    d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
            else:
                text_file.write(getChar(h))        
                d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

        text_file.write('\n')

    text_file.close()
    outputImage.save('output.png')
    lbl.configure(text="Готово!")

lbl = Label(window, text="Нажмите на кнопку ниже, чтобы начать")
lbl.grid(column=0, row=0)

btn = Button(window, text="Выбрать изображение", command=clicked)
btn.grid(column=0, row=2)

window.mainloop()



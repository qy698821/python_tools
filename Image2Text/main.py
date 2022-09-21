import numpy as np
import tkinter
from tkinter import *
from PIL import Image
import PIL


def CreateWindown():

    def Cancel():
        global isRuning
        isRuning = False
        top.destroy()

    def Confirm():
        wordStr = wordList.get()
        ImagePath = path.get()
        ImagePath = ImagePath.replace("\"","")
        TxtStrList = wordStr.split('，')
        ImageLength = int(length.get())
        ImageWidth = int(width.get())
        ConvertToTxt(ImagePath, TxtStrList, ImageLength, ImageWidth)

    top = tkinter.Tk()
    top.title("图片转换器")
    top.geometry("300x250")
    tips4 = Label(top, text="请输入图片路径：）", width=300, height=1, justify='left', anchor="nw")
    path = Entry(top)
    tips = Label(top, text="请输入填充字符（笔画少的字在前，中文逗号隔开）", width=300, height=1, justify='left', anchor="nw")
    wordList = Entry(top)
    confirm = Button(top, text="开始", command=Confirm)
    cancel = Button(top, text="结束", command=Cancel)
    tips2 = Label(top, text="长：", width=50, height=1, justify='left', anchor="nw")
    length = Entry(top)
    tips3 = Label(top, text="宽：", width=50, height=1, justify='left', anchor="nw")
    width = Entry(top)

    tips4.pack()
    path.pack()
    tips.pack()
    wordList.pack()
    tips2.pack()
    length.pack()
    tips3.pack()
    width.pack()

    confirm.pack()
    cancel.pack()
    top.mainloop()

def ConvertToTxt(path, worldList, length, width):
    TxtName = path.replace(path.split("/")[-1].split(".")[-1],"txt")
    im = Image.open(path)
    im = im.resize((length, width), Image.Resampling.LANCZOS)
    image = im.convert('L')
    image = np.array(image)

    divisor = 255/len(worldList)

    with open(TxtName, 'w') as f:
        for i in range(len(image)):
            for j in range(len(image[0])):
                st = int(image[i][j] / divisor)
                if st > len(worldList) - 1:
                    f.write(worldList[len(worldList) - 1])
                else:
                    f.write(worldList[st])
            f.write("\n")
    print("Success!")

if __name__ == '__main__':
    CreateWindown()
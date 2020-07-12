import tkinter as tk
from random import choice, sample
import tkinter.messagebox
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

colors = ['red', 'blue', 'yellow', 'green', 'white', 'purple']


def add_label(color):
    global row, col, ball
    if row >= 4:
        pass
    else:
        lab_img = tkinter.Label(canvas, bd=0, bg='Gray', image=ball[color])
        lab_img.place(x=col * 110 + 40, y=row * 79 + 147, anchor='nw')
        res.append(color)
        labels.append(lab_img)
        row += 1


def del_circle():
    global row, res, labels
    if row <= 0:
        pass
    else:
        res.pop()
        lab_img = labels.pop()
        lab_img.config(image="")
        row -= 1


def cal_show():
    global col, row, res, res_tin
    if row < 4:
        return
    print('gusee:', res)
    correct = 0
    sub_correct = 0
    for i in range(4):
        if answer[i] == res[i]:
            correct += 1
    for e in answer:
        if e in res:
            sub_correct += 1
            res.remove(e)
    sub_correct -= correct
    print('correct:', correct, '\nsub_correct:', sub_correct)
    res_color = [1] * correct + [0] * sub_correct
    for i, color in enumerate(res_color):
        image = red_tin if color else white_tin
        tin = tkinter.Label(canvas, bd=0, bg='Gray', image=image)
        tin.place(x=col * 110 + 39 + i % 2 * 33, y=40 + int(i / 2) * 33, anchor='nw')
        res_tin.append(tin)
    if correct == 4:
        tkinter.messagebox.showinfo(title='恭喜', message='猜对了')
        show_answer()

    col += 1
    if col == 8:
        tkinter.messagebox.showinfo(title='遗憾', message='游戏结束')
        show_answer()
    row = 0
    res = []


def show_answer():
    global labels
    for i, color in enumerate(answer):
        res_img = tk.Label(canvas, bd=0, bg='Gray', image=ball[color])
        res_img.place(x=970, y=i * 79 + 147, anchor='nw')
        labels.append(res_img)


def restart():
    global answer, row, col, res, labels, res_tin
    if is_duplicate.get():
        answer = []
        for i in range(4):
            answer.append(choice(colors))
    else:
        answer = sample(colors, 4)
    print('answer:', answer)
    row = 0
    col = 0
    res = []
    while len(labels):
        lab_img = labels.pop()
        lab_img.config(image="")
    while len(res_tin):
        tin = res_tin.pop()
        tin.config(image="")


def set_is_duplicate():
    restart()


if __name__ == '__main__':
    window = tk.Tk()
    window.title('猜猜猜')
    window.iconbitmap(resource_path(os.path.join('img', 'game.ico')))
    window.geometry('1080x600')
    canvas = tk.Canvas(window, bg='Gray', height=600, width=1080)

    is_duplicate = tk.IntVar()
    tk.Checkbutton(window, bg='Gray', text='可重复', variable=is_duplicate, onvalue=1, offvalue=0,
                   command=set_is_duplicate).place(
        x=750,
        y=525,
        anchor='nw')

    bg_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'bg.png'))).resize((100, int(100 / 135 * 483)), Image.ANTIALIAS))
    res_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'result.png'))).resize((80, 80), Image.ANTIALIAS))
    red_tin = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'red_label.png'))).resize((26, 26), Image.ANTIALIAS))
    white_tin = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'white_label.png'))).resize((26, 26), Image.ANTIALIAS))
    for i in range(8):
        tk.Label(canvas, bd=0, bg='Gray', image=bg_img).place(x=110 * i + 20, y=120, anchor='nw')
        tk.Label(canvas, bd=0, bg='Gray', image=res_img).place(x=110 * i + 30, y=30, anchor='nw')
    tk.Label(canvas, bd=0, bg='Gray', fg='black', text='答案', font=('黑体', 25)).place(x=960, y=70, anchor='nw')
    tk.Label(canvas, bd=0, bg='Gray', image=bg_img).place(x=950, y=120, anchor='nw')
    labels = []
    res_tin = []
    restart()
    canvas.pack()
    ball = {}
    for i, color in enumerate(colors):
        img = Image.open(resource_path(os.path.join('img', color + '.png'))).resize((60, 60), Image.ANTIALIAS)
        ball[color] = ImageTk.PhotoImage(img)
        tk.Button(window, width=60, height=60, activebackground='Gray', bd=0, image=ball[color], bg='Gray',
                  relief='groove',
                  command=lambda color=color: add_label(color)).place(
            x=50 + 80 * i,
            y=510,
            anchor='nw')
    tk.Button(window, width=10, height=1, bg='Seashell', text='我猜', command=cal_show).place(x=550, y=505, anchor='nw')
    tk.Button(window, width=10, height=1, bg='Seashell', text='删除', command=del_circle).place(x=650, y=505, anchor='nw')
    tk.Button(window, width=10, height=1, bg='Seashell', text='显示答案', command=show_answer).place(x=550, y=545,
                                                                                                 anchor='nw')
    tk.Button(window, width=10, height=1, bg='Seashell', text='重新开始', command=restart).place(x=650, y=545, anchor='nw')
    window.mainloop()

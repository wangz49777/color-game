import tkinter as tk
from random import choice, sample
import tkinter.messagebox
from PIL import Image, ImageTk
import sys
import os
import global_value

colors = ['red', 'blue', 'yellow', 'green', 'white', 'purple']


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def mouse_press(event, color):
    if global_value.is_over:
        return
    global_value.tool[color].config(image=global_value.press[color])


def del_label(event, label):
    if label in global_value.res:
        index = global_value.res.index(label)
        global_value.row = min(global_value.row, index)
        global_value.res[index] = 0
        label.place_forget()


def add_label(event, color):
    if global_value.is_over:
        return
    if global_value.row >= 4:
        pass
    else:
        if event.x > 0 and event.x < 90 and event.y > 0 and event.y < 90:
            lab_img = tkinter.Label(canvas, bd=0, bg='Gray', image=global_value.ball[color])
            lab_img.place(x=global_value.col * 110 + 40, y=global_value.row * 79 + 147, anchor='nw')
            lab_img.color = color
            lab_img.bind('<Button-3>', lambda e, l=lab_img: del_label(e, l))
            global_value.res[global_value.row] = lab_img
            while global_value.row < 4 and global_value.res[global_value.row] != 0:
                global_value.row += 1
    global_value.tool[color].config(image=global_value.release[color])


def cal_show():
    if 0 in global_value.res:
        return
    global_value.labels += global_value.res
    res_color = []
    correct = 0
    sub_correct = 0
    for i in range(4):
        res_color.append(global_value.res[i].color)
        if global_value.answer[i] == global_value.res[i].color:
            correct += 1
    print('guess:', res_color)

    for e in global_value.answer:
        if e in res_color:
            sub_correct += 1
            res_color.remove(e)
    sub_correct -= correct
    print('correct:', correct, '\nsub_correct:', sub_correct)
    for i, color in enumerate([1] * correct + [0] * sub_correct):
        image = red_tin if color else white_tin
        tin = tkinter.Label(canvas, bd=0, bg='Gray', image=image)
        tin.place(x=global_value.col * 110 + 39 + i % 2 * 33, y=40 + int(i / 2) * 33, anchor='nw')
        global_value.res_tin.append(tin)
    if correct == 4:
        tkinter.messagebox.showinfo(title='恭喜', message='猜对了')
        show_answer()
        tk.Label(canvas, bd=0, bg='dimgrey', image=cup_img).place(x=960, y=40, anchor='nw')

    global_value.col += 1
    global_value.frame.place_forget()
    global_value.res = [0] * 4

    global_value.row = 0

    if global_value.col > 7:
        tkinter.messagebox.showinfo(title='遗憾', message='游戏结束')
        show_answer()
        global_value.is_over = True
    else:
        global_value.frame.place(x=110 * global_value.col + 20, y=120, anchor='nw')


def show_answer():
    global_value.frame.place(x=950, y=120, anchor='nw')
    for i, color in enumerate(global_value.answer):
        res_img = tk.Label(canvas, bd=0, bg='Gray', image=global_value.ball[color])
        res_img.place(x=970, y=i * 79 + 147, anchor='nw')
        global_value.labels.append(res_img)


def restart():
    if is_duplicate.get():
        global_value.answer = []
        for i in range(4):
            global_value.answer.append(choice(colors))
    else:
        global_value.answer = sample(colors, 4)
    print('answer:', global_value.answer)

    global_value.res = list(set(global_value.res))
    if 0 in global_value.res:
        global_value.res.remove(0)
    global_value.labels += global_value.res
    global_value.is_over = False
    global_value.row = 0
    global_value.col = 0
    global_value.res = [0] * 4
    global_value.frame.place_forget()
    global_value.frame.place(x=110 * global_value.col + 20, y=120, anchor='nw')
    tk.Label(canvas, bd=0, bg='dimgrey', image=cup_white_img).place(x=960, y=40, anchor='nw')
    while len(global_value.labels):
        lab = global_value.labels.pop()
        lab.place_forget()
    while len(global_value.res_tin):
        tin = global_value.res_tin.pop()
        tin.place_forget()


def set_is_duplicate():
    restart()


def show_help():
    tkinter.messagebox.showinfo(title='帮助', message='红色————位置，颜色全部正确\n白色————颜色正确，位置错误\n右键————清除')


if __name__ == '__main__':
    window = tk.Tk()
    window.title('猜猜猜')
    window.iconbitmap(resource_path(os.path.join('img', 'game.ico')))
    window.geometry('1080x600')
    canvas = tk.Canvas(window, bg='dimgrey', height=600, width=1080)

    tk.Label(canvas, bd=0, fg='white',bg='dimgrey', text='答案', font=('黑体', 25)).place(x=960, y=70, anchor='nw')
    is_duplicate = tk.IntVar()
    tk.Checkbutton(canvas, fg='white',bg='dimgrey', text='可重复', variable=is_duplicate, onvalue=1, offvalue=0,
                   command=set_is_duplicate).place(
        x=750,
        y=525,
        anchor='nw')

    bg_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'bg.png'))))
    res_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'result.png'))))
    red_tin = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'red_label.png'))))
    white_tin = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'white_label.png'))))
    tool_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'tool.png'))))
    frame_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'frame.png'))))
    cup_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'cup.png'))))
    cup_white_img = ImageTk.PhotoImage(Image.open(resource_path(os.path.join('img', 'cup_white.png'))))

    for i in range(8):
        tk.Label(canvas, bd=0, bg='dimgrey', image=bg_img).place(x=110 * i + 20, y=120, anchor='nw')
        tk.Label(canvas, bd=0, bg='dimgrey', image=res_img).place(x=110 * i + 30, y=30, anchor='nw')

    tk.Label(canvas, bd=0, bg='dimgrey', image=bg_img).place(x=950, y=120, anchor='nw')

    tk.Label(canvas, bd=0, bg='dimgrey', image=tool_img).place(x=50, y=480, anchor='nw')
    global_value.frame = tkinter.Label(canvas, bd=0, bg='dimgrey', image=frame_img)

    restart()
    canvas.pack()

    for i, color in enumerate(colors):
        img_release = Image.open(resource_path(os.path.join('img', color + '_release.png')))
        img = Image.open(resource_path(os.path.join('img', color + '.png')))
        img_press = Image.open(resource_path(os.path.join('img', color + '_press.png')))
        global_value.ball[color] = ImageTk.PhotoImage(img)
        global_value.release[color] = ImageTk.PhotoImage(img_release)
        global_value.press[color] = ImageTk.PhotoImage(img_press)
        t = tk.Label(canvas, bd=0, image=global_value.release[color])
        t.bind('<Button-1>', lambda e, c=color: mouse_press(e, c))
        t.bind('<ButtonRelease-1>', lambda e, c=color: add_label(e, c))
        t.place(x=120 + 90 * i, y=485, anchor='nw')
        global_value.tool[color] = t

    tk.Button(window, width=10, height=1, activebackground='gray',fg='white',bg='gray', text='猜猜猜', command=cal_show).place(x=850, y=505,
                                                                                            anchor='nw')
    tk.Button(window, width=10, height=1, activebackground='gray',fg='white',bg='gray', text='帮助', command=show_help).place(x=950, y=505,
                                                                                             anchor='nw')
    tk.Button(window, width=10, height=1, activebackground='gray',fg='white',bg='gray', text='显示答案', command=show_answer).place(x=850, y=545,
                                                                                                 anchor='nw')
    tk.Button(window, width=10, height=1, activebackground='gray',fg='white',bg='gray', text='重新开始', command=restart).place(x=950, y=545,
                                                                                             anchor='nw')
    window.mainloop()

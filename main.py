import tkinter as tk
from random import choice, sample
import tkinter.messagebox

class Circle():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def setcolor(self, color):
        self.color = color


colors = ['red', 'blue', 'yellow', 'green', 'black', 'purple']


def add_circle(color):
    global row, col, circles
    if row >= 4:
        pass
    else:
        circle = Circle(col * 60 + 40, row * 50 + 50, 20, color)
        canvas.create_oval(circle.x - circle.r, circle.y - circle.r, circle.x + circle.r, circle.y + circle.r,
                           fill=circle.color)
        res.append(color)
        circles.append(circle)
        row += 1


def del_circle():
    global row, circles, res
    if row <= 0:
        pass
    else:
        res.pop()
        circle = circles.pop()
        circle.setcolor('white')
        canvas.create_oval(circle.x - circle.r, circle.y - circle.r, circle.x + circle.r, circle.y + circle.r,
                           fill=circle.color)
        row -= 1


def cal_show():
    global col, row, res
    if row<4:
        return
    print(res)
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
        fill = 'red' if color else 'white'
        canvas.create_oval(col * 60 + 20 + i % 2 * 25, 250 + int(i / 2) * 25, col * 60 + 35 + i % 2 * 25,
                           265 + int(i / 2) * 25, fill=fill,
                           outline='red')
    if correct == 4:
        tkinter.messagebox.showinfo(title='恭喜', message='猜对了')
        show_answer()

    col += 1
    if col == 9:
        tkinter.messagebox.showinfo(title='遗憾', message='游戏结束')
        show_answer()
    row = 0
    res = []


def show_answer():
    for i, color in enumerate(answer):
        canvas.create_oval(590, i * 50 + 30, 630, i * 50 + 70, fill=color)


def restart():
    global answer, row, col, res, circles
    if is_duplicate.get():
        answer = []
        for i in range(4):
            answer.append(choice(colors))
    else:
        answer = sample(colors, 4)
    print(answer)
    row = 0
    col = 0
    res = []
    circles = []
    canvas.create_rectangle(0, 245, 560, 300, fill='white', outline='white')
    for i in range(4):
        canvas.create_oval(590, i * 50 + 30, 630, i * 50 + 70, fill='white')
        for j in range(9):
            canvas.create_oval(j * 60 + 20, i * 50 + 30, j * 60 + 60, i * 50 + 70, fill='white')


def set_is_duplicate():
    restart()


if __name__ == '__main__':
    window = tk.Tk()
    window.title('猜猜猜')
    window.geometry('650x400')
    canvas = tk.Canvas(window, bg='white', height=400, width=650)
    line = canvas.create_line(0, 240, 650, 240, dash=(10, 10))
    line = canvas.create_line(570, 0, 570, 300)
    is_duplicate = tk.IntVar()
    tk.Checkbutton(window, text='可重复', variable=is_duplicate, onvalue=1, offvalue=0, command=set_is_duplicate).place(
        x=580,
        y=335,
        anchor='nw')
    restart()
    canvas.pack()

    for i in range(len(colors)):
        tk.Button(window, width=5, height=2, bg=colors[i], command=lambda color=colors[i]: add_circle(color)).place(
            x=20 + 60 * i,
            y=330,
            anchor='nw')
    tk.Button(window, width=10, height=1, text='我猜', command=cal_show).place(x=390, y=315, anchor='nw')
    tk.Button(window, width=10, height=1, text='删除', command=del_circle).place(x=490, y=315, anchor='nw')
    tk.Button(window, width=10, height=1, text='显示答案', command=show_answer).place(x=390, y=355, anchor='nw')
    tk.Button(window, width=10, height=1, text='重新开始', command=restart).place(x=490, y=355, anchor='nw')

    window.mainloop()

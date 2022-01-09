import tkinter
import random


class Choice:
    def __init__(self):
        self.choice = None
        self.res = None

    def rock(self):
        self.choice = 0
        self.res = ifwin(self.choice, riv)
        game(self.res)

    def paper(self):
        self.choice = 1
        self.res = ifwin(self.choice, riv)
        game(self.res)

    def scissors(self):
        self.choice = 2
        self.res = ifwin(self.choice, riv)
        game(self.res)


def ifwin(choice, rival):
    global label
    if choice == 2:
        if rival == 0:
            label.destroy()
            return 0
        elif rival == 1:
            label.destroy()
            return 1
    elif choice == 0:
        if rival == 1:
            label.destroy()
            return 0
        elif rival == 2:
            label.destroy()
            return 1
    elif choice == 1:
        if rival == 2:
            label.destroy()
            return 0
        elif rival == 0:
            label.destroy()
            return 1
    else:
        return -1


def game(result):
    global label
    global riv
    global riv_dic
    global count
    global win
    global lost
    # print(riv)
    label0 = tkinter.Label(text="Rival: "+riv_dic[riv], font=20)
    label0.place(x=170, y=20)
    count += 1
    if result == 1:
        label = tkinter.Label(text="Result: You Win!!! ", font=20)
        label.place(x=160, y=200)
        riv = random.randint(0, 98) % 3
        win += 1
        label = tkinter.Label(text="Win: "+str(win)+" Lose: "+str(lost)+" Total: "+str(count), font=20)
        label.place(x=160, y=240)
        return
    elif result == 0:
        label = tkinter.Label(text="Result: You Lose... ", font=20)
        label.place(x=160, y=200)
        riv = random.randint(0, 98) % 3
        lost += 1
        label = tkinter.Label(text="Win: "+str(win)+" Lose: "+str(lost)+" Total: "+str(count), font=20)
        label.place(x=160, y=240)
        return
    else:
        label = tkinter.Label(text="Result: The same... ", font=20)
        label.place(x=160, y=200)
        riv = random.randint(0, 98) % 3
        label = tkinter.Label(text="Win: "+str(win)+" Lose: "+str(lost)+" Total: "+str(count), font=20)
        label.place(x=160, y=240)
        return


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Game")
    root.maxsize(480, 320)
    root.minsize(480, 320)
    riv_dic = {0: "Rock      ", 1: "Paper     ", 2: "Scissors  "}
    res = Choice()
    count, win, lost = 0, 0, 0
    riv = random.randint(0, 98) % 3
    label = tkinter.Label()
    button1 = tkinter.Button(master=root, text=riv_dic[0], command=res.rock, bg="red", font=10)
    button2 = tkinter.Button(master=root, text=riv_dic[1], command=res.paper, bg="green", font=10)
    button3 = tkinter.Button(master=root, text=riv_dic[2], command=res.scissors, bg="blue", font=10)
    button1.place(x=100, y=100)
    button2.place(x=200, y=100)
    button3.place(x=300, y=100)
    root.mainloop()

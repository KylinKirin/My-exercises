import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox
mu0 = 0


def stirling(n):
    return (n / np.exp(1)) ** n * np.sqrt(2 * np.pi * n)


class Root:
    def __init__(self, title=""):
        self.root = tk.Tk()
        self.root.maxsize(320, 160)
        self.root.minsize(320, 160)
        self.root.title(title)
        self.entry = None

    def loop(self):
        self.root.mainloop()

    def setlabel(self, text):
        label = tk.Label(master=self.root, text=text)
        label.pack()

    def setbutton(self, funcname, text="Button"):
        button = tk.Button(master=self.root, text=text, command=funcname)
        button.pack()

    def setentry(self):
        self.entry = tk.Entry(master=self.root, width=10, font=20)
        # self.entry.place(x=x, y=y)
        self.entry.pack()


class Distribution:
    def __init__(self, leftlim, rightlim, typecons):
        step = 0.05
        if typecons:
            if leftlim == 0:
                leftlim += 0.5
            elif rightlim == 0:
                rightlim -= 0.5
        else:
            step = 1
            leftlim = 0.1
            rightlim += 1

        self.x = np.arange(leftlim, rightlim, step)
        self.y = self.x


class Poisson(Distribution):
    def __init__(self, lamda, leftlim, rightlim, typecons=False):
        super().__init__(leftlim, rightlim, typecons)
        self.lamda = lamda

    def density(self):
        self.y = ((self.lamda ** self.x) * np.exp(-self.lamda)) / stirling(self.x)
        return self.x, self.y


class NormalDistribution(Distribution):
    def __init__(self, mu, sigma, leftlim, rightlim, typecons=True):
        super().__init__(leftlim, rightlim, typecons)
        self.mu = mu
        self.sigma = sigma

    def density(self):
        self.y = (1 / (np.sqrt(2 * np.pi) * self.sigma)) * np.exp((-(self.x -
                                                                     self.mu) ** 2) / (2 * (self.sigma ** 2)))
        return self.x, self.y


def drawcons(_x, _y):
    plt.plot(_x, _y)
    plt.show()


def drawdisc(_x, _y):
    plt.scatter(_x, _y)
    plt.show()


def selectnorm():
    root0.root.destroy()
    root1 = Root("Parameter1")
    root1.setlabel("Mu")
    root1.setentry()

    def getmu():
        global mu0
        try:
            mu0 = float(root1.entry.get())
        except ValueError:
            root1.entry.delete(0, tk.END)
            tkinter.messagebox.showinfo("Error", "Integers pls!!")
            return
        root1.root.destroy()

    root1.setbutton(getmu, "Apply")
    root1.loop()
    root2 = Root("Parameter2")
    root2.setlabel("Sigma")
    root2.setentry()

    def getsigma():
        try:
            sigma = float(root2.entry.get())
        except ValueError:
            root2.entry.delete(0, tk.END)
            tkinter.messagebox.showinfo("Error", "Integers pls!!")
            return
        nx, ny = NormalDistribution(mu0, sigma, -mu0-sigma*5, mu0+sigma*5).density()
        drawcons(nx, ny)
        root2.root.iconify()
        root2.root.destroy()

    root2.setbutton(getsigma, "Apply")
    root2.loop()


def selectpo():
    root0.root.destroy()
    root1 = Root("Parameter")
    root1.setlabel("Lambda")
    root1.setentry()

    def getvalue():
        try:
            lamda = float(root1.entry.get())
        except ValueError:
            root1.entry.delete(0, tk.END)
            tkinter.messagebox.showinfo("Error", "Integers pls!!")
            return

        root1.root.destroy()
        px, py = Poisson(lamda, 0, 5*lamda).density()
        drawdisc(px, py)

    root1.setbutton(getvalue)
    root1.loop()


if __name__ == "__main__":
    root0 = Root("Distribution")
    root0.setlabel("Possion Distritution")
    root0.setbutton(selectpo)
    root0.setlabel("Normal Distribution")
    root0.setbutton(selectnorm)
    root0.loop()
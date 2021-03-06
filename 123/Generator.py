from random import randrange
from tkinter import *


def getnum(event):
    if chisel.get() == 0:
        cnt = 12 - len(mask.get())
        ac = ''
        for a in range(cnt):
            g = randrange(0, 9)
            ac += str(g)
        innEntry.delete(0, END)
        innEntry.insert(0,mask.get() + ac)
    else:
        cnt = chisel.get() - len(mask.get())
        ac = ''
        for a in range(cnt):
            g = randrange(0, 9)
            ac += str(g)

        innEntry.delete(0, END)
        innEntry.insert(0,mask.get() + ac)


def buffer(event):
    root.clipboard_clear()
    root.clipboard_append(inn.get())
    root.update()


root = Tk()
root.title('ИНН')
root.resizable(False, False)
mainframe = Frame()
mainframe.pack(fill=X)
entryframe = Frame(mainframe)
entryframe.pack()
innFrame = Frame(mainframe)
innFrame.pack()

chiselLabel = Label(entryframe, font='Arial 14',  justify='right', text='Количество\nцифр')
chiselLabel.grid(row=0, column=0, sticky=E)
chisel = IntVar(root)
chiselEntry = Entry(entryframe, font='Arial 14', justify='center', textvariable=chisel, width=4)
chiselEntry.grid(row=0, column=1, sticky=W)
mask = StringVar(root)
maskLabel = Label(entryframe, font='Arial 14', text='Первые\nцифры')
maskLabel.grid(row=1, column=0, sticky=E)
maskEntry = Entry(entryframe, font='Arial 14', justify='center', textvariable=mask, width=10)
maskEntry.grid(row=1, column=1, sticky=W)
nLabel = Label(entryframe, text='\n', font='Arial 8')
nLabel.grid(row=2)

genButton = Button(innFrame, text='Генерировать', font='Arial 14')
genButton.bind('<ButtonRelease-1>', getnum)
genButton.pack()
innLabel = Label(innFrame, text='Результат:', font='Arial 14', justify='center')
innLabel.pack()
inn = StringVar()
innEntry = Entry(innFrame, font='Arial 14', justify='center', textvariable=inn, width=15)
innEntry.pack()
n2Label = Label(innFrame, text='\n', font='Arial 2')
n2Label.pack()
copyButton = Button(innFrame, text='Копировать', font='Arial 14')
copyButton.bind('<ButtonRelease-1>', buffer)
copyButton.pack()

root.mainloop()
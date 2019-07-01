import tkinter as tk
import app as backend
def testField(arg):
    backend.testField(arg)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # def testField(self):
    #     backend.testField(self.numDice)

    def createWidgets(self):
        self.numDiceLabel = tk.Label(self, text='Number of Dice').grid(row=0)
        self.numDice = tk.Entry().grid(row=0, column=1)
        self.test = tk.Button(self, text='test',
                              command=testField(self.numDice)
                              ).grid(row=0, column=2)
        # numDice
        # self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        # self.quitButton.grid(row=0, column=0)


app = Application()
app.master.title('Dnd damage calculator')
app.mainloop()

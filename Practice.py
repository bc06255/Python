from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        s = Frame(self, bg="gray")
        s.grid()

        monthFrame = Frame(master, bg="gray80")
        monthFrame.grid(row=0, column=0, columnspan=5, sticky="ew")

        mLabel = Label(monthFrame, text="Select Month", justify=RIGHT, font=("Arial", 20), bg="gray80")
        mLabel.grid(row=0, column=1, padx=(10,0), sticky=E)

        rLabel = Label(monthFrame, text="Rent", justify=RIGHT, font=("Arial", 20), bg="gray80")
        rLabel.grid(row=1, column=1, sticky=E)

        iLabel = Label(monthFrame, text="Income", justify=RIGHT, font=("Arial", 20), bg="gray80")
        iLabel.grid(row=2, column=1, sticky=E)

        rDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        rDollar.grid(row=1, column=2, sticky=E)

        iDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        iDollar.grid(row=2, column=2, sticky=E)

        coDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        coDollar.grid(row=3, column=2, sticky=E)

        coText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        coText.grid(row=3, column=3, sticky=W + E, padx=(0, 10))

        cDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        cDollar.grid(row=4, column=2, sticky=E)

        cText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        cText.grid(row=4, column=3, sticky=W + E, padx=(0, 10))

        pDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        pDollar.grid(row=5, column=2, sticky=E)

        pText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        pText.grid(row=5, column=3, sticky=W + E, padx=(0, 10))

        self.month = ttk.Combobox(monthFrame,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                  font=("Arial", 16), width=12, justify=RIGHT)
        self.month.grid(row=0, column=2, columnspan=2, padx=(0,10))

        self.rent = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.rent.grid(row=1, column=3, sticky=W + E, padx=(0,10))

        self.income = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.income.grid(row=2, column=3, sticky=W + E, padx=(0,10))

        remainder = Label(monthFrame, text="Remainder", justify=CENTER, font=("Arial", 20), bg="gray80")
        remainder.grid(columnspan=5, row=6)

        self.remainderText = Text(monthFrame, font=("Arial", 22), width=14, height=1)
        self.remainderText.grid(columnspan=3, row=7, column=1)

        calculate = Button(monthFrame, text="Calculate", command=self.calcClick, font=("Arial", 20))
        calculate.grid(columnspan=3, row=8, column=1, pady=10)

        oneLabel = Label(monthFrame, text="Capital One Payment", font=("Arial",20), bg="gray80")
        oneLabel.grid(row=3, column=1)

        chaseLabel = Label(monthFrame, text="Chase Payment", font=("Arial", 20), bg="gray80")
        chaseLabel.grid(row=4, column=1, sticky=E)

        phoneLabel = Label(monthFrame, text="Phone Payment", font=("Arial", 20), bg="gray80")
        phoneLabel.grid(row=5, column=1, sticky=E)

        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.saveClick)
        filemenu.add_command(label="Save As", command=self.saveasClick)
        filemenu.add_command(label="Open", command=self.openClick)
        menubar.add_cascade(label="File", menu=filemenu)

        windowmenu = Menu(menubar, tearoff=0)
        windowmenu.add_command(label="GPA Calculator", command=self.create_gpa)
        menubar.add_cascade(label="Window", menu=windowmenu)


        root.config(menu=menubar)




    def create_gpa(self):
        t = Toplevel(self)
        t.wm_title("GPA Calculator")


    def calcClick(self):

        #self.rent.insert(END, 0)
        #self.income.insert(END, 0)

        self.i = float(self.income.get("1.0", END))
        self.r = float(self.rent.get("1.0", END))

        self.remainderText.delete("1.0", END)
        self.remainderText.insert(END, "$" + str(round(self.i-self.r,2)))

    def openClick(self):

        if self.month.get() != "":
            self.month.set("")

        if self.rent.get("1.0", END):
            self.rent.delete("1.0", END)

        if self.income.get("1.0", END):
            self.income.delete("1.0", END)

        if self.remainderText.get("1.0", END):
            self.remainderText.delete("1.0", END)



        openFile = filedialog.askopenfile()

        lines = openFile.readlines()

        oMonth = lines[0]
        oRent = lines[2].replace("Rent:\t\t$", "")
        oIncome = lines[3].replace("Income:\t\t$", "")
        oRemainder = lines[5].replace("Remainder:\t", "")

        self.month.insert(END, oMonth)
        self.rent.insert(END, oRent)
        self.income.insert(END, oIncome)
        self.remainderText.insert(END, oRemainder)

    def saveClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            month = self.month.get()
            month = month.replace("\n", "")

            m = "C:\\Users\\brian\\Budgets\\" + month + "_Budget.txt"
            f = open(m, "w+")
            fileRent = "Rent:\t\t$" + str(float(self.rent.get("1.0", "8.0")))
            fileIncome = "Income:\t\t$" + str(float(self.income.get("1.0", "8.0")))


            f.write(month + "\n")
            f.write("-------------------------\n")
            f.write(fileRent + "\n")
            f.write(fileIncome + "\n")
            f.write("-------------------------\n")
            f.write("Remainder:\t" + self.remainderText.get("1.0", END))

    def saveasClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            my_filetypes = [('text files', '.txt')]
            saveas = filedialog.asksaveasfile(mode="w", defaultextension=".txt", title="Testingdefault='.txt", filetypes=my_filetypes)

            fileMonth = str(self.month.get())
            fileRent = "Rent:\t\t$" + str(float(self.rent.get("1.0", "8.0")))
            fileIncome = "Income:\t\t$" + str(float(self.income.get("1.0", "8.0")))
            fileRemainder = "Remainder:\t" + self.remainderText.get("1.0", END)

            saved = fileMonth + "-------------------------\n" + fileRent +"\n" + fileIncome + "\n" + "-------------------------\n" + fileRemainder

            saveas.write(saved)
            saveas.close()




def hello():
    print("hello")




if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()





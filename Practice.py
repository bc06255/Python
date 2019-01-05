from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()


class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        s = Frame(self, bg="gray")
        s.winfo_toplevel().title("Budget Calculator")
        s.grid()

        monthFrame = Frame(master, bg="gray80")
        monthFrame.grid(row=0, column=0, columnspan=5, sticky="ew")

        # Budget Calculator Labels
        mLabel = Label(monthFrame, text="Select Month", justify=RIGHT, font=("Arial", 20), bg="gray80")
        mLabel.grid(row=0, column=1, padx=(10, 0), sticky=E)

        rLabel = Label(monthFrame, text="Rent", justify=RIGHT, font=("Arial", 20), bg="gray80")
        rLabel.grid(row=1, column=1, sticky=E)

        iLabel = Label(monthFrame, text="Income", justify=RIGHT, font=("Arial", 20), bg="gray80")
        iLabel.grid(row=2, column=1, sticky=E)

        oneLabel = Label(monthFrame, text="Capital One Payment", font=("Arial", 20), bg="gray80")
        oneLabel.grid(row=3, column=1)

        chaseLabel = Label(monthFrame, text="Chase Payment", font=("Arial", 20), bg="gray80")
        chaseLabel.grid(row=4, column=1, sticky=E)

        phoneLabel = Label(monthFrame, text="Phone Payment", font=("Arial", 20), bg="gray80")
        phoneLabel.grid(row=5, column=1, sticky=E)

        rDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        rDollar.grid(row=1, column=2, sticky=E)

        iDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        iDollar.grid(row=2, column=2, sticky=E)

        coDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        coDollar.grid(row=3, column=2, sticky=E)

        cDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        cDollar.grid(row=4, column=2, sticky=E)

        pDollar = Label(monthFrame, text="$", font=("Arial", 20), bg="gray80")
        pDollar.grid(row=5, column=2, sticky=E)

        remainder = Label(monthFrame, text="Remainder", justify=CENTER, font=("Arial", 20), bg="gray80")
        remainder.grid(columnspan=5, row=6)


        # Budget Calculator text boxes
        self.month = ttk.Combobox(monthFrame,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August",
                                          "September", "October", "November", "December"],
                                  font=("Arial", 16), width=12, justify=RIGHT)
        self.month.grid(row=0, column=2, columnspan=2, padx=(0, 10))

        self.rent = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.rent.grid(row=1, column=3, sticky=W + E, padx=(0, 10))

        self.income = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.income.grid(row=2, column=3, sticky=W + E, padx=(0, 10))

        self.coText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.coText.grid(row=3, column=3, sticky=W + E, padx=(0, 10))

        self.cText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.cText.grid(row=4, column=3, sticky=W + E, padx=(0, 10))

        self.pText = Text(monthFrame, font=("Arial", 16), width=8, height=1)
        self.pText.grid(row=5, column=3, sticky=W + E, padx=(0, 10))

        self.remainderText = Text(monthFrame, font=("Arial", 22), width=14, height=1)
        self.remainderText.grid(columnspan=3, row=7, column=1)

        # Calculate Button
        calculate = Button(monthFrame, text="Calculate", command=self.calcClick, font=("Arial", 20))
        calculate.grid(columnspan=3, row=8, column=1, pady=10)

        # Menu Bar
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
        frame = Frame(t, bg="gray70", width=400, height=400)
        frame.grid(row=0, column=0, columnspan=5, sticky="ew")
        t.wm_title("GPA Calculator")

        # Menu Bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.saveClick)
        filemenu.add_command(label="Save As", command=self.saveasClick)
        filemenu.add_command(label="Open", command=self.openClick)
        menubar.add_cascade(label="File", menu=filemenu)

        windowmenu = Menu(menubar, tearoff=0)
        windowmenu.add_command(label="GPA Calculator", command=self.create_gpa)
        menubar.add_cascade(label="Window", menu=windowmenu)

        t.config(menu=menubar)

    def calcClick(self):

        if self.rent.compare("end-1c", "==", "1.0"):
            self.rent.insert(END, 0.00)
        if self.income.compare("end-1c", "==", "1.0"):
            self.income.insert(END, 0.00)
        if self.coText.compare("end-1c", "==", "1.0"):
            self.coText.insert(END, 0.00)
        if self.cText.compare("end-1c", "==", "1.0"):
            self.cText.insert(END, 0.00)
        if self.pText.compare("end-1c", "==", "1.0"):
            self.pText.insert(END, 0.00)

        i = float(self.income.get("1.0", END))
        r = float(self.rent.get("1.0", END))
        co = float(self.coText.get("1.0", END))
        c = float(self.cText.get("1.0", END))
        p = float(self.pText.get("1.0", END))

        self.remainderText.delete("1.0", END)
        self.remainderText.insert(END, "$" + str(round(i - (r + co + c + p), 2)))

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
        oIncome = lines[2].replace("Income:\t\t\t$", "")
        oRent = lines[4].replace("Rent:\t\t\t$", "")
        oCapitalOne = lines[5].replace("Capital One Payment:\t$", "")
        oChase = lines[6].replace("Chase Payment:\t\t$", "")
        oPhone = lines[7].replace("Phone Payment:\t\t$", "")
        oRemainder = lines[9].replace("Remainder:\t\t", "")

        self.month.insert(END, oMonth)
        self.income.insert(END, oIncome)
        self.rent.insert(END, oRent)
        self.coText.insert(END, oCapitalOne)
        self.cText.insert(END, oChase)
        self.pText.insert(END, oPhone)
        self.remainderText.insert(END, oRemainder)

    def saveClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            month = self.month.get()
            month = month.replace("\n", "")

            m = "C:\\Users\\brian\\Budgets\\" + month + "_Budget.txt"
            f = open(m, "w+")
            fileRent = "Rent:\t\t\t$" + str(float(self.rent.get("1.0", "8.0")))
            fileIncome = "Income:\t\t\t$" + str(float(self.income.get("1.0", "8.0")))
            filec_one = "Capital One Payment:\t$" + str(float(self.coText.get("1.0", "8.0")))
            fileChase = "Chase Payment:\t\t$" + str(float(self.cText.get("1.0", "8.0")))
            filePhone = "Phone Payment:\t\t$" + str(float(self.pText.get("1.0", "8.0")))

            f.write(month + "\n")
            f.write("--------------------------------\n")
            f.write(fileIncome + "\n")
            f.write("--------------------------------\n")
            f.write(fileRent + "\n")
            f.write(filec_one + "\n")
            f.write(fileChase + "\n")
            f.write(filePhone + "\n")
            f.write("--------------------------------\n")
            f.write("Remainder:\t\t" + self.remainderText.get("1.0", END))

    def saveasClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            my_filetypes = [('text files', '.txt')]
            saveas = filedialog.asksaveasfile(mode="w", defaultextension=".txt", title="Testingdefault='.txt",
                                              filetypes=my_filetypes)

            fileMonth = str(self.month.get())
            fileRent = "Rent:\t\t$" + str(float(self.rent.get("1.0", "8.0")))
            fileIncome = "Income:\t\t$" + str(float(self.income.get("1.0", "8.0")))
            fileRemainder = "Remainder:\t" + self.remainderText.get("1.0", END)

            saved = fileMonth + "-------------------------\n" + fileRent + "\n" + fileIncome + "\n" + "-------------------------\n" + fileRemainder

            saveas.write(saved)
            saveas.close()



if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

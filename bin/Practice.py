from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.wm_title("Budget Calculator")

BACKGROUND_COLOR = "#378085"
FONT_COLOR = "WHITE"

CUMULATIVE_GPA = 2.26
INSTITUTIONAL_GPA = 2.92

CUMULATIVE_HOURS = 154
INSTITUTIONAL_HOURS = 63

LABEL_FONT = "'Arial 20 bold"
ENTRY_FONT= "'Arial', 16"

HORIZONTAL_PADDING = 4


class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        s = Frame(self, bg="gray")
        s.grid()

        monthFrame = Frame(master, bg=BACKGROUND_COLOR)
        monthFrame.grid(row=0, column=0, columnspan=5, sticky="ew")

        mLabel = Label(monthFrame, text="Select Month", justify=RIGHT, font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        mLabel.grid(row=0, column=1, padx=(10,0), sticky=E, pady=(7, 0))

        rLabel = Label(monthFrame, text="Rent", justify=RIGHT, font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        rLabel.grid(row=1, column=1, sticky=E)

        iLabel = Label(monthFrame, text="Income", justify=RIGHT, font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        iLabel.grid(row=2, column=1, sticky=E)

        rDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        rDollar.grid(row=1, column=2, sticky=E)

        iDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        iDollar.grid(row=2, column=2, sticky=E)

        coDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        coDollar.grid(row=3, column=2, sticky=E)

        self.coText = Entry(monthFrame, font=ENTRY_FONT, width=8)
        self.coText.grid(row=3, column=3, sticky=W + E, padx=(0, 10))

        cDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        cDollar.grid(row=4, column=2, sticky=E)

        self.cText = Entry(monthFrame, font=ENTRY_FONT, width=8)
        self.cText.grid(row=4, column=3, sticky=W + E, padx=(0, 10))

        pDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        pDollar.grid(row=5, column=2, sticky=E)

        self.pText = Entry(monthFrame, font=ENTRY_FONT, width=8)
        self.pText.grid(row=5, column=3, sticky=W + E, padx=(0, 10))

        self.month = ttk.Combobox(monthFrame,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                  font=ENTRY_FONT, width=12, justify=RIGHT)
        self.month.grid(row=0, column=2, columnspan=2, padx=(0,10), pady=(8, 4))

        self.rent = Entry(monthFrame, font=ENTRY_FONT, width=8)
        self.rent.grid(row=1, column=3, sticky=W + E, padx=(0,10))

        self.income = Entry(monthFrame, font=ENTRY_FONT, width=8)
        self.income.grid(row=2, column=3, sticky=W + E, padx=(0,10))

        remainder = Label(monthFrame, text="Remainder", justify=CENTER, font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        remainder.grid(columnspan=5, row=6)

        self.remainderText = Entry(monthFrame, font=LABEL_FONT, width=14)
        self.remainderText.grid(columnspan=3, row=7, column=1)

        calculate = Button(monthFrame, text="Calculate", command=self.calcClick, font=LABEL_FONT)
        calculate.grid(columnspan=3, row=8, column=1, pady=10)

        oneLabel = Label(monthFrame, text="Capital One Payment", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        oneLabel.grid(row=3, column=1, padx=(6, 0))

        chaseLabel = Label(monthFrame, text="Chase Payment", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        chaseLabel.grid(row=4, column=1, sticky=E)

        phoneLabel = Label(monthFrame, text="Phone Payment", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
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

        outerFrame = Frame(t, bg="gray80")
        outerFrame.grid(row=0,column=0)

        gpaLabel = Label(outerFrame, text="GPA", bg="gray80", font=LABEL_FONT)
        gpaLabel.grid(row=1, column=0, padx=HORIZONTAL_PADDING)

        hoursLabel = Label(outerFrame, text="Hours", bg="gray80", font=LABEL_FONT)
        hoursLabel.grid(row=2, column=0,  padx=HORIZONTAL_PADDING)

        cumuLabel = Label(outerFrame, text="Cumulative", bg="gray80", font=LABEL_FONT)
        cumuLabel.grid(row=0, column=1, padx=HORIZONTAL_PADDING)

        instLabel = Label(outerFrame, text="Institutional", bg="gray80", font=LABEL_FONT)
        instLabel.grid(row=0, column=2, padx=HORIZONTAL_PADDING)

        semLabel = Label(outerFrame, text="Semester", bg="gray80", font=LABEL_FONT)
        semLabel.grid(row=0, column=3, padx=HORIZONTAL_PADDING)

        global CUMULATIVE_GPA
        global INSTITUTIONAL_GPA
        global CUMULATIVE_HOURS
        global INSTITUTIONAL_HOURS

        self.cumuGPAText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.cumuGPAText.insert(END, CUMULATIVE_GPA)
        self.cumuGPAText.grid(row=1, column=1)

        self.cumuHoursText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.cumuHoursText.insert(END, CUMULATIVE_HOURS)
        self.cumuHoursText.grid(row=2, column=1)

        self.instGPAText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.instGPAText.insert(END, INSTITUTIONAL_GPA)
        self.instGPAText.grid(row=1, column=2)

        self.instHoursText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.instHoursText.insert(END, INSTITUTIONAL_HOURS)
        self.instHoursText.grid(row=2, column=2, pady=4)

        self.semGPAText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.semGPAText.grid(row=1, column=3)

        self.semHoursText = Entry(outerFrame, width=4, font=ENTRY_FONT)
        self.semHoursText.grid(row=2, column=3)

        calculate = Button(outerFrame, text="Calculate", command=self.calc_gpa, font=("Arial", 20))
        calculate.grid(columnspan=3, row=8, column=1, pady=10)



    def calc_gpa(self):

        try:
            cumuGPA = float(self.cumuGPAText.get())
            cumuHours = float(self.cumuHoursText.get())
            instGPA = float(self.instGPAText.get())
            instHours = float(self.instHoursText.get())
            semGPA = float(self.semGPAText.get())
            semHours = float(self.semHoursText.get())

            cumuPoints = cumuGPA*cumuHours
            instPoints = instGPA*instHours
            semPoints = semGPA*semHours

            cumuGPA = round((cumuPoints+semPoints)/(cumuHours+semHours), 2)
            instGPA = round((instPoints+semPoints)/(instHours+semHours), 2)
            cumuHours = int(cumuHours + semHours)
            instHours = int(instHours + semHours)

            self.cumuGPAText.delete(0, END)
            self.cumuHoursText.delete(0, END)

            self.instHoursText.delete(0, END)
            self.instGPAText.delete(0, END)

            self.cumuGPAText.insert(END, cumuGPA)
            self.cumuHoursText.insert(END, cumuHours)

            self.instGPAText.insert(END, instGPA)
            self.instHoursText.insert(END, instHours)

            self.semGPAText.delete(0, END)
            self.semHoursText.delete(0, END)
        except ValueError:
            t = Tk()
            t.after(2500, lambda: t.destroy())
            t.wm_title("Error")

            outerFrame = Frame(t, bg="red", width=300, height=60)
            outerFrame.pack()

            errorLabel = Label(outerFrame, text="INPUT ALL DATA", bg="red", font=("Arial", 24))
            errorLabel.pack()



    def calcClick(self):
        try:
            calcIncome = float(self.income.get())
            calcRent = float(self.rent.get())
            calcCone = float(self.coText.get())
            calcChase = float(self.cText.get())
            calcPhone = float(self.pText.get())

            self.remainderText.delete(0, END)
            self.remainderText.insert(END, "$" + str(round(calcIncome - (calcRent+calcCone+calcChase+calcPhone), 2)))

        except ValueError:
            t = Tk()
            t.after(2500, lambda: t.destroy())
            t.wm_title("Error")

            outerFrame = Frame(t, bg="red", width=300, height=60)
            outerFrame.pack()

            errorLabel = Label(outerFrame, text="INPUT ALL DATA", bg="red", font=("Arial", 24))
            errorLabel.pack()


    def openClick(self):

        if self.month.get() != "":
            self.month.delete(0, END)

        if self.rent.get():
            self.rent.delete(0, END)

        if self.income.get():
            self.income.delete(0, END)

        if self.remainderText.get():
            self.remainderText.delete(0, END)

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

            fileMonth = str(self.month.get())


            m = "C:\\Users\\brian\\Budgets\\" + fileMonth + "_Budget.txt"
            f = open(m, "w+")

            fileMonth += "\n"
    
            fileRent = "Rent:\t\t\t$" + str(float(self.rent.get())) + "\n"
            fileIncome = "Income:\t\t\t$" + str(float(self.income.get())) + "\n"
            fileRemainder = "Remainder:\t\t" + str(self.remainderText.get()) + "\n"
            file_cOne = "Capital One Payment:\t$" + str(float(self.coText.get())) + "\n"
            fileChase = "Chase Payment:\t\t$" + str(float(self.cText.get())) + "\n"
            filePhone = "Phone Payment:\t\t$" + str(float(self.pText.get())) + "\n"
            separator = "---------------------------------\n"

            saved = fileMonth + separator + fileIncome + separator + fileRent + file_cOne + fileChase + filePhone + separator + fileRemainder

            f.write(saved)

    def saveasClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            my_filetypes = [('Text File (.txt)', '.txt')]
            saveas = filedialog.asksaveasfile(mode="w", defaultextension=".txt", title="Save Budget", filetypes=my_filetypes)

            fileMonth = str(self.month.get()) + "\n"
            fileRent = "Rent:\t\t\t$" + str(float(self.rent.get())) + "\n"
            fileIncome = "Income:\t\t\t$" + str(float(self.income.get())) + "\n"
            fileRemainder = "Remainder:\t\t" + str(self.remainderText.get()) + "\n"
            file_cOne = "Capital One Payment:\t$" + str(float(self.coText.get())) + "\n"
            fileChase = "Chase Payment:\t\t$" + str(float(self.cText.get())) + "\n"
            filePhone = "Phone Payment:\t\t$" + str(float(self.pText.get())) + "\n"
            separator = "---------------------------------\n"

            saved = fileMonth + separator + fileIncome + separator + fileRent + file_cOne + fileChase + filePhone + separator + fileRemainder

            saveas.write(saved)
            saveas.close()


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()





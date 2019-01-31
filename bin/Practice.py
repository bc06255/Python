from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk

root = Tk()
root.wm_title("Budget Calculator")

BACKGROUND_COLOR = "gray50"
FONT_COLOR = "BLACK"

CUMULATIVE_GPA = 2.26
INSTITUTIONAL_GPA = 2.92

CUMULATIVE_HOURS = 154
INSTITUTIONAL_HOURS = 63

turn = "red"

LABEL_FONT = "'Arial 20 bold"
GPA_ENTRY_FONT= "'Arial', 30"
BUDGET_ENTRY_FONT = "Arial 16"

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

        self.coText = Entry(monthFrame, font=BUDGET_ENTRY_FONT, width=8)
        self.coText.grid(row=3, column=3, sticky=W + E, padx=(0, 10))

        cDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        cDollar.grid(row=4, column=2, sticky=E)

        self.cText = Entry(monthFrame, font=BUDGET_ENTRY_FONT, width=8)
        self.cText.grid(row=4, column=3, sticky=W + E, padx=(0, 10))

        pDollar = Label(monthFrame, text="$", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        pDollar.grid(row=5, column=2, sticky=E)

        self.pText = Entry(monthFrame, font=BUDGET_ENTRY_FONT, width=8)
        self.pText.grid(row=5, column=3, sticky=W + E, padx=(0, 10))

        self.month = ttk.Combobox(monthFrame,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                  font=BUDGET_ENTRY_FONT, width=12, justify=RIGHT)
        self.month.grid(row=0, column=2, columnspan=2, padx=(0,10), pady=(8, 4))

        self.rent = Entry(monthFrame, font=BUDGET_ENTRY_FONT, width=8)
        self.rent.grid(row=1, column=3, sticky=W + E, padx=(0,10))

        self.income = Entry(monthFrame, font=BUDGET_ENTRY_FONT, width=8)
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
        windowmenu.add_command(label="Checkers", command=self.create_checkers)
        menubar.add_cascade(label="Window", menu=windowmenu)


        root.config(menu=menubar)

    def create_gpa(self):

        t = Toplevel(self)
        t.wm_title("GPA Calculator")

        outerFrame = Frame(t, bg=BACKGROUND_COLOR)
        outerFrame.grid(row=0,column=0)

        gpaLabel = Label(outerFrame, text="GPA", bg=BACKGROUND_COLOR, font=LABEL_FONT)
        gpaLabel.grid(row=1, column=0, padx=HORIZONTAL_PADDING)

        hoursLabel = Label(outerFrame, text="Hours", bg=BACKGROUND_COLOR, font=LABEL_FONT)
        hoursLabel.grid(row=2, column=0,  padx=HORIZONTAL_PADDING)

        cumuLabel = Label(outerFrame, text="Cumulative", bg=BACKGROUND_COLOR, font=LABEL_FONT)
        cumuLabel.grid(row=0, column=1, padx=HORIZONTAL_PADDING)

        instLabel = Label(outerFrame, text="Institutional", bg=BACKGROUND_COLOR, font=LABEL_FONT)
        instLabel.grid(row=0, column=2, padx=HORIZONTAL_PADDING)

        semLabel = Label(outerFrame, text="Semester", bg=BACKGROUND_COLOR, font=LABEL_FONT)
        semLabel.grid(row=0, column=3, padx=HORIZONTAL_PADDING)

        global CUMULATIVE_GPA
        global INSTITUTIONAL_GPA
        global CUMULATIVE_HOURS
        global INSTITUTIONAL_HOURS

        self.cumuGPAText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
        self.cumuGPAText.insert(END, CUMULATIVE_GPA)
        self.cumuGPAText.grid(row=1, column=1)

        self.cumuHoursText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
        self.cumuHoursText.insert(END, CUMULATIVE_HOURS)
        self.cumuHoursText.grid(row=2, column=1)

        self.instGPAText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
        self.instGPAText.insert(END, INSTITUTIONAL_GPA)
        self.instGPAText.grid(row=1, column=2)

        self.instHoursText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
        self.instHoursText.insert(END, INSTITUTIONAL_HOURS)
        self.instHoursText.grid(row=2, column=2, pady=4)

        self.semGPAText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
        self.semGPAText.grid(row=1, column=3)

        self.semHoursText = Entry(outerFrame, width=4, font=GPA_ENTRY_FONT)
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

    def create_checkers(self):
        self.t = Toplevel()
        self.t.wm_title("Checkers")


        self.blackPiecePath = "C:\\Users\\Brian\\PycharmProjects\\Python\\bin\\blackCheckers.png"
        self.blackCheckersImage = Image.open(self.blackPiecePath)
        self.blackCheckersImage = self.blackCheckersImage.resize((60, 60))

        self.blackCheckersPiece = ImageTk.PhotoImage(self.blackCheckersImage)

        self.redPiecePath = "C:\\Users\\Brian\\PycharmProjects\\Python\\bin\\redCheckers.png"
        self.redCheckersImage = Image.open(self.redPiecePath)
        self.redCheckersImage = self.redCheckersImage.resize((60, 60))

        self.redCheckersPiece = ImageTk.PhotoImage(self.redCheckersImage)

        self.checkerboardPath = "C:\\Users\\Brian\\PycharmProjects\\Python\\bin\\Checkerboard.png"
        self.checkerboardImage = Image.open(self.checkerboardPath)
        self.checkerboardImage = self.checkerboardImage.resize((600, 600))
        self.checkerboard = ImageTk.PhotoImage(self.checkerboardImage)

        Checkerboard = Label(self.t, width=595, height=595, image=self.checkerboard)
        Checkerboard.grid(row=0, column=0, rowspan=2)
        Checkerboard.bind("<Button-1>", self.addPiece)

        redTurn = Button(self.t, text="Red\nTurn", bg="red", fg="white", font="Arial 20 bold", command=self.red_turn)
        redTurn.grid(row=0, column=2, sticky=N+S+E+W)

        blackTurn = Button(self.t, text="Black\nTurn", bg="black", fg="white", font="Arial 20 bold",  command=self.black_turn)
        blackTurn.grid(row=1, column=2, sticky=N+S)

        w = self.checkerboard.width() + 100
        h = self.checkerboard.height()


        self.redLabel = [None] * 32
        self.blackLabel = [None] * 32

        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        for i in range(32):
            self.redLabel[i] = Label(self.t, width=55, height=55, image=self.redCheckersPiece, bg="black")
            self.blackLabel[i] = Label(self.t, width=55, height=55, image=self.blackCheckersPiece, bg="black")
            self.redLabel[i].bind('<Button-1>', self.onCanvasClick)
            self.blackLabel[i].bind('<Button-1>', self.onCanvasClick)

            if i < 4:
                self.redLabel[i].place(x=i * 150, y=0, width=70, height=70)

            if i > 3 & i < 8:
                self.redLabel[i].place(x=(j * 150) + 75, y=75, width=70, height=70)
                j += 1
            if (i > 7) & (i < 12):
                self.redLabel[i].place(x=k * 150, y=150, width=70, height=70)
                k += 1

            if 19 < i < 24:
                self.blackLabel[i].place(x=(l * 150) + 75, y=375, width=70, height=70)
                l += 1
            if 23 < i < 28:
                self.blackLabel[i].place(x=(m * 150), y=450, width=70, height=70)
                m += 1
            if 27 < i < 32:
                self.blackLabel[i].place(x=(n * 150) + 75, y=525, width=70, height=70)
                n += 1

        self.t.geometry('%dx%d+0+0' % (w,h))



    def onCanvasClick(self, event):
        event.widget.place_forget()


    def addPiece(self, event):
        global turn
        print(event.x, event.y)
        if turn is "red":
            if (0 < event.x < 75) & (0 < event.y < 75):
                self.redLabel[0].place(x=0, y=0, width=70, height=70)
            if (150 < event.x < 225) & (0 < event.y < 75):
                self.redLabel[1].place(x=150, y=0, width=70, height=70)
            if (300 < event.x < 375) & (0 < event.y < 75):
                self.redLabel[2].place(x=300, y=0, width=70, height=70)
            if (450 < event.x < 525) & (0 < event.y < 75):
                self.redLabel[3].place(x=450, y=0, width=70, height=70)

            if (75 < event.x < 150) & (75 < event.y < 150):
                self.redLabel[4].place(x=75, y=75, width=70, height=70)
            if (225 < event.x < 300) & (75 < event.y < 150):
                self.redLabel[5].place(x=225, y=75, width=70, height=70)
            if (375 < event.x < 450) & (75 < event.y < 150):
                self.redLabel[6].place(x=375, y=75, width=70, height=70)
            if (525 < event.x < 600) & (75 < event.y < 150):
                self.redLabel[7].place(x=525, y=75, width=70, height=70)

            if (0 < event.x < 75) & (150 < event.y < 225):
                self.redLabel[8].place(x=0, y=150, width=70, height=70)
            if (150 < event.x < 225) & (150 < event.y < 225):
                self.redLabel[9].place(x=150, y=150, width=70, height=70)
            if (300 < event.x < 375) & (150 < event.y < 225):
                self.redLabel[10].place(x=300, y=150, width=70, height=70)
            if (450 < event.x < 525) & (150 < event.y < 225):
                self.redLabel[11].place(x=450, y=150, width=70, height=70)

            if (75 < event.x < 150) & (225 < event.y < 300):
                self.redLabel[12].place(x=75, y=225, width=70, height=70)
            if (225 < event.x < 300) & (225 < event.y < 300):
                self.redLabel[13].place(x=225, y=225, width=70, height=70)
            if (375 < event.x < 450) & (225 < event.y < 300):
                self.redLabel[14].place(x=375, y=225, width=70, height=70)
            if (525 < event.x < 600) & (225 < event.y < 300):
                self.redLabel[15].place(x=525, y=225, width=70, height=70)

            if (0 < event.x < 75) & (300 < event.y < 375):
                self.redLabel[16].place(x=0, y=300, width=70, height=70)
            if (150 < event.x < 225) & (300 < event.y < 375):
                self.redLabel[17].place(x=150, y=300, width=70, height=70)
            if (300 < event.x < 375) & (300 < event.y < 375):
                self.redLabel[18].place(x=300, y=300, width=70, height=70)
            if (450 < event.x < 525) & (300 < event.y < 375):
                self.redLabel[19].place(x=450, y=300, width=70, height=70)

            if (75 < event.x < 150) & (375 < event.y < 450):
                self.redLabel[20].place(x=75, y=375, width=70, height=70)
            if (225 < event.x < 300) & (375 < event.y < 450):
                self.redLabel[21].place(x=225, y=375, width=70, height=70)
            if (375 < event.x < 450) & (375 < event.y < 450):
                self.redLabel[22].place(x=375, y=375, width=70, height=70)
            if (525 < event.x < 600) & (375 < event.y < 450):
                self.redLabel[23].place(x=525, y=375, width=70, height=70)


        if turn is "black":
            if (0 < event.x < 75) & (0 < event.y < 75):
                self.blackLabel[0].place(x=0, y=0, width=70, height=70)
            if (150 < event.x < 225) & (0 < event.y < 75):
                self.blackLabel[1].place(x=150, y=0, width=70, height=70)
            if (300 < event.x < 375) & (0 < event.y < 75):
                self.blackLabel[2].place(x=300, y=0, width=70, height=70)
            if (450 < event.x < 525) & (0 < event.y < 75):
                self.blackLabel[3].place(x=450, y=0, width=70, height=70)

            if (75 < event.x < 150) & (75 < event.y < 150):
                self.blackLabel[4].place(x=75, y=75, width=70, height=70)
            if (225 < event.x < 300) & (75 < event.y < 150):
                self.blackLabel[5].place(x=225, y=75, width=70, height=70)
            if (375 < event.x < 450) & (75 < event.y < 150):
                self.blackLabel[6].place(x=375, y=75, width=70, height=70)
            if (525 < event.x < 600) & (75 < event.y < 150):
                self.blackLabel[7].place(x=525, y=75, width=70, height=70)

            if (0 < event.x < 75) & (150 < event.y < 225):
                self.blackLabel[8].place(x=0, y=150, width=70, height=70)
            if (150 < event.x < 225) & (150 < event.y < 225):
                self.blackLabel[9].place(x=150, y=150, width=70, height=70)
            if (300 < event.x < 375) & (150 < event.y < 225):
                self.blackLabel[10].place(x=300, y=150, width=70, height=70)
            if (450 < event.x < 525) & (150 < event.y < 225):
                self.blackLabel[11].place(x=450, y=150, width=70, height=70)

    def red_turn(self):
        global turn
        turn = "red"
        print(turn)

    def black_turn(self):
        global turn
        turn = "black"
        print(turn)







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

        if self.income.get():
            self.income.delete(0, END)

        if self.rent.get():
            self.rent.delete(0, END)

        if self.coText.get():
            self.coText.delete(0, END)

        if self.cText.get():
            self.cText.delete(0, END)

        if self.pText.get():
            self.pText.delete(0, END)

        if self.remainderText.get():
            self.remainderText.delete(0, END)

        openFile = filedialog.askopenfile()

        lines = openFile.readlines()
        lines.append("")
        lines.append("")
        lines.append("")
        lines.append("")
        lines.append("")
        lines.append("")
        lines.append("")


        oMonth = lines[0]
        oIncome = lines[2].replace("Income:\t\t\t$", "")
        oRent = lines[4].replace("Rent:\t\t\t$", "")
        oC_One = lines[5].replace("Capital One Payment:\t$", "")
        oChase = lines[6].replace("Chase Payment:\t\t$", "")
        oPhone = lines[7].replace("Phone Payment:\t\t$", "")
        oRemainder = lines[9].replace("Remainder:\t\t", "")

        self.month.insert(END, oMonth)
        self.rent.insert(END, oRent)
        self.income.insert(END, oIncome)
        self.coText.insert(END, oC_One)
        self.cText.insert(END, oChase)
        self.pText.insert(END,oPhone)
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

            whitespace = "\n\n\n\n\n\n\n"

            f.write(saved)
            f.write(whitespace)

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





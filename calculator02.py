from math import exp
from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        expression = add_missing_mult(expression)
        expression = expression.replace("x","*")
        expression = expression.replace("%","/100")
        expression = expression.replace("mode","%")
        total = str(eval(expression.replace("^","**")))
        if ".999999" in total :
            spliter = total.split(".")
            total = int(spliter[0])+1
        equation2.set(total)
    except:
        equation2.set("error")

def clear():
    global expression
    expression = ""
    equation.set("")
    equation2.set("")

def crt():
    global expression
    print(expression)
    expression = expression[0:len(expression)-1]  
    equation.set(expression)

def sqrt():
    global expression
    expression = str(expression**0.5)
    equation.set(expression)

def percentage(percent):
    global expression
    expression = str((percent*expression)/100)
    equation.set(expression)

def add_missing_mult(s):
    splitted = s.split('(')
    for i, sub in enumerate(splitted[:-1]):
        if sub[-1].isdigit() or sub[-1] == '.':
            splitted[i] += "x"
    s = '('.join(splitted)
    
    try: 
        splitted = s.split(')')
        for i, sub in enumerate(splitted[1:]):
            if sub[0].isdigit():
                splitted[i+1] = "x" + splitted[i+1]
        s = ')'.join(splitted)
    except:
        pass
    return (s)



if __name__ == "__main__":
    gui = Tk()
    gui.iconbitmap("calculator_icon-icons.com_72046.ico")
    gui.configure(background="black")
    gui.title("Simple Calculator")
    gui.geometry("235x325")
    equation = StringVar()
    equation2 = StringVar()

    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=20, ipadx=55)

    equation.set("Enter")

    expression_field2 = Entry(gui, textvariable=equation2)
    expression_field2.grid(row=2, columnspan=20, ipadx=55)

    button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                    command=lambda: press(1), height=2, width=7)
    button1.grid(row=6, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='black',
                    command=lambda: press(2), height=2, width=7)
    button2.grid(row=6, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                    command=lambda: press(3), height=2, width=7)
    button3.grid(row=6, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='black',
                    command=lambda: press(4), height=2, width=7)
    button4.grid(row=5, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                    command=lambda: press(5), height=2, width=7)
    button5.grid(row=5, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='black',
                    command=lambda: press(6), height=2, width=7)
    button6.grid(row=5, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='black',
                    command=lambda: press(7), height=2, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='black',
                    command=lambda: press(8), height=2, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                    command=lambda: press(9), height=2, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='black',
                    command=lambda: press(0), height=2, width=7)
    button0.grid(row=7, column=1)

    button00 = Button(gui, text=' 00 ', fg='white', bg='black',
                    command=lambda: press("00"), height=2, width=7)
    button00.grid(row=7, column=0)


    plus = Button(gui, text=' + ', fg='green', bg='black',
                    command=lambda: press("+"), height=2, width=7)
    plus.grid(row=7, column=3)

    minus = Button(gui, text=' - ', fg='green', bg='black',
                    command=lambda: press("-"), height=2, width=7)
    minus.grid(row=6, column=3)

    multiply = Button(gui, text=' x ', fg='green', bg='black',
                    command=lambda: press("x"), height=2, width=7)
    multiply.grid(row=5, column=3)

    divide = Button(gui, text=' / ', fg='green', bg='black',
                    command=lambda: press("/"), height=2, width=7)
    divide.grid(row=4, column=3)

    equal = Button(gui, text=' = ', fg='green', bg='black',
                    command=lambda : equalpress(), height=2, width=7)
    equal.grid(row=9, column=3)

    clear1 = Button(gui, text=' Clear ', fg='green', bg='black',
                    command=clear, height=2, width=7)
    clear1.grid(row=3, column=0)

    percent = Button(gui, text=' % ', fg='green', bg='black',
                    command=lambda:press("%"), height=2, width=7)
    percent.grid(row=8, column=0)

    Decimal = Button(gui, text=' . ', fg='white', bg='black',
                    command=lambda: press("."), height=2, width=7)
    Decimal.grid(row=7, column=2)

    power = Button(gui, text=' ^n ', fg='green', bg='black',
                    command=lambda: press("^"), height=2, width=7)
    power.grid(row=9, column=0)

    correct = Button(gui, text=' del ', fg='green', bg='black',
                    command=lambda: crt(), height=2, width=7)
    correct.grid(row=3, column=3)

    square_root = Button(gui, text=' sqrt ', fg='green', bg='black',
                    command=lambda: press("^(1/2)"), height=2, width=7)
    square_root.grid(row=8, column=2)

    cube_root = Button(gui, text=' cbrt ', fg='green', bg='black',
                    command=lambda: press("^(1/3)"), height=2, width=7)
    cube_root.grid(row=8, column=3)

    bracket1 = Button(gui, text=' ( ', fg='green', bg='black',
                    command=lambda: press("("), height=2, width=7)
    bracket1.grid(row=3, column=1)

    bracket2 = Button(gui, text=' ) ', fg='green', bg='black',
                    command=lambda: press(")"), height=2, width=7)
    bracket2.grid(row=3, column=2)

    square = Button(gui, text=' ^2 ', fg='green', bg='black',
                    command=lambda: press("^2"), height=2, width=7)
    square.grid(row=9, column=1)

    cube = Button(gui, text=' ^3 ', fg='green', bg='black',
                    command=lambda: press("^3"), height=2, width=7)
    cube.grid(row=9, column=2)

    remainder = Button(gui, text=' mode ', fg='green', bg='black',
                    command=lambda: press("mode"), height=2, width=7)
    remainder.grid(row=8, column=1)

    gui.mainloop()

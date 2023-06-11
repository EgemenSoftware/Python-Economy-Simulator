import tkinter as tk
form=tk.Tk()
form.title("Economy Simulator")
etiket=tk.Label(text="Economy",fg="black")
etiket.pack()
etiket2=tk.Label(form,text="Simulator",fg="black")
etiket2.pack()
print("Welcome to Economy Simulator")
print("If Debt Level 300, Inflation 250, Dollar (Pound-Dollar) 50, Unemployment finds 100 game will be over")
interest=8
dollar=23
inflation=175
debt=200
unemployment=40
def increase():
    global interest
    interest=interest+1
    print("Interest Rate Increase")
    print(interest)
    global dollar
    dollar=dollar-2
    print("Dolar Decrease")
    print(dollar)
    global inflation
    inflation=inflation-10
    print("Inflation Decrease")
    print(inflation)
    global unemployment
    unemployment=unemployment+10
    print("Unemployment Increase")
    print(unemployment)
    global debt
    debt=debt+10
    print("Debt Increase")
    print(debt)


form.state("normal")

def decrease():
    global interest
    interest=interest-1
    print("Interest Rate Decrease")
    print(interest)
    global dollar
    dollar=dollar+2
    print("Dollar Increase")
    print(dollar)
    global inflation
    inflation=inflation+10
    print("Inflation Increase")
    print(inflation)
    global unemployment
    unemployment=unemployment-10
    print("Unemployment Decrease")
    print(unemployment)
    global debt
    debt=debt-10
    print("Debt Decrease")
    print(debt)


buton=tk.Button(form,text="Increase Interest Rate",fg="black",bg="green",command=increase)
buton.pack()
buton2=tk.Button(form,text="Decrease Interest Rate",fg="black",bg="green",command=decrease)
buton2.pack()

form.mainloop()


import tkinter as tk
from tkinter import messagebox as mb
import os
import math

# function to close program
def do_close():
    root.destroy()
    
# percent format
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'

def do_processing():
    #read values from entries
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())
    
    #check values
    if n1 <= 0 or n2 <= 0:
        mb.showerror(title='Error', message='Incorrect number of visitors')
        return
    
    popup_window(n1, c1, n2, c2)
    
    
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B result")
    
    # output text window
    txtOutput = tk.Text(window, font=('Courier new', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    # header
    txtOutput.insert(tk.END, '                          Control           Test' + os.linesep)
    txtOutput.insert(tk.END, '                          group             group' + os.linesep)
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)
    
    # output conversion and standard deviation
    p1 = c1 / n1
    p2 = c2 / n2
    txtOutput.insert(tk.END, 'Conversion           ' + num_percent(p1) + '      ' + num_percent(p2)  + os.linesep)
    
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Standard deviation   ' + num_percent(sigma1) + '      ' + num_percent(sigma2)  + os.linesep)
    
    txtOutput.insert(tk.END, '---------------------------------------------------------' + os.linesep)
    
    
    btnClosePopup = tk.Button(window, text="Close", font=('Helvetica', 10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    # focus on a popup window
    window.focus_force()


# main window
root = tk.Tk()
root.geometry("280x300")
root.title("A/B Calculator")

# header
lblTitle = tk.Label(text="A/B Calculator", font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=20)

# header for control group
lblTitle1 = tk.Label(text="Control group", font=('Helvetica', 12, 'bold'), fg='#0066ff')
lblTitle1.place(x=25, y=55)

# fields for entry for control group
lblVisitors1 = tk.Label(text="Visitors", font=('Helvetica', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center')
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '255')

lblConversions1 = tk.Label(text="Conversions", font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center')
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '26')


# header for test group
lblTitle1 = tk.Label(text="Test group", font=('Helvetica', 12, 'bold'), fg='#008800')
lblTitle1.place(x=25, y=145)

# fields for entry for test group
lblVisitors2 = tk.Label(text="Visitors", font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '235')

lblConversions2 = tk.Label(text="Conversions", font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font=('Helvetica', 10, 'bold'), justify='center')
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '18')


# close button
btnProcess = tk.Button(root, text="Calculate", font=('Helvetica', 10, 'bold'), command=do_processing)
btnProcess.place(x=25, y=250, width=90, height=30)

# close button
btnClose = tk.Button(root, text="Close", font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)


root.mainloop()

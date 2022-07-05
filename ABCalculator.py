
import tkinter as tk

# function to close program
def do_close():
    root.destroy()

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

entVisitors1 = tk.Entry(font=('Helvetica', 10, 'bold'))
entVisitors1.place(x=115, y=85, width=90, height=20)

lblConversions1 = tk.Label(text="Conversions", font=('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font=('Helvetica', 10, 'bold'))
entConversions1.place(x=115, y=115, width=90, height=20)


# header for test group
lblTitle1 = tk.Label(text="Test group", font=('Helvetica', 12, 'bold'), fg='#008800')
lblTitle1.place(x=25, y=145)

# fields for entry for test group
lblVisitors2 = tk.Label(text="Visitors", font=('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font=('Helvetica', 10, 'bold'))
entVisitors2.place(x=115, y=175, width=90, height=20)

lblConversions2 = tk.Label(text="Conversions", font=('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font=('Helvetica', 10, 'bold'))
entConversions2.place(x=115, y=205, width=90, height=20)


# close button
btnProcess = tk.Button(root, text="Calculate", font=('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)

# close button
btnClose = tk.Button(root, text="Close", font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)


root.mainloop()

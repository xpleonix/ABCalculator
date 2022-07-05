
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

# close button
btnProcess = tk.Button(root, text="Calculate", font=('Helvetica', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)

# close button
btnClose = tk.Button(root, text="Close", font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)


root.mainloop()

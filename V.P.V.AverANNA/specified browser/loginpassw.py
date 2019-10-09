from tkinter import *
from passwchecker import mainScript as mnSc
disp = Tk()
def command():
	global e1, e2, usr, passw
	usr, passw = e1.get(),e2.get()
	disp.quit()
Label(disp, text="user name", font="Leelawadee 10").grid(row=0, column=0)
Label(disp, text="password", font="Leelawadee 10").grid(row=1, column=0)
usr, passw = "", ""
e1 = Entry(disp)
e2 = Entry(disp, show="*")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
while True:
	Button(disp, text="submit", command=command).grid(row=2, column=0)
	disp.mainloop()
	if mnSc("passw", usr, passw):
		import script
	else:
		disp2 = Tk()
		Label(disp2, text="login failed . That is all we know :-(").grid(row=0, column=0)
		disp2.mainloop()
	
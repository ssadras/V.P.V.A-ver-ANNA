from tkinter import * 

choosing_disp = Tk()
Label(choosing_disp, text="Login With :", fg="black", bg="white", font="Leelawadee 16 bold").grid(row=1, column=0)
var = IntVar()
nvar = 0
def sel ():
	global nvar
	nvar = int(var.get())

def quit():
	global choosing_disp
	choosing_disp.quit()
radbutton1 = Radiobutton(choosing_disp, text="Face ID", variable=var, value=1, command=sel)
radbutton2 = Radiobutton(choosing_disp, text="password", variable=var, value=2, command=sel)

radbutton1.grid(row=2, column=0)
radbutton2.grid(row=3, column=0)
while True:
	try:
		Button(choosing_disp, text="submit", command=quit).grid(row=4, column=1)
	except:
		pass
	choosing_disp.mainloop()
	if nvar == 2:
		import loginpassw 

	if nvar == 1:
		pass #loading the face login menu

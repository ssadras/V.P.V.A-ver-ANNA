def mainScript (passwFile, inpUsr, inpPassw):
	with open(passwFile,"r") as file:
		lines = file.readlines()
		for line in range(len(lines)):
			if lines[line] == "usr\n":
				usr = lines[line+1][:-1]
			elif lines[line] == "passw\n":
				passw = lines[line+1][:-1]
		if inpUsr == usr and inpPassw == passw:
			return True
		else:
			return False
			
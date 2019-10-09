def findall (inp,target):#### target = open|go
	text = inp.split (" ")
	targets = target.split("|")

	for tar in range(len(targets)):
		targets[tar] = targets[tar].split("@")
		if "?" in target:
			for i in range(len(targets[tar])):
				if "?" in targets[tar][i]:
					a = targets[tar][i].split("?")
					targets[tar][i] = a[0]
					targets[tar].insert(i+1,"?")
		if "!" in target:
			for i in range(len(targets[tar])):
				if "!" in targets[tar][i]:
					a = targets[tar][i].split("!")
					targets[tar][i] = a[0]
					targets[tar].insert(i+1,"!")
					targets[tar].insert(i+2,a[1])
	for tar in range(len(targets)):
		if not isinstance(targets[tar],list):
			string = ""
			for i in targets[tar]:
				string += i
			targets[tar] = [string] 
			
	#spliting text into words
	output = []
	for word in range(len(text)):
		for i in range(len(targets)):
			if targets[i][0] == text[word]:
				if len(targets[i])>1:


					if targets[i][1] != "?":
						if targets[i][1] == "!":
							if targets[i][2] != text[word+1]:
								output.append((text[word],word))
								continue;	
						if text[word+1] == targets[i][1]:
							if "?" in targets[i]:
								if word+2<=len(text): 
									output.append((text[word],word))
							else:
								output.append((text[word],word))
				else:
					output.append((text[word],word))
	return output

def search (inp,text):
	return True if text in inp else False ;

class emotions (object):
	def __init__ (self, text):
		self.text = text
	@staticmethod
	def _freq_ (text):
		splited = text.split()
		for i in splited:
			if i in "!@#$%^&*()_+<>?":
				splited.remove(i)
		allwords = [(splited[word], splited.count(splited[word]), word) for word in range(len(splited))]
		
		return allwords
	def checkCore (self):
		allwords = _freq_(self.text)
		freqs = []
		for word, ferq, index in allwords:
			freqs.append([ferq,index])
		Max = [0, 0]
		for obj in freqs:
			if obj[0]>Max[0]:
				Max = obj[:]
		return Max
text = emotions ("hello world !")
array = text._freq_()
print(array)

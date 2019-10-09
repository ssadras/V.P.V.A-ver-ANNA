#https://translate.google.com/#view=home&op=translate&sl=fa&tl=en&text=
import requests as req 
import os

def getUrlHtml (url):
	source = req.get(url)
	return source.text

def loadPage (srcFile):
	os.startfile (srcFile)

def saveHtml (code, destFile):
	try:
		with open(destFile, "a") as src :
			src.write(code)
			src.close()
		return 1
	except:
		return 0
def writeIn (code, destFile):
	try:
		with open(destFile, "w") as src:
			src.write(code)
			src.close()
		return 1

	except:
		return 0

def main (srcLang, destLang, plainText):

	langs = {
	"french":"fr",
	"english":"en",
	"persian":"fa"
	}
	if srcLang not in langs:
		raise ValueError("Unsupported source language")
	if destLang not in langs:
		raise ValueError("Un supported source language")
	url = "https://translate.google.com/#view=home&op=translate&sl=%s&tl=%s&text=%s"%(langs[srcLang], langs[destLang], plainText)
	code = getUrlHtml(url)
	if os.path.exists("src.html"):
		write = lambda : writeIn(code, "src.html")
	else:
		saveHtml(code, "src.html")
	loadPage("src.html")

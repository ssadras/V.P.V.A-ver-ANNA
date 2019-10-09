import requests as req 
import os


class htmlDocument :
	def __init__(self):
		pass
	def get_html(self, url):
		source = req.get(url)
		return source.text	
	def load_page (self,name):
		os.startfile(name)

	def createHtmlDocument (self,source):
		mode = "w" if os.path.exists("src.html") else "a" 
		with open("src.html",mode) as src:
				src.write(source)
				src.close ()
obj = htmlDocument()
src = obj.get_html("http://google.com/search?q=mom")
doc = obj.createHtmlDocument(src)
obj.load_page("src.html")
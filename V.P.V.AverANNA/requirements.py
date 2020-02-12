import wikipedia as wiki 
import webbrowser as web
import wolframalpha as prc
import requests as req 
import smtplib
import ssl
import os 

def open_file (path):
	#### This function includes the openning files with their 
	#### own suffixs . 
	with open(path,"r") as file : ## reading file
		# attaching lines togather
		data = ''.join(file.readlines()[:-2])
		# returning the data
		return data;

def open_app (path):
	
	### THIS FUNCTION OPENS REQUIRED APPS IN
	### THEIR PARTICULAR PATH(S)
	try :
	###tring if the path exists and there were no
	###exception during operating the operation.
		os.startfile(path)
		### this line of code starts app in the spesified 
		### location.
		return True;
		### returns true if there were no exception.
	except Exception as e:
		### cheks if an exception occured during operating the operation.
		print(e)
		return False;
		### returns false if there were exceptions.

def search (text_input):
	### this function returns a summary from the wikpedia.
	return wiki.summary(text_input);

def send_email (recv,massage):
	port = 456
	smtp_server = "smtp..gmail.com"
	send = "ilia.var84@gmail.com"
	r = recv
	passw = "ame mohem tarin padide ye gharn hazer ast !"
	mass = massage
	context = ssl.creat_default_context()
	with smtplib.SMTP_SSL(smtp_server,port,context = context) as server:
		server.login(send,passw)
		server.sendmail(send,r,mass)
def commandline (prompt):
	os.popen(prompt)
def search_google (url):
	web.open(url)
import wikipedia as wiki 
import wolframalpha as prc 
import math

class client (object):
	def __init__ (self, appId):
		self.client = prc.Client(appId);

	def make_query(self, string):
		self.query = self.client.query(string);

	def result(self):
		# backup_query = None
		try:
			backup_query = self.query;
			exists = 1
		except :
			backup_query =None;
			exists = 0
		if not exists:
			return "Error : loading query failed."
		return next(self.query.results).text
def all_extensions(query_string):
	try:
		c = client("V5X78Y-Y2HJH5Y63E")
		c.make_query(query_string)
		return c.result()
	except:
		return "I'm not sure I'm understand";


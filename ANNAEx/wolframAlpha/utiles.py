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
c = client("V5X78Y-Y2HJH5Y63E")
c.make_query("Weather Tehran today?")
print(c.result())
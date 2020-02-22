import requests as rq
import xmltodict
import pprint
import json
import os

req = rq.get("https://api.exchangerate-api.com/v4/latest/USD");

file_readed = str(req.text)

parsed_file = None;


typeof = "xml" if file_readed[0] == "<" else "json"
#file_readed = f.read()
print(file_readed)

if typeof == "xml":
	if os.path.exists("./xml_data.xml"):
		with open("xml_data.xml", "w") as f:
			f.write(str(file_readed))
			f.close()
	else:
		with open("xml_data.xml", "a") as f:
			f.write(str(file_readed))
			f.close()
	parsed_file = xmltodict.parse(file_readed)
	print(parsed_file["main"])

else:
	if os.path.exists("./json_data.json"):
		with open("json_data.json", "w") as f:
			f.write(str(file_readed))
			f.close()
	else:
		with open("json_data.json", "a") as f:
			f.write(str(file_readed))
			f.close()
	parsed_file = json.loads(file_readed)


if os.path.exists("./dict.py"):
	with open("dict.py", "w") as f:
		f.write("dict = "+str(parsed_file))
		f.close()
else:
	with open("dict.py", "a") as f:
		f.write("dict = "+str(parsed_file))
		f.close()
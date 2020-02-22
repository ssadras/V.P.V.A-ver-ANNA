import xmltodict
import pprint
import json
import os

parsed_file = None;

with open("data.txt", "r") as f:
	typeof = "xml" if f.read()[0] == "<" else "json"
	file_readed = f.read()
	print(file_readed)

if typeof == "xml":
	if os.path.exists("./xml_data.xml"):
		with open("xml_data.xml", "w") as f:
			f.write(file_readed)
			f.close()
	else:
		with open("xml_data.xml", "a") as f:
			f.write(file_readed)
			f.close()
	parsed_file = xmltodict.parse(file_readed)

else:
	if os.path.exists("./json_data.json"):
		with open("json_data.json", "w") as f:
			f.write(file_readed)
			f.close()
	else:
		with open("json_data.json", "a") as f:
			f.write(file_readed)
			f.close()
	parsed_file = json.loads(file_readed)


if os.path.exists("./dict.py"):
	with open("dict.py", "w") as f:
		f.write(parsed_file)
		f.close()
else:
	with open("dict.py", "a") as f:
		f.write(parsed_file)
		f.close()
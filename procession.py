import speech_recognition as sr
import requirements as req
import wikipedia as wiki
import playsound as pl
import regex as re
import gtts
import cv2
import os



def _speak_(input):
    toSay = gtts.gTTS(text=input, lang="en-US", slow=False)
    toSay.save ("input-computer.mp3")
    pl.playsound ("input-computer.mp3")
    os.remove("input-computer.mp3")
def get_audio (limit):

    rObj = sr.Recognizer()

    with sr.Microphone() as src:

        '''
        listen and record the user s command
        '''
        audio = rObj.listen(src, phrase_time_limit = limit)

    try:
        final_text = rObj.recognize_google (audio, language = "en-US")
        print ("You said : %s"%(final_text))

        return final_text

    except Exception as exc :
        _speak_ ("i didn't get that, please repeat your command.")

        print(exc)

        return
def command_proccess(input_data):

	input_data = input_data.lower()

	opennings = re.findall (input_data.lower(),"open|go@to");print(opennings)
	searchs = re.findall(input_data.lower(),"search@about|search!about")
	whats = re.findall(input_data.lower(),"what@is|what's")
	sending = re.findall(input_data.lower(),"send@mail|mail?|send@email")
	command = input_data.split(" ")
	print(command)
	if len(opennings)!=0:
		for value,index in opennings:
			'''
			if command[index+1] == "chrome":
				req.open_app("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
			if command[index+1] == "mozilla" or command[index+1] == "firefox":
				req.open_app("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
			if command[index+1] == "word":
				req.open_app("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe")
			if command[index+1] == "powerpoint":
				req.open_app("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe")
			if command[index+1] == "excel":
				req.open_app("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe")
			if command[index+1] == "pycharm":
				req.open_app("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\JetBrains PyCharm 2019.1.1.exe")
			'''
			req.commandline("start %s"%command[index+1])
	if len(searchs) != 0:
		for value, index in searchs:
			_speak_("here's what I found on the web:")
			req.search_google("google.com/search?q=%s"%''.join(command[index+2:]))
		return
	if len(whats) != 0:
		for value, index in whats:
			try:
				#a = ''.join(command[index+2:]
				alist = ""

				for i in command[index+2:]:
					alist += "%s "%i
				al = alist.split(" ")
				url = "https://en.wikipedia.org//wiki//%s"%"_".join(al)#wiki.page(alist).url
				req.search_google(url)
				print(alist)
				print(command[index+2:])
				result = wiki.summary(alist).split(".")
				print(result)
				for i in range (len(result)):
					_speak_(result[i])
					_speak_("shall i continue ? ")
					res = get_audio(3)
					print(res)
					if res.lower() == "yes":
						continue
					elif res.lower() == "it's enough" or res.lower() == "no":
						_speak_("okay")
						return

			except Exception as exc:
				print(exc)
				#a = ''.join(command[index+2:]
				alist = ""
				for i in command[index+2:]:
					alist += "%s "%i
				print(alist)
				_speak_("here's what I found on the web:")
				req.search_google("www.google.com/search?q=%s"%alist)


		return
	if len(sending) != 0:
		_speak_("to who? you wanna talk? or... write?")
		opt = get_audio(3)
		if opt.lower() == "talk":
			_speak_("okay;i'm hearing")
			recv = get_audio(3)
			_speak_("okay ; read your mail...or you wanna write it?")
			if get_audio(3).lower() == "write":
				txt = input("Write it so : ")
			else:
				_speak_("okay;i'm hearing")
				txt = get_audio(5)
		elif opt.lower() == "write" or opt.lower() == "right":
			recv = input('Write it so : ')
			_speak_("okay ; read your mail...or you wanna write it?")
			x = get_audio(3).lower()
			if x == "write" or x == "right":
				txt = input("Write it so : ")
			else:
				_speak_("okay;i'm hearing")
				txt = get_audio(5)
		_speak_("sent")
		req.send_email(recv, txt)
	if input_data == "who are you":
		return "I am hana ;I am here to make your life way easier!"
	return

from time import sleep
import speech_recognition as sr
import face_recognition as fr
import procession  as pro
import face_recognition
import playsound as pl
import pygame as pg
import numpy as np
import threading
import gtts
import sys
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os #; print(len(os.listdir("\\V.P.V.A\\assets")))
# starting
pg.init()

class display (object) :
    def __init__(self, surface):
        self.surface = surface

    def load_image(self, pathname, pos, scale, surface):
        img = pg.image.load(pathname)
        img = pg.transform.scale(img, tuple(scale))

        surface.blit(img, tuple(pos))

    def write_text(self, pos, text, color, font_face, font_size, surface):
        txt = pg.font.SysFont(font_face, font_size)
        label = txt.render(text, True, tuple(color))
        surface.blit(label, tuple(pos))
def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "anonymous"

        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_names

def cFaceCapture ():
    video_capture = cv2.VideoCapture(0)
    cou = 1
    ret, frame = video_capture.read()
    cv2.imwrite("frames\\frame%d.jpg" % cou, frame)
    while len(classify_face("frames\\frame%d.jpg"%cou)) == 0:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        cou += 1
        cv2.imwrite("frames\\frame%d.jpg"%cou, frame)
    return classify_face("frames\\frame%d.jpg"%cou)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
def _speak_ (input):
    toSay = gtts.gTTS(text=input, lang="en-US", slow=False)
    toSay.save ("input-computer.mp3")
    pl.playsound ("input-computer.mp3")
    os.remove("input-computer.mp3")
def get_audio(limit, starter):

    rObj = sr.Recognizer()

    with sr.Microphone() as src:
        print("talk to me ...")
        #_speak_(starter)
        '''
        listen and record the user s command
        '''
        audio = rObj.listen(src)#, phrase_time_limit=limit
    #print("limit finished")
    while True:
        try:
            final_text = rObj.recognize_google (audio, language = "en-US")
            print ("You said : %s"%final_text)

            return final_text

        except Exception as exc :
            _speak_ ('''
            I'm sorry but an error occurred during processing your voice :
                please check conection and speak english. i will hear you.
                ''')
            rObj = sr.Recognizer()

            with sr.Microphone() as src:
                print("talk to me ...")
                _speak_(starter)
                '''
                listen and record the user s command
                '''
                audio = rObj.listen(src, phrase_time_limit=limit)
            print("limit finished")
            print(exc)
namevar=''
passvar=''
userpasscheck=''
loginpage=''
def checkuserpass ():
    global namevar,passvar,userpasscheck
    userpassfile=open('userpass.txt','r')
    userpasslist=userpassfile.readlines()
    count=0
    for userpass in userpasslist:
        userpassSplit=userpass.split(',')
        user=userpassSplit[0]
        password=userpassSplit[1][:-1]
        count+=1
        if user.lower()==namevar.get().lower() and password.lower()==passvar.get().lower():
            return user
    return 'nobody'
def loginbutton (event):
    global namevar,passvar,userpasscheck,loginpage
    user=checkuserpass()
    if user=='nobody':
        userpasscheck=''
        #namentry.delete(0,len(namevar))
        #passentry.delete(0,len(namevar))
    elif user!='':
        userpasscheck=user
        loginpage.destroy()
def loginpagetk ():
    global namevar,passvar,userpasscheck,loginpage
    loginpage=tk.Tk()
    loginpage.title('Anna - Login')
    loginpage.geometry('425x100+450+300')
    namevar=tk.StringVar()
    passvar=tk.StringVar()
    nametext=tk.Label(loginpage,text='Username ',font=('Arial',15))
    passtext=tk.Label(loginpage,text='Password ',font=('Arial',15))
    namentry=tk.Entry(loginpage,font=('Arial',15),textvariable=namevar)
    passentry=tk.Entry(loginpage,font=('Arial',15),textvariable=passvar,show="*")
    loginbut=tk.Button(loginpage,text='Login',font=('Arial',15))
    nametext.grid(column=2,row=2)
    namentry.grid(column=4,row=2)
    passtext.grid(column=2,row=4)
    passentry.grid(column=4,row=4)
    loginbut.grid(column=3,row=6)
    loginbut.bind('<Button-1>',loginbutton)
    loginpage.mainloop()
def loginway ():
    #loginpagetk()
    com="In which way you want to login, 1- with username and password, or 2- with face recognation?"
    _speak_(com)
    command = get_audio(7, com)
    if command.lower() == 'face recognation':
        try:
            rname = cFaceCapture()
            boolean = False
            cou = 0
            for i in rname :
                if i != "anonymous":
                    boolean = True
                    break;
                cou += 1
            if not boolean:
                _speak_("i don't know who you are,so login failed")
                sys.exit(0)
            _speak_("welcome %s %s"%(rname[cou].split(" ")[0], rname[cou].split(" ")[1]))
            name = rname[cou].split(" ")[0]
        except:
            _speak_("an error occurred during processing your face.All i could say is : login failed.")
            sys.exit(0)
        return (name)
    else:
        loginpagetk()
        name=userpasscheck
    return name
def gif ():
    pg.init()
    disp = pg.display.set_mode((300, 150))
    pg.display.set_caption("V.P.V.A ver ANA")
    color = [241, 241, 241]

    sur = display(disp)
    for i in range (225):
        disp.fill(tuple(color))
        sur.load_image("E:\\V.P.V.A\\assets\\%s"%os.listdir("\\V.P.V.A\\assets")[i], (50, 0), (200, 150),disp)
        pg.display.update()
        pg.time.Clock().tick(60)
    pg.quit()
def main (event):
    global name,output
    com = "%s How can i help you ?"%name
    _speak_(com)

    command = get_audio(7, com)
    if command.lower() == "nothing" or command.lower() == "no":
        output="okay %s, until next time i'll not bother you."%name
        _speak_(output)
        sys.exit(0)

    elif command.lower() == "bye" or command.lower() == "goodbye":
        output="okay %s, bye for now."%name
        _speak_(output)
        sys.exit(0)
    elif command.lower() == "what does Anna stands for" or command.lower() == "what does Ana stands for":
        output="%s,Anna stands on : artificial nural network assistant"%name
        _speak_(output)
    else:
        output=' '
    try:
        _speak_(pro.command_proccess(command))
    except :
        pass
tkpage=tk.Tk()
tkpage.title('Anna')
tkpage.geometry('300x200+1200+0')
annabox=tk.Label(tkpage,text='In which way you want to login,\n 1- with username and password \n or 2- with face recognation?',font=('Arial',10),fg='green')
annabox['bg']=annabox.master['bg']
annabox.grid(row=1,column=1)
name='sadra'
output=' '
custbox=tk.Label(tkpage,text=output)
custbox.grid(row=2,column=1)
iconim=Image.open('default.png')
iconim=ImageTk.PhotoImage(iconim)
speechbut=tk.Button(tkpage,image=iconim)
speechbut.grid(row=3,column=2)
speechbut.bind('<Button-1>',main)
tkpage.mainloop()

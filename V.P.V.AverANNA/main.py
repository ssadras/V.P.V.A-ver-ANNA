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

    return face_names[0]

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
        _speak_(starter)
        '''
        listen and record the user s command
        '''
        audio = rObj.listen(src, phrase_time_limit=limit)
    print("limit finished")

    try:
        final_text = rObj.recognize_google (audio, language = "en-US")
        print ("You said : %s"%final_text)

        return final_text

    except Exception as exc :
        _speak_ ('''
        I'm sorry but an error occurred during processing your voice :
            see if you are not connected to the internet ;
            if you were connected and there were not any problem with the connection ; please reduce noises around you;
            if neither problems above occurred,please speak english.
        however I will put the error below and if you know python language programming please help us to debug;
            ''')

        print(exc)

        return

def gif ():
    pg.init()
    disp = pg.display.set_mode((300, 150))
    pg.display.set_caption("V.P.V.A ver ANNA")
    color = [241, 241, 241]

    sur = display(disp)
    for i in range (225):
        disp.fill(tuple(color))
        sur.load_image("E:\\V.P.V.A\\assets\\%s"%os.listdir("\\V.P.V.A\\assets")[i], (50, 0), (200, 150),disp)
        pg.display.update()
        pg.time.Clock().tick(60)
    pg.quit()


def main ():



    '''
    disp.fill(tuple(color))
    sur.load_image("default.png", (50, 350), (200, 150), disp)
    pg.display.update()
    '''
    _speak_("running face recognition software...")
    name = cFaceCapture()
    if name == "anonymous":
        _speak_("i don't know who you are ; so login failed.")
        sys.exit(0)
    _speak_("welcome %s"%name)
    name = name.split(" ")[0]
    com = "%s, How can i help you ?"%name #if j else "hello; i am Ana; how can i help you ?"


    command = get_audio(7, com)
    if command.lower() == "nothing" or command.lower() == "no":
        _speak_("okay %s, until next time i'll not bother you."%name)
        sys.exit(0)

    if command.lower() == "bye" or command.lower() == "goodbye":
        _speak_("okay %s, bye for now."%name)
        sys.exit(0)
    try:
        _speak_(pro.command_proccess(command))
    except :
        pass

cou = 1
index = 0
while 1:
    '''
    x = threading.Thread(target=gif())
    x.start()
    y = threading.Thread(target=main())
    y.start()
    '''
    if cou == 1:
        _speak_("running face recognition software...")
        done=False
        while not done:
            try:
                rname = cFaceCapture()
                if rname == "anonymous":
                    _speak_("i don't know who you are,so login failed")
                    sys.exit(0)
                _speak_("welcome %s %s"%(rname.split(" ")[0], rname.split(" ")[1]))
                name = rname.split(" ")[0]
                notdone=True
            except:
                _speak_("an error occurred during processing your face.All i could say is : login failed and i want to check you again.")
                #sys.exit(0)
    if index:
        sleep(7)
    com = "%s How can i help you ?"%name
    _speak_(com)

    command = get_audio(7, com)
    if command.lower() == "nothing" or command.lower() == "no":
        _speak_("okay %s, until next time i'll not bother you."%name)
        sys.exit(0)

    if command.lower() == "bye" or command.lower() == "goodbye":
        _speak_("okay %s, bye for now."%name)
        sys.exit(0)
    if command.lower() == "what does Hana stands for" or command.lower() == "what does Anna stands for":
        _speak_("%s,hana stands on : Artificial Neural Network Assistant"%name)
    try:
        _speak_(pro.command_proccess(command))
    except :
        pass
    cou += 1
    index += 1

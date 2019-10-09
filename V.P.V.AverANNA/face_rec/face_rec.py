import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep


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
        name = "anonymuous"

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
print(cFaceCapture())

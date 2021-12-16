import cv2
import face_recognition as fr
from os import listdir


RECT_COLOR = (0, 255, 255) # Yellow color Note: BRG
MODEL = "hog" # hog/cnn (hog is for CPU)
TOLERANCE = 0.6
FRAME_THICKNESS = 1


def load_known_faces():
    # Get number of files (images) in "known" directory
    filenames = listdir(path)
    
    images = []
    face_locations = []
    images_encodings = []
    
    for i in filenames:
        img = fr.load_image_file(f"{path}/{i}")
        location = fr.face_locations(img, model=MODEL)
        encoding = fr.face_encodings(img, model=MODEL)[0]

        images.append(img)
        face_locations.append(location)
        images_encodings.append(encoding)
    # Get names of images
    face_filenames = []
    for i in filenames:
        i = i[:-4]
        face_filenames.append(i)
    return (images, face_locations, images_encodings, face_filenames)


cap = cv2.VideoCapture(0)

path = "known"
face_imgs, face_locats, face_encs, face_filenames = load_known_faces()

while True:
    _, img = cap.read()

    curr_location = fr.face_locations(img, model=MODEL)
    curr_encodings = fr.face_encodings(img, model=MODEL)
    
    for f_encoding, f_location in zip(curr_encodings, curr_location):
        match = fr.compare_faces(face_encs, f_encoding)
        
        #name = "Unknown Person"
        name = None

        if True in match:
            name = face_filenames[match.index(True)]

            top_left = (f_location[3], f_location[0])
            bottom_right = (f_location[1], f_location[2])

            cv2.rectangle(img, top_left, bottom_right, RECT_COLOR, FRAME_THICKNESS)

            top_left = (f_location[3], f_location[2])
            bottom_right = (f_location[1], f_location[2]+20)
            cv2.rectangle(img, top_left, bottom_right, RECT_COLOR, cv2.FILLED)
            cv2.putText(img, str(name), (f_location[3]+10, f_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (20, 20, 20))

    cv2.imshow("result", img)

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()

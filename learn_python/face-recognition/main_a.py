import face_recognition as fr
from os import listdir
from PIL import Image, ImageDraw, ImageFont

DRAW_RECT = (255, 255, 0) # Yellow color
MODEL = "hog" # hog/cnn (hog is for CPU)
TOLERANCE = 0.6

font = ImageFont.truetype("arial.ttf", 20)

def load_known_faces():
    path = "known"
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



def compare_images(known_img, known_loc, known_enc, known_face_img):
    # Load unknown faces from directory
    path = "unknown"
    unknown_images = listdir(path)

    for i in unknown_images:
        image = fr.load_image_file(f"{path}/{i}")
        face_location = fr.face_locations(image, model=MODEL)
        face_encodings = fr.face_encodings(image, model=MODEL)


        pill_image = Image.fromarray(image)
        pill_draw = ImageDraw.Draw(pill_image)

        # Start comparing unknown and known faces
        for (top, right, bottom, left), face_encoding in zip(face_location, face_encodings):
            face_matches = fr.compare_faces(known_enc, face_encoding, TOLERANCE)

            name = "Unknown Face"

            if True in face_matches:
                # If there is more known faces
                match_index = face_matches.index(True)
                name = known_face_img[match_index]

            pill_draw.rectangle(((left, top), (right, bottom)), outline=DRAW_RECT)

            text_width, text_height = pill_draw.textsize(name)
            pill_draw.rectangle(((left, bottom - text_height), (right, bottom+15)), fill=DRAW_RECT, outline=DRAW_RECT)
            pill_draw.text((left, bottom - text_height), name, font=font, fill=(0, 0, 0, 0))

        del pill_draw

        pill_image.show()
    

known_images, locations, encodings, face_filenames = load_known_faces()

compare_images(known_images, locations, encodings, face_filenames)
    

# face-recognition

MODULES:\
face_recognition, cv2, PIL\
(language: python)
\
**ABOUT IT**\
Repository has two scripts -> main_a and main_b

First I tried to learn the face_recognition module and started with main_a. It use two folders -> "known" and "unknown". Script than load images, use face_encoding on each image (you compare encoded two images to get True or False; which determine if there is match between those two), get position of face and get name of image. This goes for every image in "unknown", which are compared with every already encoded (and so on...) images and try to find match. If True, than draw rectangle on face position and put there coresponding name, else label it with "Unknown Face". You can add images as you want to "known" and "unknown" folders, but I encountered problem with more images of one persons labeled with diferrent names. Editing with images is done with PIL module.\
\
Second script (main_b) instead of images it use camera (open-cv module) (you can also use recorded video; you just insted of 0 in cap = VideoCapture(0) write path to the video; if you have mmore cames, you switch with different numbers). This script also don't use "unknown" folder.

**VIRTENV**\
As virtual environment I used Anaconda, but I encountered problems with installing face_recognition (dlibs errors) and I found out this procedure to be able to solve it:

Write in your terminal:
```
activate *your virtual environment*
conda config --add channels conda-forge
conda install numpy
conda install scipy
conda install dlib
pip install --no-dependencies face_recognition
```

**SCRIPTS**\
TOLERANCE is set to 0.6, which is default and considered to be best. Lower TOLLERANCE, fewer recognized images.\
MODEL is set to "hog", which is older model of neural network (use CPU); you can switch it to something else (for example "cnn", which is newer).\
COLOR is set to yellow (Be aware that cv2 use BGR instead of RGB).\
In script main_b you can switch camera or change it to some recorded video.


SCRIPT: **main_b**\
![camera_face_recognition_1](https://user-images.githubusercontent.com/57571014/83691460-7e6d9180-a5f2-11ea-9fd5-9fa3f4709928.gif)


_______


SCRIPT: **main_a**\
![image_face_recognition](https://user-images.githubusercontent.com/57571014/83691620-c987a480-a5f2-11ea-85ae-79123c313367.gif)

Overall: I am happy with result and I am planning to implement this system to somewhere (propably on drone or different robot).

#blackpanther
import cv2
import numpy
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Open Webcam
from PIL import Image
filename = 'blackpanther.png'
frontImage = Image.open(filename)
frontImage = frontImage.convert("RGBA")
cap = cv2.VideoCapture(0)
while True:
    ret,photo = cap.read()
    cv2.normalize(photo,photo, 10, 255, cv2.NORM_MINMAX)
    loc = face_model.detectMultiScale(photo)
#     photo1 = photo
    if len(loc) == 1:
        x1 =loc[0][0]-20
        y1 =loc[0][1]-60
        x2 =loc[0][2]+x1+30
        y2 =loc[0][3]+y1+85
        cphoto = photo[y1:y2, x1:x2]
        if cphoto.shape[1] >0 and cphoto.shape[0] > 0 :
            img = frontImage.resize((cphoto.shape[1],cphoto.shape[0]), Image.ANTIALIAS)
#             photo[y1:y2, x1/:x2]=img
            photo = Image.fromarray(photo)
            photo.paste(img, (x1,y1), img)
            photo = numpy.asarray(photo)
        cv2.normalize(photo,photo, 0, 255, cv2.NORM_MINMAX)
        cv2.imshow('hi',photo)

        if cv2.waitKey(10) == 13: #13 is the Enter Key
            break
        
cap.release()
cv2.destroyAllWindows()
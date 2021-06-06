import cv2
import mediapipe as mp
import tkinter
from pynput.mouse import Button ,Controller
mouse = Controller()
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand=mp_hands.Hands(max_num_hands=2,min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap=cv2.VideoCapture(0)
while True:
    ret,photo = cap.read()
    photo=cv2.resize(photo,(int(width/2),int(height/2)))
    results=hand.process(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))
    if results.multi_handedness:
#         print('Handedness:', results.multi_handedness)
#         print(results.multi_hand_landmarks
        for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(photo, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            h,w,c = photo.shape
            for ids , ss in enumerate(hand_landmarks.landmark):
                if ids == 4 :
#                     print("x : ",ss.x*w ,"\ny : ",ss.y*h )
#                     cv2.line(photo ,(0,0),(int(ss.x*w),int(ss.y*h)),(0,255,0), 2)
                    l4x = int(ss.x*w)
                    l4y = int(ss.y*h)
                    mouse.position = (int(ss.x*w)*2,int(ss.y*h)*2)
                if ids == 8:
                    l8x = int(ss.x*w)
                    l8y = int(ss.y*h)
            ly = l4y - l8y
            if ly < 20:
                mouse.press(Button.left)
#                 print("y :" ,l4y - l8y)
            elif ly > 40: 
                mouse.release(Button.left)
    cv2.imshow('hi',photo)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
cap.release()
cv2.destroyAllWindows()
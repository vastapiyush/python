import cv2 as cv
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, 500)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)

while True:
    _,screen = cam.read()
    screen = cv.flip(screen,1)
    frame_height,frame_width,_= screen.shape
    rgb = cv.cvtColor(screen,cv.COLOR_BGR2RGB)
    output = hand_detector.process(rgb)
    hands = output.multi_hand_landmarks
    if hands :
        for hand in hands:
            drawing.draw_landmarks(screen,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                # print(x,y)
                if id == 8:
                    # cv.circle(img=frame,center=(x,y),radius=20,color=(255,0,0))
                    pyautogui.moveTo(x*2,y*2)

    print(hands)
    cv.flip(screen,0)
    cv.imshow("camera",screen)
    cv.waitKey(1)


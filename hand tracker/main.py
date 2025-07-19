import cv2 as cv
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, 500)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)

while True:
    _,frame = cam.read()
    frame = cv.flip(frame,1)
    frame_height,frame_width,_= frame.shape
    rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output = hand_detector.process(rgb)
    hands = output.multi_hand_landmarks
    if hands :
        for hand in hands:
            drawing.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                # print(x,y)
                if id == 8:
                    # cv.circle(img=frame,center=(x,y),radius=20,color=(255,0,0))
                    pyautogui.moveTo(x*2,y*2)

    print(hands)
    cv.flip(frame,0)
    cv.imshow("camera",frame)
    cv.waitKey(1)


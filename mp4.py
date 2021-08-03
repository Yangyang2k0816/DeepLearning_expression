import cv2
cap = cv2.VideoCapture("./opencv.mov")
#frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
videowriter = cv2.VideoWriter("video_1280_720"+".avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 60, (1280,720))

success = cap.read()

while success:
    success, img1 = cap.read()
    try:
         img = cv2.resize(img1, (1280, 720), interpolation=cv2.INTER_LINEAR)
         videowriter.write(img)
    except:
         break


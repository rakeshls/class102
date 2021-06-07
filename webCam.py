import cv2
def take_snap():
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        print(ret)
        cv2.imwrite("Niayti.jpg",frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snap()
import time
import  random
import cv2
import dropbox
start = time.time()
def take_snap():
    number=random.randint(0,100)
    videoCaptuerObject=cv2.VideoCaptuer(0)
    result = True
    while(result):
        ret,frame=videoCaptuerObject.read()
        img = "img"+str(number)+".png"
        cv2.imwrite(img,frame)
        start = time.time
        result = False
    return img 
    print("snapshort taken")
    videoCaptuerObject.release()
    cv2.destroyAllWindows()
def upload_file(img):
    access_token=""
    file = img_counter
    file_from = file
    file_to = "/New/"+(img)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
#print(time.time())
#print(random.randint(0,9))
def main():
    while(True):
        if((time.time()-start)>=300):
            name=take_snap()
            upload_file(name)
main()
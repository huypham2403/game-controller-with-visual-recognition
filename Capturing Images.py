import cv2
import numpy as np

vc = cv2.VideoCapture(0)
pic_no = 10
total_pic = 3000
flag_capturing = False
path = "train_data"
while(vc.isOpened()):
    # read image
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
    
    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(frame, (500,400), (300,200), (0,255,0),0)
    
    cv2.imshow("image", frame)
    
    crop_img = frame[200:400, 300:500]
    
    if flag_capturing:
        
        pic_no += 1
        save_img = cv2.resize(crop_img, (64,64))
        save_img = np.array(save_img)
        cv2.imwrite(path + "/" + str(pic_no) + ".jpg", save_img)
        
    
    keypress = cv2.waitKey(1)
    
    if pic_no == total_pic:
        flag_capturing = False
        break
    
    if keypress == ord('q'):
        break
    elif keypress == ord('c'):
        flag_capturing = True

vc.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
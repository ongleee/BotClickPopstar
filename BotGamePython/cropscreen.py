import cv2
import time
import numpy as np
from ppadb.client import Client as adb

client = adb(host='127.0.0.1', port=5037)
LD = client.devices()
device = LD[0]
print("My Device is name:", device)

def save():
    savess = device.screencap()
    with open('screen.png', 'wb') as f:
        f.write(savess)
        time.sleep(.3)
    print("Screenshot saved as screen.png")

save()
sceenshot = cv2.imread('screen.png')
test = sceenshot.shape
print(test)
end_point = (test[1], test[0])
screenshot_with_rectangle = cv2.rectangle(sceenshot.copy() , (0,test[0] - 1590) , end_point , (0,255,0) , 3 )

cv2.imwrite('screen_with_rectangle.png' , screenshot_with_rectangle)
print("Ok")

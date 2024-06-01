import cv2 , time , numpy
from ppadb.client import Client as adb

client = adb(host='127.0.0.1' , port=5037)
LD = client.devices()
device = LD[0]
print("My Device is name : " , LD[0])

def save():
    savess = LD[0].screencap()
    with open('screen.png' , 'wb') as f:
        f.write(savess)
        time.sleep(.3)
    print("Screenshot saved as screen.png")
    

choice = ['image/Bottom.png','image/BottomHide.png', 'image/blueX.png' , 'image/blueY.png' , 'image/greenX.png' ,
           'image/greenY.png' ,'image/greenXdiamondR.png', 'image/pinkX.png' , 'image/pinkY.png' ,'image/redX.png' ,'image/redY.png','image/yellowX.png' , 'image/yellowY.png'  ]



def check(color):
    template = cv2.imread(color)
    screen = cv2.imread('screen.png')

    test = screen.shape[:2]
    end_point = (test[1] , test[0])
    screenshot_with_rectangle = cv2.rectangle(screen.copy() , (0,test[0] - 1590) , end_point , (0,255,0) , 3 )
    modified_image = screenshot_with_rectangle

    if template is None:
        print(f"ไม่สามารถโหลดรูปภาพเทมเพลต: {color}")
        return
    if screen is None:
        print("ไม่สามารถโหลดรูปภาพหน้าจอ: screen.png")
        return

    result = cv2.matchTemplate(modified_image, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    print(f"min_val: {min_val}, min_loc: {min_loc}")

    if min_val <= 0.6:
        x, y = min_loc
        device.shell(f'input tap {x + 10} {y + 10}')

        print(f"{color}: ({x}, {y})")

        h , w = template.shape[:2]
        cv2.rectangle(template, (x,y) , (x+w , y+h) ,(0,255,0) , 2)
        
      
        cv2.imshow("output" , template)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

    else:
        print(f"{color} ไม่พบการจับคู่ที่ตรงกัน")

while True:
    save()
    for color in choice:
        check(color)
    time.sleep(1)
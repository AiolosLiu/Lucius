#  import os
#
# dirname = '/home/ming/AI/faces/small_face/3'
# os.chdir(dirname)
# files = os.listdir(dirname)
# for i, f in enumerate(files):
#     os.rename(f, str(i) + '.jpg')
import cv2, freenect


while True:
    array, _ = freenect.sync_get_video()
    frame = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    cv2.imshow('RGB image',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

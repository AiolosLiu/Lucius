import os, sys, math, cv2
from PIL import Image
import numpy as np

ix = -1
iy = -1


def Distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx * dx + dy * dy)


def ScaleRotateTranslate(image, angle, center=None, new_center=None, scale=None, resample=Image.BICUBIC):
    if (scale is None) and (center is None):
        return image.rotate(angle=angle, resample=resample)
    nx, ny = x, y = center
    sx = sy = 1.0
    if new_center:
        (nx, ny) = new_center
    if scale:
        (sx, sy) = (scale, scale)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    a = cosine / sx
    b = sine / sx
    c = x - nx * a - ny * b
    d = -sine / sy
    e = cosine / sy
    f = y - nx * d - ny * e
    return image.transform(image.size, Image.AFFINE, (a, b, c, d, e, f), resample=resample)


def CropFace(image, eye_left=(0, 0), eye_right=(0, 0), offset_pct=(0.2, 0.2), dest_sz=(70, 70)):
    # calculate offsets in original image
    offset_h = math.floor(float(offset_pct[0]) * dest_sz[0])
    offset_v = math.floor(float(offset_pct[1]) * dest_sz[1])
    # get the direction
    eye_direction = (eye_right[0] - eye_left[0], eye_right[1] - eye_left[1])
    # calc rotation angle in radians
    rotation = -math.atan2(float(eye_direction[1]), float(eye_direction[0]))
    # distance between them
    dist = Distance(eye_left, eye_right)
    # calculate the reference eye-width
    reference = dest_sz[0] - 2.0 * offset_h
    # scale factor
    scale = float(dist) / float(reference)
    # rotate original around the left eye
    image = ScaleRotateTranslate(image, center=eye_left, angle=rotation)
    # crop the rotated image
    crop_xy = (eye_left[0] - scale * offset_h, eye_left[1] - scale * offset_v)
    crop_size = (dest_sz[0] * scale, dest_sz[1] * scale)
    image = image.crop(
        (int(crop_xy[0]), int(crop_xy[1]), int(crop_xy[0] + crop_size[0]), int(crop_xy[1] + crop_size[1])))
    # resize it
    image = image.resize(dest_sz, Image.ANTIALIAS)
    return image


def draw_circle(event, x, y, flags, param):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ix, iy = x, y


if __name__ == "__main__":
    p = 3
    dirname = '/home/ming/AI/faces/raw_face/' + str(p)
    os.chdir(dirname)
    # image = Image.open("1.jpg")
    # image1 = cv2.imread('0.jpg')
    # cv2.imshow('image', image1)
    # cv2.waitKey()
    files = os.listdir(dirname)
    for i, f in enumerate(files):
        # image = Image.open(dirname + str(i) + '.jpg')
        image = Image.open(str(i) + '.jpg')
        img = cv2.imread(str(i) + '.jpg')
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_circle)
        while True:
            cv2.imshow('image', img)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                raise KeyboardInterrupt
            elif k == ord('q'):
                leye = (ix, iy)
                print(leye)
            elif k == ord('w'):
                reye = (ix, iy)
                print(reye)
                break
        CropFace(image, eye_left=leye, eye_right=reye, offset_pct=(0.2, 0.2), dest_sz=(200, 200)).save(
            '/home/ming/AI/faces/small_face/' + str(p) + '/s' + str(i) + '.jpg')
        CropFace(image, eye_left=leye, eye_right=reye, offset_pct=(0.3, 0.3), dest_sz=(200, 200)).save(
            '/home/ming/AI/faces/big_face/' + str(p) + '/b' + str(i) + '.jpg')
        # CropFace(image, eye_left=(252, 364), eye_right=(420, 366), offset_pct=(0.2, 0.2), dest_sz=(200, 200)).save(
        #     "arnie_20_20_200_200.jpg")
        # CropFace(image, eye_left=(252, 364), eye_right=(420, 366), offset_pct=(0.3, 0.3), dest_sz=(200, 200)).save(
        #     "arnie_30_30_200_200.jpg")
        # CropFace(image, eye_left=(252, 364), eye_right=(420, 366), offset_pct=(0.2, 0.2)).save("arnie_20_20_70_70.jpg")

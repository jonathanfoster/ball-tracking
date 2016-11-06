import argparse
import cv2
import imutils
import numpy as np

colors = []
lower = np.array([])
upper = np.array([])
mask = np.array([])

def on_mouse_click (event, x, y, flags, image):
    if event == cv2.EVENT_LBUTTONUP:
        colors.append(image[y,x].tolist())

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to the image file")
parser.add_argument("-l", "--lower", help="HSV lower bounds")
parser.add_argument("-u", "--upper", help="HSV upper bounds")
args = vars(parser.parse_args())

if args["lower"] and args["upper"]:
  lower = np.fromstring(args["lower"], sep=",")
  upper = np.fromstring(args["upper"], sep=",")

image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

if lower.any() and upper.any():
  mask = cv2.inRange(hsv, lower, upper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)

while True:
    cv2.imshow("image", hsv)
    cv2.setMouseCallback("image", on_mouse_click, hsv)

    if mask.any():
      cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

if not colors:
  exit

minh = min(c[0] for c in colors)
mins = min(c[1] for c in colors)
minv = min(c[2] for c in colors)

maxh = max(c[0] for c in colors)
maxs = max(c[1] for c in colors)
maxv = max(c[2] for c in colors)

print [minh, mins, minv], [maxh, maxs, maxv]

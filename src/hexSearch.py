import cv2
import imutils as im
import numpy as np

area = []
img = cv2.imread("/home/rahul/Pictures/hex.jpg")
print img.shape
# img = im.resize(img,340,680,cv2.INTER_LANCZOS4)
output = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




adThresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,1)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(adThresh,cv2.MORPH_OPEN,kernel, iterations = 1)

opening = cv2.erode(opening,(3,3),iterations=2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=2)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

#try
erode = cv2.erode(sure_bg,(5,5),iterations=1,borderType=2,borderValue=cv2.MORPH_HITMISS)
edge = cv2.Canny(erode,35,55,apertureSize=5,L2gradient=True)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 0

# Change thresholds
params.minThreshold = 2
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 10

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.001

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(edge)
im_with_keypoints = cv2.drawKeypoints(output, keypoints, np.array([]), (0, 255, 0),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

if (len(keypoints) > 0):

    for keyPoint in keypoints:
        x = int(keyPoint.pt[0])
        y = int(keyPoint.pt[1])
        s = int(keyPoint.size)
        ang = keyPoint.angle
        area1 = np.pi*(s/2)**2
        print x, y, s, ang,"Area: ",area1
        area.append(area1)
        #     cv2.circle(output, (x, y), int(s / 2), (0, 0, 255))
        cv2.circle(output, (x, y), 2, (0, 255, 255), -1)


# # #----------uncomment for contour method--------------------
#
# cnts = cv2.findContours(edge.copy(),cv2.RETR_CCOMP,
#                             cv2.CHAIN_APPROX_SIMPLE)[-2]
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#
# print "no. of hex detected: ",len(cnts)
#
# for i in range(len(cnts)):
#
#     M = cv2.moments(cnts[i])
#     if M["m00"]!= 0:
#         center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#         print center
#         cv2.circle(img,center,2,(0,0,255),-1)

# # ------------------------------------------------------------
print "no. of cells : ",len(keypoints),"minimum area: ",min(area),"maximum area: ",max(area)
cv2.imshow("input_image",img)
cv2.imshow("thresh", adThresh)
cv2.imshow("opening",opening)
cv2.imshow("sure_bg",sure_bg)
cv2.imshow("sure_fg",sure_fg)
cv2.imshow("unknown",unknown)
cv2.imshow("Area Showing Output: ",im_with_keypoints)
cv2.imshow("edge: ",edge)
cv2.imshow("output: ",output)

cv2.waitKey(0)
cv2.destroyAllWindows()
import os
import cv2

searching = cv2.imread('D:/image/goose_test.jpg', cv2.IMREAD_COLOR)
searchHLS = cv2.cvtColor(searching, cv2.COLOR_BGR2HLS)
searchhistogram = cv2.calcHist([searchHLS], [0], None, [256], [0, 256])
findlist = {}

for root, dirs, files in os.walk('D:/image'):
    for fname in files:
        full_fname = os.path.join(root, fname)
        # print(full_fname)

        imgNames = cv2.imread(full_fname)
        imgsHLS = cv2.cvtColor(imgNames, cv2.COLOR_BGR2HLS)


        histogram = cv2.calcHist([imgsHLS], [0], None, [256], [0, 256])
        # print(histogram)

        matching_score = cv2.compareHist(histogram, searchhistogram, cv2.HISTCMP_CORREL)
        if (matching_score > 0.0):
            findlist[full_fname] = matching_score
            # print(findlist)
    findlist_x = sorted(findlist.items(), key=(lambda x: x[1]), reverse=True)
    for k in findlist_x:
        print(k)

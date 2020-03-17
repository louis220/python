import os
import cv2



searching = cv2.imread('D:/image/pilsner_test.jpg', cv2.IMREAD_COLOR)
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
        if (matching_score > 0.4):
            findlist[full_fname] = matching_score
            # print(findlist)
    findlist_x = sorted(findlist.items(), key=(lambda x: x[1]), reverse=True)

    sift = cv2.xfeatures2d.SIFT_create()
    findlist2={}

    for k in findlist_x:
        # full_fname = os.path.join(root, )
        # print(full_fname)
        imgNames = cv2.imread(findlist_x)

        kp1, des1 = sift.detectAndCompute(k, None)
        kp2, des2 = sift.detectAndCompute(imgNames, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        img3 = cv2.drawMatchesKnn(k, kp1, imgNames, kp2, good, None, flags=2)
        count = len(good)
        if (count > 0):
            findlist2[full_fname] = count
            # print(count)
        findlist_y = sorted(findlist.items(), key=(lambda x: x[1]), reverse=True)
for m in findlist_y:
    print(m)




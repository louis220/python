import os
import cv2

searching = cv2.imread('D:/image_test/hoo_test.jpg', cv2.IMREAD_COLOR)
sift = cv2.xfeatures2d.SIFT_create()
findlist={}
for root, dirs, files in os.walk('D:/image'):
    for fname in files:
        full_fname = os.path.join(root, fname)
        # print(full_fname)
        imgNames = cv2.imread(full_fname)

        kp1, des1 = sift.detectAndCompute(searching, None)
        kp2, des2 = sift.detectAndCompute(imgNames, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        img3 = cv2.drawMatchesKnn(searching, kp1, imgNames, kp2, good, None, flags=2)
        count = len(good)
        if (count > 0 ):
            findlist[full_fname] = count
            # print(count)
        findlist_x = sorted(findlist.items(), key=(lambda x:x[1]), reverse=True)

    for k in findlist_x:
        print(k)
    # target = findlist_x[1]
    # print(target)

# cv2.imshow('result', target)
# cv2.waitKey(0)




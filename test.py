import cv2
import numpy as np
import glob

# # Membaca Image
image = cv2.imread("Dataset/Kemangi/001.jpg")
# # print(image)
# print(image.shape)
#
# # cv2.imshow("001", image)
#
# # resize image (ignore aspect ratio)
im_resized = cv2.resize(image, (400,400))
# # cv2.imshow('im_resized',im_resized)
#
# # # adjust image contrast
# im_adjusted = cv2.addWeighted(im_resized, 1.5, np.zeros(im_resized.shape, im_resized.dtype), 0, -100)
# cv2.imshow('im_adjusted', im_adjusted)
#
# #
# # # convert image to grayscale\n",
# # im_gray = cv2.cvtColor(im_resized, cv2.COLOR_BGR2GRAY),
# # cv2.imshow('Original Image',im_resized)
# # cv2.imshow('Grayscale Image',im_gray)
#
# # detect edges
# im_edges = cv2.Canny(im_resized, 100, 200)
#
# cv2.imshow("Original Image", im_resized)
# cv2.imshow("Detected Edges", im_edges)


imdir = 'Dataset/Kemangi/'
ext = ['jpg']

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

images = [cv2.imread(file) for file in files]

i = 1
for img in images:
    im_adjusted = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, -100)
    im_edges = cv2.Canny(im_adjusted, 100, 200)
    im_name = "Dataset/kemangi_edges_test/" + str(i) + ".jpg"
    cv2.imwrite(im_name, im_edges)
    i += 1

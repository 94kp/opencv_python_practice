import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
from collections import defaultdict

from numpy.lib.npyio import load

# constants

SIZE_IMAGE = 20
NUMBER_CLASSES = 10

def raw_pixels(img):
    return img.flatten()

def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11'] / m['mu02']
    M = np.float32([[1, skew, -0.5 * SIZE_IMAGE * skew], [0, 1, 0]])
    img = cv2.warpAffine(img, M, (SIZE_IMAGE, SIZE_IMAGE), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    return img

def get_accuracy(predictions, labels):

    accuracy = (np.squeeze(predictions) == labels).mean()
    return accuracy * 100

def load_digits_and_labels(big_image):
    ## Returns all the digits from the big image and creates the corresponding labels for each image

    digits_img = cv2.imread(big_image, 0)
    number_rows = digits_img.shape[1] / SIZE_IMAGE
    rows = np.vsplit(digits_img, digits_img.shape[0] / SIZE_IMAGE)

    digits = []
    for row in rows:
        row_cells = np.hsplit(row, number_rows)
        for digit in row_cells:
            digits.append(digit)
    digits = np.array(digits)

    #Create labels
    labels = np.repeat(np.arange(NUMBER_CLASSES), len(digits) / NUMBER_CLASSES)
    return digits, labels

    # compute descriptors

def get_hog():
    hog = cv2.HOGDescriptor((SIZE_IMAGE, SIZE_IMAGE), (8, 8), (4, 4), (8, 8), 9, 1, -1, 0, 0.2, 1, 64, True)
    print("hog descriptor size: '{}'".format(hog.getDescriptorSize()))
    return hog

digits, labels = load_digits_and_labels('images\digits.png')
hog = get_hog()

rand = np.random.RandomState(1234)

shuffle = rand.permutation(len(digits))
digits, labels = digits[shuffle], labels[shuffle]

results = defaultdict(list)

hog_descriptors =[]

for img in digits:
    hog_descriptors.append(hog.compute(deskew(img)))
hog_descriptors = np.squeeze(hog_descriptors)

split_values = np.arange(0.1, 1, 0.1)

resultst = defaultdict(list)

knn = cv2.ml.KNearest_create()

for split_value in split_values:
    partition = int(split_value * len(hog_descriptors))
    hog_descriptors_train, hog_descriptors_test = np.split(hog_descriptors, [partition])
    labels_train, labels_test = np.split(labels, [partition])
    print("Training KNN - HOG features")
    knn.train(hog_descriptors_train, cv2.ml.ROW_SAMPLE, labels_train)

    for k in np.arange(1, 10):
        ret, result, neighbours, dist = knn.findNearest(hog_descriptors_test, k)
        acc = get_accuracy(result, labels_test)
        print(" {}".format("%.2f" % acc))
        results[int(split_value * 100)].append(acc)


fig = plt.figure(figsize=(12, 5))
plt.suptitle("kNN hadwritten digits recognition", fontsize=14, fontweight="hold")
fig.patch.set_facecolor('silver')

ax = plt.subplot(1, 1, 1)
ax.set_xlim(0, 10)
dim = np.arange(1, 10)

for key in results:
    ax.plot(dim, results[key], linestyle='--', marker='o', label=str(key) + "%")

plt.legend(loc='upper left', title="% training")
plt.title('Accuracy of knn')
plt.xlabel("number of k")
plt.ylabel("accuracy")
plt.show()
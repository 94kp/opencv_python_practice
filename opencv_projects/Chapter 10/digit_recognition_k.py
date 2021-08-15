import cv2
import numpy as np
import argparse
from collections import defaultdict
import matplotlib.pyplot as plt

from numpy.lib.npyio import load

# constants

SIZE_IMAGE = 20
NUMBER_CLASSES = 10

def raw_pixels(img):
    return img.flatten()

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

digits, labels = load_digits_and_labels('images\digits.png')

rand = np.random.RandomState(1234)

shuffle = rand.permutation(len(digits))
digits, labels = digits[shuffle], labels[shuffle]

raw_descriptors = []
for img in digits:
    raw_descriptors.append(np.float32(raw_pixels(img)))
raw_descriptors = np.squeeze(raw_descriptors)

partition = int(0.5 * len(raw_descriptors))
raw_descriptors_train, raw_descriptors_test = np.split(raw_descriptors, [partition])
labels_train, labels_test = np.split(labels, [partition])

print('Training knn with raw pixel as features')
knn = cv2.ml.KNearest_create()
knn.train(raw_descriptors_train, cv2.ml.ROW_SAMPLE, labels_train)

k = 5 
ret, result, neighbours, dist = knn.findNearest(raw_descriptors_test, k)

acc = get_accuracy(result, labels_test)
print(f"Accuracy: {acc}")

results = defaultdict(list)

for k in np.arange(1, 10):
    ret, result, neighbours, dist = knn.findNearest(raw_descriptors_test, k)
    acc = get_accuracy(result, labels_test)
    print(" {}".format("%.2f" % acc))
    results['50'].append(acc)

fig, ax = plt.subplots(1, 1)
ax.set_xlim(0, 10)
dim = np.arange(1, 10)

for key in results:
    ax.plot(dim, results[key], linestyle='--', marker='o', label="50%")

plt.legend(loc='upper left', title= "% training")
plt.title('Accuracy of the KNN model varying k')
plt.xlabel("number of k")
plt.ylabel("accuracy")
plt.show()

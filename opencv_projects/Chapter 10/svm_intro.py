import numpy as np
import cv2

def svm_init(C=12.5, gamma=0.50625):
    model = cv2.ml.SVM_create()
    model.setGamma(gamma)
    model.setC(C)
    model.setKernel(cv2.ml.SVM_LINEAR)
    model.setType(cv2.ml.SVM_C_SVC)
    model.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))

    return model

def svm_train(model, samples, responses):
    model.train(samples, cv2.ml.ROW_SAMPLE, responses)
    return model

def show_svm_response(model, image):
    colors = {1: (255, 255, 0), -1: (0, 255, 255)}

    for i in range(image.shape[1]):
        for j in range(image.shape[1]):
            sample = np.atrix([[j, i]], dtype=np.float32)
            response = svm_predict(model, sample)

            image[i, j] = colors[response.item(0)]

    cv2.circle(image, (500,10), 10, (255, 0, 0), -1)
    cv2.circle(image, (550, 100), 10, (255, 0, 0), -1)
    cv2.circle(image, (300, 10), 10, (255, 0, 0), -1)
    cv2.circle(image, (500, 300), 10, (255, 0, 0), -1)
    cv2.circle(image, (10, 600), 10, (255, 0, 0), -1)

    support_vectors = model.getUncompressedSupportVectors()

    for i in range(support_vectors.shape[0]):
        cv2.circle(image, (support_vectors[i, 0], support_vectors[i, 1]), 15, (0, 0, 255), 6)


labels = np.array([1, 1, -1, -1, -1])
data = np.matrix([500, 10], [550, 100], [300, 10], [500, 300], [10, 600], dtype = np.float32)

svm_model = svm_init(C=12.5, gamma=0.50625)

svm_train(svm_model, data, labels)

img_output = np.zeroes((640, 640, 3), dtype="uint8")

show_svm_rsponse(svm_model, img_output)
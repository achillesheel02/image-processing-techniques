from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import argparse

def sigmoid_activation(x):
    return 1.0/(1+np.exp(-x))

def predict(X,W):
    preds=sigmoid_activation(X.dot(W))
    preds[preds <= 0.5] = 0
    preds[preds > 0] = 1
    return preds


def next_batch(X, y, batchSize):
    # loop over our dataset ‘X‘ in mini-batches, yielding a tuple of
    # the current batched data and labels
    for i in np.arange(0, X.shape[0], batchSize):
        yield (X[i:i + batchSize], y[i:i + batchSize])


ap = argparse.ArgumentParser()
ap.add_argument( "-e",'--epochs', type=float, default=100,
                 help="# of epochs")
ap.add_argument("-a",'--alpha', type=float, default=.01,
                 help="learning rate")

args = vars(ap.parse_args())

(X, y) = make_blobs(n_samples=1000, n_features=2, centers=2,
cluster_std=1.5, random_state=1)
y = y.reshape((y.shape[0], 1))

# insert a column of 1’s as the last entry in the feature
# matrix -- this little trick allows us to treat the bias
# as a trainable parameter within the weight matrix
X = np.c_[X, np.ones((X.shape[0]))]
# the data for training and the remaining 50% for testing
(trainX, testX, trainY, testY) = train_test_split(X, y,
test_size=0.5, random_state=42)

print("[INFO] training...")
W = np.random.randn(X.shape[1], 1)
losses = []

for epoch in np.arange(0, args["epochs"]):
    epochLoss = []
    for (batchX, batchY) in next_batch(X, y, 32):
        preds = sigmoid_activation(batchX.dot(W))
        error = preds - batchY
        epochLoss.append(np.sum(error ** 2))

        gradient = batchX.T.dot(error)
        W += -args["alpha"] * gradient

    loss = np.average(epochLoss)
    losses.append(loss)
    if epoch == 0 or (epoch + 1) % 5 == 0:

        print("[INFO] epoch={}, loss={:.7f}".format(int(epoch + 1),
                                                    loss))

print("[INFO] evaluating...")
preds = predict(testX, W)
print(classification_report(testY, preds))



# construct a figure that plots the loss over time
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, args["epochs"]), losses)
plt.title( "Training Loss")
plt.xlabel("Epoch #" )
plt.ylabel("Loss" )
plt.show()

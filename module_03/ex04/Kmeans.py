from matplotlib import pyplot as plt
import sys
import numpy as np


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        """Parse, read dataset, fit dataset, 
        display coordinates of the different centroids and the associated region
            for the case ncentroid=4
        display the number of individuals associated to ech centroid"""
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
       
       
    def init_centroids(self, X):
        centroid = X.copy()
        np.random.shuffle(centroid)
        self.centroids = centroid[:self.ncentroid, 1:]
        
    def move_centroids(self, X, closest):
        """returns the new centroids assigned from the points closest to them"""
        self.centroids = np.array([X[closest == k].mean(axis=0) for k in range(self.centroids.shape[0])])
        
       
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        
        self.init_centroids(X)
        
        closest = []
        for i in range(0, self.max_iter):
            closest = self.predict(X[:, 1:]) # = closest centroid
            self.move_centroids(X[:, 1:], closest)

        array = np.append(X, np.transpose([closest]), axis = 1)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_zlabel('Bone density')
        
        # cluster = []
        # for i in range(self.ncentroid):
        #     np.append()
            
        array = array[array[:, 4].argsort()]
        zero = array[array[:, 4] == 0]
        one = array[array[:, 4] == 1]
        two = array[array[:, 4] == 2]
        three = array[array[:, 4] == 3]

        res = self.get_origin()

        ax.scatter(zero[:, 1], zero[:, 2], zero[:, 3], c='b')
        ax.scatter(one[:, 1], one[:, 2], one[:, 3], c='purple')
        ax.scatter(two[:, 1], two[:, 2], two[:, 3], c='g')
        ax.scatter(three[:, 1], three[:, 2], three[:, 3], c='orange')
        ax.scatter(self.centroids[:, 0], self.centroids[:, 1], self.centroids[:, 2], c='r', s=100)
        
        ax.legend(res, ncol=5)
        plt.show()
       


    def get_origin(self):
        res = ['', '', '', '', 'Centroids']
        maxinrows = np.argmax(self.centroids, axis=0)

        temp = np.append(self.centroids, np.array(range(0, self.ncentroid)).reshape((4, 1)), axis=1)

        res[int(temp[maxinrows[0]][3])] = 'Belt'
        temp = np.delete(temp, maxinrows[0], axis=0)
        mininrows = np.argmin(temp, axis=0)
        res[int(temp[mininrows[1]][3])] = 'Venus'
        temp = np.delete(temp, mininrows[1], axis=0)
        maxinrows = np.argmax(temp, axis=0)
        res[int(temp[maxinrows[1]][3])] = 'Earth'
        temp = np.delete(temp, maxinrows[1], axis=0)
        res[int(temp[0][3])] = 'Mars'
        return res

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        dist = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(dist, axis=0)


def parse_args(argv):
    ncentroid = 0
    max_iter = 0
    file = ""
    if len(argv) > 4 or len(argv) < 2:
        raise Exception("Usage: [filepath] [max_iter] [ncentroid]")
    for element in argv:
        pos = element.find('ncentroid=')
        if pos != -1 and ncentroid == 0:
            ncentroid = int(element[10:])
        elif pos != -1 and ncentroid > 0:
            return None
        pos = element.find('max_iter=')
        if pos != -1 and max_iter == 0:
            max_iter = int(element[9:])
        elif pos != -1 and max_iter > 0:
            return None
        pos = element.find('filepath=')
        if pos != -1 and len(file) == 0:
            file = element[9:]
        elif pos != -1 and len(file) > 0:
            return None
        
    if len(file) == 0:
        return None
    
    return file, max_iter, ncentroid


def main():
    # Parsing des arguments
    args = parse_args(sys.argv)
    if args is None:
        print("Input Error")
        quit(1)
        
    # Parsing du csv
    with open(args[0], 'r') as x:
        file = np.genfromtxt(args[0], delimiter=",", skip_header=1)
    data = np.array(file)

    kmeans = KmeansClustering(args[1], args[2])
    kmeans.fit(data)


if __name__ == '__main__':
    main()

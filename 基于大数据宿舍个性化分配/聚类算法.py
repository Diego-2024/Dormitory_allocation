from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import warnings
from sklearn.metrics import silhouette_samples

warnings.filterwarnings("ignore")


def JuLei(data):


    def juleifuntion(i):
        julei = KMeans(n_clusters=i)
        julei.fit(data)
        labels = julei.labels_
        return labels

    def juleimeans(i):
        julei = KMeans(n_clusters=i)
        julei.fit(data)
        labels = julei.labels_
        score = silhouette_samples(data, labels)
        means = np.mean(score)
        return means

    def findmeans():
        y = []
        for i in range(2, 10):
            means = juleimeans(i)
            y.append(means)
        max_value = max(y)
        max_index = y.index(max_value)
        return max_index + 1

    return juleifuntion(findmeans())

from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from .data import PenguinsData
from .utils import save_model


class Models:
    def __init__(self, data: PenguinsData):
        self._data: PenguinsData = data

    def save_models(self):
        self._logistic_regression()
        self._svm()
        self._decision_tree()
        self._knn()

    def _logistic_regression(self):
        lr = OneVsRestClassifier(LogisticRegression(C=100.0, random_state=1, solver='lbfgs'))
        lr.fit(self._data.X_TRAIN, self._data.Y_TRAIN)
        save_model(lr, "lr", self._data.DV)

    def _svm(self):
        svm = SVC(kernel='linear', C=1.0, random_state=1, probability=True)
        svm.fit(self._data.X_TRAIN, self._data.Y_TRAIN)
        save_model(svm, "svm", self._data.DV)

    def _decision_tree(self):
        dt = DecisionTreeClassifier(criterion='gini', max_depth=4,
                                    random_state=1)
        dt.fit(self._data.X_TRAIN, self._data.Y_TRAIN)
        save_model(dt, "dt", self._data.DV)

    def _knn(self):
        knn = KNeighborsClassifier(n_neighbors=3, p=2, metric='minkowski')

        knn.fit(self._data.X_TRAIN, self._data.Y_TRAIN)
        save_model(knn, "knn", self._data.DV)

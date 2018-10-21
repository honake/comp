import numpy as np
import math
import time

def load_iris():
    from sklearn.datasets import load_iris
    iris = load_iris()
    return train_test_split(iris.data, iris.target, test_size=0.20)

class RandomForestClassifier(object):
    def __init__(self, criterion='gini', random_state=100, max_depth=3, min_samples_leaf=3):
        # Decision Tree Set Up
        self.criterion = criterion
        self.random_state = random_state
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.pred = None
        
        # Decision Tree Container
        self.decision_tree_container = []
        
    def fit(self, X, y, sample_num):
        start = time.time()
        
        from sklearn.tree import DecisionTreeClassifier
        
        nrow, ncol = X.shape
        sample_size = math.floor(np.sqrt(nrow))
        feature_size = math.floor(np.sqrt(ncol))
        
        if(len(self.decision_tree_container) != 0):
            self.decision_tree_container = []
        
        for i in range(0, sample_num):
            
            # Bootstrap
            idx = np.random.choice(nrow, sample_size, replace=False)
            X_sub, y_sub = X[idx], y[idx]
            
            # Week learner
            weekTree = DecisionTreeClassifier(criterion = self.criterion,
                random_state = self.random_state,
                max_depth = self.max_depth,
                min_samples_leaf = self.min_samples_leaf,
                max_features = feature_size)
            
            self.decision_tree_container.append(weekTree.fit(X_sub, y_sub))

        elapsed_time = time.time() - start
        print("Elapsed Time: {0}".format(elapsed_time) + "[sec]")
        
        return True
        
    def predict(self, X):
        from scipy import stats
        y = []
        
        for _x in X:
            week_preds = [clf.predict(_x.reshape(1,-1))[0] for clf in self.decision_tree_container]
            majority = stats.mode(week_preds)[0][0]
            y.append(majority)

        self.pred = y

        return y
    
    def summary(self, y_test):
        from sklearn.metrics import accuracy_score
        if self.pred == None:
            print("Predicted Value Not Found")
        else:
            print("Accuracy: {0}".format(accuracy_score(y_test, self.pred)))

# Execution
X_train, X_test, y_train, y_test = load_iris()
rf = RandomForestClassifier(criterion='gini', random_state=100, max_depth=3, min_samples_leaf=5)
rf.fit(X_train, y_train, sample_num=1000)
rf.predict(X_test)
rf.summary(y_test)

# -> Elapsed Time: 0.18492698669433594[sec]
# -> Accuracy: 0.9666666666666667

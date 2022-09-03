import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle 


dataset = pd.read_csv("creditcard.csv")
# selecting features and target 

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#feature sclaing 

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# train the model

log_classifier = LogisticRegression()
l_svm = LinearSVC(random_state=0)
svc = SVC(random_state=0)
knn = KNeighborsClassifier()


#fitting the model

log_classifier.fit(X_train,y_train)

# make the pickle file 

pickle.dump(log_classifier,open("model.pkl","wb"))



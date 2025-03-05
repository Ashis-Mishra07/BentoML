import bentoml

from sklearn import svm   # Support vector machines 
from sklearn import datasets

# Load the training data set
iris = datasets.load_iris()
X,y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma='scale')   # clf -> classifier
clf.fit(X, y)

# Save the model to bentoML local model store 

'''
When the bentoml get installed , it creates a local repository in my local drive . 
and it will store the files in that local storage first .
BentoML also do some versioning of the model , so that we can keep track of the model versions.
'''

saved_model = bentoml.sklearn.save_model("iris_clf" , clf)
print(f"Model Saved: {saved_model}")   # Model Saved: Model(tag="iris_clf:gzpw2l7z2swy7fut")


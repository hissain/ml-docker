import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()

# Create a random forest classifier
rf = RandomForestClassifier()

# Train the classifier
rf.fit(iris.data, iris.target)

# Save the trained model
joblib.dump(rf, "app/model.joblib")

print("predicted:", rf.predict([[5.1, 3.5, 1.4, 0.2]]))

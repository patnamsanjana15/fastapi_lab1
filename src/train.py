import pickle
from sklearn.datasets import load_iris

# MODIFICATION: RandomForestClassifier instead of DecisionTreeClassifier
# RandomForest builds 100 decision trees and combines their results
# This makes it much more accurate and reliable than a single tree
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset — it's built into scikit-learn, no download needed!
# Contains 150 flower samples with 4 measurements each
iris = load_iris()
X = iris.data    # the 4 measurements (features): sepal/petal length & width
y = iris.target  # the species label: 0=setosa, 1=versicolor, 2=virginica

# MODIFICATION: Train with RandomForest
# n_estimators=100 → builds 100 trees, all vote on every prediction
# random_state=42  → makes results identical every time you run train.py
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)  # ← this is where the actual "learning" happens

# Save the trained model to a .pkl file using pickle
# "wb" means "write binary" — model data is stored as binary, not text
# We save it so the API can load it instantly without retraining
with open("../model/iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("RandomForest model trained and saved successfully!")
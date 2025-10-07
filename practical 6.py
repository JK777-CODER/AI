import pandas as pd 
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

# Dataset URL and column names
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Load the dataset
dataframe = pd.read_csv(url, names=names)

# Split dataset into input features (X) and target (Y)
X = dataframe.iloc[:, 0:8]
Y = dataframe.iloc[:, 8]

# AdaBoost parameters
seed = 7
num_trees = 30

# Initialize AdaBoost classifier
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)

# Evaluate using cross-validation
results = cross_val_score(model, X, Y, cv=10)
print("Mean Accuracy:", results.mean())
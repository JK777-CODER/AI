import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.datasets import load_breast_cancer
import warnings

warnings.filterwarnings('ignore')

# Load dataset from sklearn
cancer = load_breast_cancer()

# Convert to DataFrame for easier handling
data = pd.DataFrame(cancer.data, columns=cancer.feature_names)
data['diagnosis'] = pd.Series(cancer.target)  # 0 = malignant, 1 = benign

# Map diagnosis to meaningful labels (optional)
data['diagnosis'] = data['diagnosis'].map({0: 'malignant', 1: 'benign'})

# Data Exploration
print(data.head())
print(data.tail())
print("Shape of data:", data.shape)
print(data.info())

# Plot diagnosis distribution
data['diagnosis'].value_counts().plot(kind='bar')
plt.title("Diagnosis Distribution")
plt.show()

# Correlation heatmap (on numeric features)
plt.figure(figsize=(12, 10))
sns.heatmap(data.select_dtypes(include=np.number).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Feature Selection
selected_features = ['mean radius', 'mean texture', 'mean smoothness']

X = data[selected_features].values
Y = data['diagnosis'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=43)

# Build and train model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predictions and evaluation
y_pred = gnb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, pos_label='malignant')
confusion = confusion_matrix(y_test, y_pred)

print("Accuracy Score: {:.2f}%".format(accuracy * 100))
print("F1 Score:", f1)
print("Confusion Matrix:\n", confusion)

# Predicting New Data
new_data_point = [[14.58, 21.53, 0.1054]]
diagnosis_prediction = gnb.predict(new_data_point)
print("Predicted Diagnosis for new data point:", diagnosis_prediction[0])

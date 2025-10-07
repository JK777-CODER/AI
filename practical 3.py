import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Load dataset
df = pd.read_csv("salaries.csv")
print(df.head())

# Features (inputs) and target (output)
inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']

# Encode categorical columns
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

print(inputs.head())

# Final input data without categorical strings
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
print(inputs_n)

# Train decision tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)

# Example prediction (company=2, job=2, degree=2)
print("Prediction:", model.predict([[2, 2, 2]]))  

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.3, random_state=1)

# Train on training set
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Plot decision tree
fig = plt.figure(figsize=(20, 15))
_ = plot_tree(
    model,
    feature_names=inputs_n.columns.tolist(),
    class_names=['<=100k', '>100k'],
    filled=True
)
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load MNIST data
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train logistic regression model
logistic_model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
logistic_model.fit(X_train, y_train)

# Predict and evaluate
y_train_pred = logistic_model.predict(X_train)
y_test_pred = logistic_model.predict(X_test)

train_accuracy_logistic = accuracy_score(y_train, y_train_pred)
test_accuracy_logistic = accuracy_score(y_test, y_test_pred)

print(f"Training accuracy (Logistic Regression): {train_accuracy_logistic}")
print(f"Test accuracy (Logistic Regression): {test_accuracy_logistic}")

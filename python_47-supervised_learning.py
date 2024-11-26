from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = [[1500], [1800], [2400], [3000], [3500], [4000]]
y = [400000, 500000, 600000, 650000, 700000, 750000]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Test Data Output:", y_test)
print("Test Data Predicted Output:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = [[25, 40000], [30, 50000], [35, 60000], [40, 70000], [45, 80000]]
y = [0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Test Data Output: {y_test}")
print(f"Test Data Predicted Output: {y_pred}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")


from sklearn.svm import SVC

X = [[2, 3], [4, 6], [6, 8], [1, 1], [2, 2], [7, 7]]
y = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Test Data Output: {y_test}")
print(f"Test Data Predicted Output: {y_pred}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")


from sklearn.tree import DecisionTreeClassifier

X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y = [0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Test Data Output: {y_test}")
print(f"Test Data Predicted Output: {y_pred}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
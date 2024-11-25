import numpy
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = numpy.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.8, 3.0]).reshape(-1, 1)
Y = numpy.array([100, 120, 150, 200, 220, 270, 300])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(Y_test, Y_pred)}")

plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Predicted Line")

plt.xlabel("House Size (1000 sqft)")
plt.ylabel("House Price ($1000s)")
plt.legend()

plt.savefig("Images/house_prices.png")


from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

X = numpy.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.8, 3.0]).reshape(-1, 1)

scaler = StandardScaler()
print(f"X Scaled: {scaler.fit_transform(X)}")

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform([['Red'], ['Green'], ['Blue']]).toarray()
print(f"X Encoded: {X_encoded}")

imputer = SimpleImputer(strategy='mean')
X_with_missing = [[1], [2], [None], [4]]
print(f"X filled: {imputer.fit_transform(X_with_missing)}")


# Feed into a Model
# When we say feed data into a model, it means:

# We give the model our features (X) → the independent variables (inputs).
# Example: Age, Gender, Hours_Study, Age_Study.

# We give the model the target (y) → the dependent variable (output we want to predict).
# Example: Score.

# The model then learns the relationship between X and y.


from sklearn.linear_model import LinearRegression
import pandas as pd 


df= pd.read_csv('students.csv')

model = LinearRegression()
X_train = df[['Age', 'Gender', 'Hours_Study', 'Age_Study']]
y_train = df['Score']
X_test = df[['Age', 'Gender', 'Hours_Study', 'Age_Study']]
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

print("Predictions:", predictions)

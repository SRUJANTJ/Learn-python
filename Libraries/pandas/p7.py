# Split Data into Train/Test Sets
# Splitting data into train/test sets means dividing your dataset into two parts: one for learning, one for checking if the learning works on new data.

from sklearn.model_selection  import train_test_split
import pandas as pd 

# Load the dataset
df = pd.read_csv('students.csv')


# Features (X) and Target (y)
X = df[['Age', 'Gender', 'Hours_Study', 'Age_Study']]
y = df['Score']

print("Loading dataset:")

# Split 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)
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

# Output

# (4, 4) (2, 4)

# 4,4 => traning data 
# 2,4 => testing data




# X → Features (independent variables / inputs)
# Example: Age, Gender, Hours_Study, Age_Study

# y → Target (dependent variable / output)
# Example: Score
# So, X is the data you feed into the model, and y is what you want the model to predict.


# Parameters in train_test_split

# X, y
# The full dataset → it will split both into training and testing sets.

# test_size=0.2
# Means 20% of the data will go into the test set, and the remaining 80% into the train set.

# If you had 100 rows → 80 train, 20 test.

# You can also use test_size=0.3 for 30%, etc.

# random_state=42
# Sets a random seed for reproducibility.

# Without it → each time you run, you might get different train/test splits.

# With it (any number, not just 42) → you’ll always get the same split.

# 42 is a "fun default" in ML, but you can use any number.


# What are X_train, X_test, y_train, y_test?

# After splitting, you get four subsets:

# X_train

# Training features (inputs)

# Used to train the ML model.

# X_test

# Testing features (inputs)

# Used to test the model’s predictions.

# y_train

# Training labels/targets (outputs).

# The "answers" the model learns from.

# y_test

# Testing labels/targets (outputs).

# The "real answers" used to evaluate how well the model predicts.
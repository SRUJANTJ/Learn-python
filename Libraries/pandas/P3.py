# Create a CSV File (Simulated Dataset)

# We’ll make a simple dataset representing a student performance prediction scenario.
# At this point, you’ll have a file called students.csv in your working directory.
import pandas as pd
data = {
    'StudentID': [1, 2, 3, 4, 5],
    'HoursStudied': [5, 10, 15, 20, 25],
    'PreviousScore': [50, 60, 70, 80, 90],
    'FinalScore': [55, 65, 75, 85, 95]
}
df=pd.DataFrame(data)
df.to_csv('students.csv', index=False)




# Getting  Data into Pandas
data = pd.read_csv('students.csv')
print(data)


# Explore the Data
print("Explore the Data")


print("Data types + missing values",df.info())      # Data types + missing values
print("Summary statistics ",df.describe())  # Summary statistics (numeric only)
print(" First 5 rows",df.head())      # First 5 rows

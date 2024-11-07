# !pip install pandas
import pandas

data = [10, 20, 30, 40, 50]

series = pandas.Series(data, index=["a", "b", "c", "d", "e"])
print(f"Series:\n{series}")


df = pandas.read_csv("Files/read_example.csv")
print(f"DataFrame from CSV:\n{df}")

df.to_csv("Files/write_example.csv", index=False)


print(f"Head Of DataFrame:\n{df.head()}")
print(f"Tail Of DataFrame:\n{df.tail()}")
print(f"Info Of DataFrame:\n{df.info()}")
print(f"Statistical Summary Of DataFrame:\n{df.describe()}")


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pandas.DataFrame(data)

print(f"DataFrame:\n {pandas.DataFrame(data)}")
print(f"Ages Column:\n {df['Age']}")
print(f"Subset Of Column:\n {df[['Name', 'City']]}")
print(f"Row with Index 1:\n {df.loc[1]}")
print(f"Filtered Age (Age > 30):\n {df[df["Age"] > 30]}")


df["Salary"] = [50000, 60000, 70000]
print(f"DataFrame with Salary Column:\n {df}")

df = df.drop("Salary", axis=1)
print(f"DataFrame without Salary Column:\n {df}")


print(f"Missing Values:\n {df.isnull().sum()}")

df_filled = df.fillna(0)
print(f"DataFrame with Filled Missing Values:\n {df_filled}")

df_dropped = df.dropna()
print(f"DataFrame with Dropped Missing Values:\n {df_dropped}")
from sklearn.model_selection import train_test_split
import pandas as pd
# Split the data into training and testing sets
data_path = 'dat/raw/movielens/ratings.csv'
data = pd.read_csv(data_path)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Check the size of each set
print("Training data size:", train_data.shape)
print("Testing data size:", test_data.shape)

# Optionally, you can save these to new CSV files
train_data.to_csv('dat/raw/movielens/train_data.csv', index=False)
test_data.to_csv('dat/raw/movielens/test_data.csv', index=False)
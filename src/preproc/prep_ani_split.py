import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
data_path = 'dat/raw/anime/rating.csv'
data = pd.read_csv(data_path)
data = data.loc[data['rating'] != -1]
# Reduce the dataset size by keeping only the top 60%
reduced_data = data.iloc[:int(len(data) * 0.1)]

# Split the reduced data into training and testing sets
train_data, test_data = train_test_split(reduced_data, test_size=0.2, random_state=42)

# Check the size of each set
print("Training data size:", train_data.shape)
print("Testing data size:", test_data.shape)

# Optionally, you can save these to new CSV files
train_data.to_csv('dat/raw/anime/train_data.csv', index=False)
test_data.to_csv('dat/raw/anime/test_data.csv', index=False)
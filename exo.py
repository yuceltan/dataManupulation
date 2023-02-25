import pandas as pd
# Load the dataset
df = pd.read_csv('/Users/pc home/Downloads/googleplaystore.csv')

# Drop duplicates
df.drop_duplicates(subset='App', inplace=True)

# Drop rows with missing values:
df.dropna(inplace=True)

# Convert 'Reviews', 'Size', and 'Installs' columns to numerical values
df['Reviews'] = df['Reviews'].astype(int)
# df['Size'] = df['Size'].apply(lambda x: float(x.strip('M').replace(',', '')) if 'M' in x else float(x.strip('k').replace(',', '')) / 1000)
df['Installs'] = df['Installs'].apply(lambda x: int(x.strip('+').replace(',', '')))

# Clean 'Type' column
df['Type'] = df['Type'].apply(lambda x: 1 if x == 'Paid' else 0)

# Clean 'Price' column
df['Price'] = df['Price'].apply(lambda x: float(x.strip('$')) if x != '0' else 0)

# Clean 'Content Rating' column
df['Content Rating'] = df['Content Rating'].apply(lambda x: 'Everyone' if x == 'Unrated' else x)

# Convert 'Genres' column to a list of genres
df['Genres'] = df['Genres'].apply(lambda x: x.split(';')[0])

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned dataset to a new CSV file
df.to_csv('cleaned_googleplaystore1.csv', index=False)
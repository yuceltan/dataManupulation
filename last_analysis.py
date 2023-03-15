import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/pc home/Desktop/gogglestore_cleaning.csv')
lolly = pd.read_csv('/Users/pc home/Desktop/googleplaystore_user_reviews (gr3).csv')

#drop all nan values from the dataset
lolly.dropna(subset=['Translated_Review', 'Sentiment'], inplace=True)

# select only the necessary columns from the apps dataset
df = df[['App', 'Category', 'Rating']]
lolly= lolly[['App','Sentiment','Sentiment_Polarity','Sentiment_Subjectivity']]

# Merge the two dataframe
merged_df = pd.merge(lolly, df, on='App', how='left')

# merged_df.to_csv('/Users/pc home/Desktop/final.csv', index=False)

#positive
positive_cat = merged_df[merged_df["Sentiment"] == 'Positive'] 
positive_cat["Category"].value_counts()


#negative 
nagative_cat = merged_df[merged_df["Sentiment"] == 'Negative'] 
count_neg = nagative_cat["Category"].value_counts()

#neutral
neutral_cat = merged_df[merged_df["Sentiment"] == 'Neutral'] 
count_neu = neutral_cat["Category"].value_counts()






















# # Define a function to remove special characters
# def remove_special_characters(text):
#     return re.sub('[^A-Za-z0-9 ]+', '', text)

# # Remove special characters from all columns
# df = df.applymap(lambda x: remove_special_characters(str(x)))

# # Fill missing values with 'nan'
# df = df.fillna('nan')

# # Save the cleaned dataset to a new CSV file
# df.to_csv('/Users/pc home/Desktop/reviews_after_cleaning6.csv', index=False)

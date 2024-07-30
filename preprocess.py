# Load movie reviews dataset from NLTK
def load_movie_reviews():
    reviews = []
    labels = []
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            reviews.append(movie_reviews.raw(fileid))
            labels.append(category)
    return reviews, labels

reviews, labels = load_movie_reviews()

# Convert to DataFrame for convenience
df = pd.DataFrame({'review': reviews, 'label': labels})

# Encode labels: pos -> 1, neg -> 0
df['label'] = df['label'].map({'pos': 1, 'neg': 0})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['label'], test_size=0.2, random_state=42)

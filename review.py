def predict_sentiment(review):
    prediction = model.predict([review])
    return 'Positive' if prediction[0] == 1 else 'Negative'

# Test the function with a new review
new_review = "This movie was fantastic! I loved the plot and the characters."
print(predict_sentiment(new_review))


import pandas as pd
from textblob import TextBlob
import emoji
import os
from textblob.exceptions import NotTranslated

# -----------------------------------------------------------
def demojized(text):
    """This function demojizes emojis and gives score based on the emoji"""
    return emoji.demojize(str(text))

# -----------------------------------------------------------
def get_sentiment(text):
    """This function gives polarity and subjectivity of reviews"""
    cleaned = demojized(text)
    blob = TextBlob(str(cleaned))
    sentiment = blob.sentiment
    return pd.Series([sentiment.polarity, sentiment.subjectivity])

# -----------------------------------------------------------
def classify_sentiment(score):
    """This function assigns labels to reviews based on polarity"""
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------------------------------------
def sentiment_analyzer(dataset):
    # Ensure 'data' folder exists
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    # Perform sentiment analysis
    dataset[["Polarity", "Subjectivity"]] = dataset["Review Text"].apply(get_sentiment)
    
    # Assign sentiment labels
    dataset["Label"] = dataset["Polarity"].apply(classify_sentiment)
    
    # Construct full output path
    output_path = os.path.join(data_dir, "sentiment_updated_data.csv")
    
    # Save the updated dataset
    dataset.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    return dataset


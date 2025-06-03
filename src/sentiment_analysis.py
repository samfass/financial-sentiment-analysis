from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob.

    Args:
        text (str): Input text.

    Returns:
        float: Sentiment polarity.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None
